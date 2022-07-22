from collections.abc import Sequence

import abc
import grpc
import queue
import re

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
    q = [
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
            ),
          ),
        ),
      )
    ]

    for listen_response in stub.Listen(iter(q)):
      logging.info("%s", listen_response)


def main(argv: Sequence[str]) -> None:
  if len(argv) == 1:
    raise app.UsageError("no command specified; supported commands are: init ls set:DocN=999 listen")
  elif len(argv) == 2:
    command_str = argv[1]
  elif len(argv) > 2:
    raise app.UsageError(f"unexpected argument: {argv[2]}")

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
  else:
    raise app.UsageError(f"unsupported command: {command_str}")

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


if __name__ == "__main__":
  app.run(main)
