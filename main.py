from __future__ import annotations

import abc
from collections.abc import Sequence
import dataclasses
import io
import grpc
import queue
import re
import socket
import socketserver
import threading
from typing import Optional

from absl import app
from absl import flags
from absl import logging
from google.firestore.v1 import common_pb2
from google.firestore.v1 import document_pb2
from google.firestore.v1 import firestore_pb2
from google.firestore.v1 import firestore_pb2_grpc
from google.firestore.v1 import query_pb2


FLAG_FIRESTORE_EMULATOR = flags.DEFINE_boolean(
  name="emulator",
  default=False,
  help="Whether or not to use the Firestore Emulator; if not using the "
    "Firestore Emulator, then use prod.",
)

FLAG_RESUME_TOKEN = flags.DEFINE_string(
  name="resume_token",
  default=None,
  help="The resume token to specify (e.g. 0a0908b9d2b1dff08cf902).",
)

DATABASE = "projects/dconeybe-testing/databases/(default)"
PARENT = f"{DATABASE}/documents"
COLLECTION_ID = "WatchDemo"


class Command(abc.ABC):

  @abc.abstractmethod
  def run(self, stub: firestore_pb2_grpc.FirestoreStub) -> None:
    raise NotImplementedError


class InitializeCommand(Command):

  def run(self, stub: firestore_pb2_grpc.FirestoreStub) -> None:
    for i in range(5):
      request = firestore_pb2.CreateDocumentRequest(
        parent=PARENT,
        collection_id=COLLECTION_ID,
        document_id=f"Doc{i}",
        document=document_pb2.Document(
          fields={
            "key": document_pb2.Value(
              integer_value=42,
            ),
          },
        ),
      )

      logging.info("Creating document: %s", request.document_id)
      stub.CreateDocument(request)


class ListDocumentsCommand(Command):

  def run(self, stub: firestore_pb2_grpc.FirestoreStub) -> None:
    request = firestore_pb2.ListDocumentsRequest(
      parent=PARENT,
      collection_id=COLLECTION_ID,
    )

    logging.info("Listing documents...")
    response = stub.ListDocuments(request)

    count = 0
    for document in response.documents:
      count += 1
      logging.info(
        "#%s: %s key=%s",
        count,
        document.name,
        str(document.fields.get("key")).strip()
      )

    logging.info("Found %s documents", count)


class UpdateDocumentCommand(Command):

  def __init__(self, document_id: str, value: int) -> None:
    self.document_id = document_id
    self.value = value

  def run(self, stub: firestore_pb2_grpc.FirestoreStub) -> None:
    request = firestore_pb2.UpdateDocumentRequest(
      document=document_pb2.Document(
        name=f"{PARENT}/{COLLECTION_ID}/{self.document_id}",
        fields={
          "key": document_pb2.Value(
            integer_value=self.value,
          ),
        },
      ),
      update_mask=common_pb2.DocumentMask(
        field_paths=["key"],
      ),
      current_document=common_pb2.Precondition(
        exists = True,
      )
    )

    logging.info("Updating document: %s (setting key=%s)", self.document_id, self.value)
    stub.UpdateDocument(request)

