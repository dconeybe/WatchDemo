from collections.abc import Sequence

import grpc

from absl import app
from absl import logging
from google.firestore.v1 import document_pb2
from google.firestore.v1 import firestore_pb2
from google.firestore.v1 import firestore_pb2_grpc

def main(argv: Sequence[str]) -> None:
  if len(argv) > 1:
    raise app.UsageError(f"unexpected argument: {argv[1]}")

  with grpc.insecure_channel('localhost:8080') as grpc_channel:
    stub = firestore_pb2_grpc.FirestoreStub(grpc_channel)

    create_document_request = firestore_pb2.CreateDocumentRequest(
      parent="projects/dconeybe-testing/databases/(default)/documents",
      collection_id="col",
      document_id="doc",
      document=document_pb2.Document(),
    )
    create_document_response = stub.CreateDocument(create_document_request)
    print(f"created document: {create_document_request}")

    get_document_request = firestore_pb2.GetDocumentRequest(
      name="projects/dconeybe-testing/databases/(default)/documents/col/doc",
    )
    document = stub.GetDocument(get_document_request)
    print(f"got document: {document}")



if __name__ == "__main__":
  app.run(main)
