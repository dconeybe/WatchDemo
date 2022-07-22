import abc
from collections.abc import Sequence
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

  def run(self, stub: firestore_pb2_grpc.FirestoreStub) -> None:

    class ListenRequestIter:

      def __init__(self) -> None:
        self.queue = queue.Queue()

      def enqueue(self, listen_request: firestore_pb2.ListenRequest) -> None:
        self.queue.put(listen_request)

      def __next__(self) -> firestore_pb2.ListenRequest:
        request = self.queue.get()
        logging.info("Sending: ListenRequest:\n%s", request)
        return request

    class RemoteCommandRequestHandler(socketserver.StreamRequestHandler):

      def handle(self):
        data = self.rfile.read()
        if data == b"pause":
          self.send_listen_request(ListenCommand.remove_target_listen_request())
        elif data == b"resume":
          resume_token = self.server.resume_token
          if not resume_token:
            self.send_listen_request(ListenCommand.add_target_listen_request())
          else:
            self.send_listen_request(ListenCommand.add_target_listen_request(resume_token))
        elif data.startswith(b"resume:"):
          resume_token = data[len(b"resume:"):]
          self.send_listen_request(ListenCommand.add_target_listen_request(resume_token))
        else:
          logging.warning("Received unknown command: %s", data)

      def send_listen_request(self, request: firestore_pb2.ListenRequest) -> None:
        self.server.q.enqueue(request)

    class RemoteCommandServer(socketserver.TCPServer):

      def __init__(self, q: ListenRequestIter):
        super().__init__(("127.0.0.1", 23445), RemoteCommandRequestHandler)
        self.q = q
        self.resume_token: Optional[bytes] = None

      def serve_forever(self, *args, **kwargs):
        logging.info("Listening on %s", self.server_address)
        return super().serve_forever(*args, **kwargs)

    listen_request_iter = ListenRequestIter()
    remote_command_server = RemoteCommandServer(q=listen_request_iter)
    thread = threading.Thread(target=remote_command_server.serve_forever)
    thread.daemon = True
    thread.start()

    listen_request_iter.enqueue(
      firestore_pb2.ListenRequest(
        database=DATABASE,
        add_target=firestore_pb2.Target(
          target_id=1,
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
    )

    metadata = (
      ("google-cloud-resource-prefix", DATABASE),
      ("x-goog-request-params", DATABASE),
    )

    for listen_response in stub.Listen(listen_request_iter, metadata=metadata):
      logging.info("Received: ListenResponse:\n%s", listen_response)

      target_change = listen_response.target_change
      if not target_change:
        continue

      if target_change.target_change_type != firestore_pb2.TargetChange.TargetChangeType.NO_CHANGE:
        continue

      if len(target_change.target_ids) > 0:
        continue

      resume_token = target_change.resume_token
      if len(resume_token) > 0:
        logging.info("Updating resume token to: %s", resume_token.hex())
        remote_command_server.resume_token = resume_token



  @staticmethod
  def add_target_listen_request(resume_token: Optional[bytes] = None) -> firestore_pb2.ListenRequest:
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
    command = ListenCommand()
  elif command_str == "pause":
    command = ListenPauseCommand()
  elif command_str == "resume":
    command = ListenResumeCommand()
  elif command_str.startswith("resume:"):
    resume_token = bytes.fromhex(command_str[len("resume:"):])
    command = ListenResumeCommand(resume_token=resume_token)
  else:
    raise app.UsageError(f"unsupported command: {command_str}")

  run_command(command)


if __name__ == "__main__":
  app.run(main)