class ListenCommand(Command):

  def __init__(self, resume_token: Optional[bytes]) -> None:
    self.resume_token = resume_token

  def run(self, stub: firestore_pb2_grpc.FirestoreStub) -> None:
    state = self.ListenerState(
      target_added=True,
      resume_token=self.resume_token,
      requests=self.ListenRequestIter(),
    )

    state.requests.enqueue(
      self.add_target_listen_request(resume_token=self.resume_token))

    remote_command_server = self.RemoteCommandServer(state)
    thread = threading.Thread(target=remote_command_server.serve_forever)
    thread.daemon = True
    thread.start()

    metadata = (
      ("google-cloud-resource-prefix", DATABASE),
      ("x-goog-request-params", DATABASE),
    )

    for response in stub.Listen(state.requests, metadata=metadata):
      logging.info("RECV %s", ListenCommand.description_from_listen_response(response))
      logging.debug("Received: ListenResponse:\n%s", response)

      target_change = response.target_change
      if not target_change:
        continue

      if target_change.target_change_type != firestore_pb2.TargetChange.TargetChangeType.NO_CHANGE:
        continue

      if len(target_change.target_ids) > 0:
        continue

      resume_token = target_change.resume_token
      if len(resume_token) > 0:
        logging.info("Updating resume token to: %s", resume_token.hex())
        state.resume_token = resume_token

  @staticmethod
  def add_target_listen_request(*, resume_token: Optional[bytes]) -> firestore_pb2.ListenRequest:
    return firestore_pb2.ListenRequest(
      database=DATABASE,
      add_target=firestore_pb2.Target(
        target_id=1,
        resume_token=resume_token,
        query=firestore_pb2.Target.QueryTarget(
          parent=PARENT,
          structured_query=query_pb2.StructuredQuery(
            where=query_pb2.StructuredQuery.Filter(
              field_filter=query_pb2.StructuredQuery.FieldFilter(
                field=query_pb2.StructuredQuery.FieldReference(
                  field_path="key",
                ),
                op=query_pb2.StructuredQuery.FieldFilter.Operator.EQUAL,
                value=document_pb2.Value(
                  integer_value=42,
                ),
              ),
            ),
            **{
              "from": [
                query_pb2.StructuredQuery.CollectionSelector(
                  collection_id=COLLECTION_ID,
                  all_descendants=False,
                ),
              ]
            }
          ),
        ),
      ),
    )

  @staticmethod
  def remove_target_listen_request() -> firestore_pb2.ListenRequest:
    return firestore_pb2.ListenRequest(
      database=DATABASE,
      remove_target=1,
    )

  @staticmethod
  def description_from_listen_request(request: firestore_pb2.ListenRequest) -> str:
    target_change = request.WhichOneof("target_change")
    if target_change == "add_target":
      if not request.add_target.resume_token:
        return f"TARGET_ADD {request.add_target.target_id}"
      else:
        return f"TARGET_ADD {request.add_target.target_id} resume_token=" + \
               request.add_target.resume_token.hex()
    elif target_change == "remove_target":
      return f"TARGET_REMOVE {request.remove_target}"
    else:
      return f"UNKNOWN target_change: {target_change}"

  @classmethod
  def description_from_listen_response(cls, response: firestore_pb2.ListenResponse) -> str:
    response_type = response.WhichOneof("response_type")
    if response_type == "target_change":
      return cls.description_from_target_change(response.target_change)
    else:
      return f"UNKNOWN response_type: {response_type}"

  @classmethod
  def description_from_target_change(cls, target_change: firestore_pb2.TargetChange) -> str:
    target_ids = tuple(str(x) for x in sorted(target_change.target_ids))
    if target_change.target_change_type == firestore_pb2.TargetChange.TargetChangeType.ADD:
      if len(target_ids) == 1:
        return f"TARGET_ADDED: {target_ids[0]}"
      else:
        return "TARGETS_ADDED: " + ", ".join(target_ids)
    elif target_change.target_change_type == firestore_pb2.TargetChange.TargetChangeType.REMOVE:
      if len(target_ids) == 1:
        return f"TARGET_REMOVED: {target_ids[0]}"
      else:
        return "TARGETS_REMOVED: " + ", ".join(target_ids)
    elif target_change.target_change_type == firestore_pb2.TargetChange.TargetChangeType.CURRENT:
      return "CURRENT " + ", ".join(target_ids)
    elif target_change.target_change_type == firestore_pb2.TargetChange.TargetChangeType.RESET:
      return "RESET " + ", ".join(target_ids)
    elif target_change.target_change_type == firestore_pb2.TargetChange.TargetChangeType.NO_CHANGE:
      if len(target_ids) == 0:
        return "GLOBAL_SNAPSHOT resume_token=" + target_change.resume_token.hex()
      else:
        return "NO_CHANGE " + + ", ".join(target_ids)
    else:
      return f"UNKNOWN target_change_type: {target_change.target_change_type}"

  class ListenRequestIter:

    def __init__(self) -> None:
      self.queue = queue.Queue()

    def enqueue(self, listen_request: firestore_pb2.ListenRequest) -> None:
      self.queue.put(listen_request)

    def __next__(self) -> firestore_pb2.ListenRequest:
      request = self.queue.get()
      logging.info("SEND %s", ListenCommand.description_from_listen_request(request))
      logging.debug("Sending: ListenRequest:\n%s", request)
      return request

  @dataclasses.dataclass
  class ListenerState:
    target_added: bool
    resume_token: Optional[bytes]
    requests: ListenCommand.ListenRequestIter

  class RemoteCommandRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
      data = self.rfile.read()
      if data == b"pause":
        self.send_listen_request(ListenCommand.remove_target_listen_request())
      elif data == b"resume":
        listen_request = ListenCommand.add_target_listen_request(
          resume_token=self.server.state.resume_token)
        self.send_listen_request(listen_request)
      elif data.startswith(b"resume:"):
        resume_token = data[len(b"resume:"):]
        listen_request = ListenCommand.add_target_listen_request(
          resume_token=resume_token)
        self.send_listen_request(listen_request)
      else:
        logging.warning("Received unknown command: %s", data)

    def send_listen_request(self, request: firestore_pb2.ListenRequest) -> None:
      self.server.state.requests.enqueue(request)

  class RemoteCommandServer(socketserver.TCPServer):

    def __init__(self, state: ListenCommand.ListenerState) -> None:
      super().__init__(("127.0.0.1", 23445), ListenCommand.RemoteCommandRequestHandler)
      self.state = state

    def serve_forever(self, *args, **kwargs):
      logging.info("Listening on %s", self.server_address)
      return super().serve_forever(*args, **kwargs)


class ListenSendCommandRPCCommand(Command):

  def __init__(self, command_name: str, command: bytes, arg: Optional[bytes] = None) -> None:
    self.command_name = command_name
    self.command = command
    self.arg = arg

  def run(self, stub: firestore_pb2_grpc.FirestoreStub) -> None:
    remote_address = ("127.0.0.1", 23445)
    with socket.socket() as s:
      logging.info("Connecting to %s", remote_address)
      s.connect(remote_address)
      if self.arg is None:
        logging.info("Sending %s command", self.command_name)
        s.sendall(self.command)
      else:
        logging.info("Sending %s command with arg: %s", self.command_name, self.arg.hex())
        s.sendall(self.command + b":" + self.arg)

class ListenPauseCommand(ListenSendCommandRPCCommand):

  def __init__(self) -> None:
    super().__init__("PAUSE", b"pause")


class ListenResumeCommand(ListenSendCommandRPCCommand):

  def __init__(self, resume_token: Optional[bytes] = None) -> None:
    super().__init__("RESUME", b"resume", resume_token)


def run_command(command: Command) -> None:
  if FLAG_FIRESTORE_EMULATOR.value:
    logging.info("Connecting to the Firestore Emulator at localhost:8080")
    grpc_channel = grpc.insecure_channel("localhost:8080")
  else:
    logging.info("Connecting to Firestore Prod at firestore.googleapis.com")
    channel_creds = grpc.ssl_channel_credentials()
    grpc_channel = grpc.secure_channel("firestore.googleapis.com", channel_creds)

  with grpc_channel:
    stub = firestore_pb2_grpc.FirestoreStub(grpc_channel)
    command.run(stub)


def main(argv: Sequence[str]) -> None:
  if len(argv) == 1:
    raise app.UsageError("no command specified; supported commands are: init ls set:DocN=999 listen")
  elif len(argv) > 2:
    raise app.UsageError(f"unexpected argument: {argv[2]}")

  resume_token_str = FLAG_RESUME_TOKEN.value
  resume_token = bytes.fromhex(resume_token_str) if resume_token_str else None

  command_str = argv[1]
  command: Command
  if command_str == "init":
    command = InitializeCommand()
  elif command_str == "ls":
    command = ListDocumentsCommand()
  elif command_str.startswith("set:"):
    match = re.fullmatch(r"set:(\w+)=(\d+)", command_str)
    if not match:
      raise app.UsageError(f"invalid set command: {command_str} (expected set:DocId=IntValue)")
    command = UpdateDocumentCommand(document_id=match.group(1), value=int(match.group(2)))
  elif command_str == "listen":
    command = ListenCommand(resume_token)
  elif command_str == "pause":
    command = ListenPauseCommand()
  elif command_str == "resume":
    command = ListenResumeCommand(resume_token)
  elif command_str.startswith("resume:"):
    resume_token = bytes.fromhex(command_str[len("resume:"):])
    command = ListenResumeCommand(resume_token=resume_token)
  else:
    raise app.UsageError(f"unsupported command: {command_str}")

  run_command(command)


if __name__ == "__main__":
  app.run(main)
