# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.firestore.v1 import document_pb2 as google_dot_firestore_dot_v1_dot_document__pb2
from google.firestore.v1 import firestore_pb2 as google_dot_firestore_dot_v1_dot_firestore__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class FirestoreStub(object):
    """Specification of the Firestore API.

    The Cloud Firestore service.

    Cloud Firestore is a fast, fully managed, serverless, cloud-native NoSQL
    document database that simplifies storing, syncing, and querying data for
    your mobile, web, and IoT apps at global scale. Its client libraries provide
    live synchronization and offline support, while its security features and
    integrations with Firebase and Google Cloud Platform (GCP) accelerate
    building truly serverless apps.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDocument = channel.unary_unary(
                '/google.firestore.v1.Firestore/GetDocument',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.GetDocumentRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_document__pb2.Document.FromString,
                )
        self.ListDocuments = channel.unary_unary(
                '/google.firestore.v1.Firestore/ListDocuments',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListDocumentsRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListDocumentsResponse.FromString,
                )
        self.UpdateDocument = channel.unary_unary(
                '/google.firestore.v1.Firestore/UpdateDocument',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.UpdateDocumentRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_document__pb2.Document.FromString,
                )
        self.DeleteDocument = channel.unary_unary(
                '/google.firestore.v1.Firestore/DeleteDocument',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.DeleteDocumentRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.BatchGetDocuments = channel.unary_stream(
                '/google.firestore.v1.Firestore/BatchGetDocuments',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BatchGetDocumentsRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BatchGetDocumentsResponse.FromString,
                )
        self.BeginTransaction = channel.unary_unary(
                '/google.firestore.v1.Firestore/BeginTransaction',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BeginTransactionRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BeginTransactionResponse.FromString,
                )
        self.Commit = channel.unary_unary(
                '/google.firestore.v1.Firestore/Commit',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.CommitRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.CommitResponse.FromString,
                )
        self.Rollback = channel.unary_unary(
                '/google.firestore.v1.Firestore/Rollback',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.RollbackRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.RunQuery = channel.unary_stream(
                '/google.firestore.v1.Firestore/RunQuery',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.RunQueryRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.RunQueryResponse.FromString,
                )
        self.PartitionQuery = channel.unary_unary(
                '/google.firestore.v1.Firestore/PartitionQuery',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.PartitionQueryRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.PartitionQueryResponse.FromString,
                )
        self.Write = channel.stream_stream(
                '/google.firestore.v1.Firestore/Write',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.WriteRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.WriteResponse.FromString,
                )
        self.Listen = channel.stream_stream(
                '/google.firestore.v1.Firestore/Listen',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListenRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListenResponse.FromString,
                )
        self.ListCollectionIds = channel.unary_unary(
                '/google.firestore.v1.Firestore/ListCollectionIds',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListCollectionIdsRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListCollectionIdsResponse.FromString,
                )
        self.BatchWrite = channel.unary_unary(
                '/google.firestore.v1.Firestore/BatchWrite',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BatchWriteRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BatchWriteResponse.FromString,
                )
        self.CreateDocument = channel.unary_unary(
                '/google.firestore.v1.Firestore/CreateDocument',
                request_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.CreateDocumentRequest.SerializeToString,
                response_deserializer=google_dot_firestore_dot_v1_dot_document__pb2.Document.FromString,
                )


class FirestoreServicer(object):
    """Specification of the Firestore API.

    The Cloud Firestore service.

    Cloud Firestore is a fast, fully managed, serverless, cloud-native NoSQL
    document database that simplifies storing, syncing, and querying data for
    your mobile, web, and IoT apps at global scale. Its client libraries provide
    live synchronization and offline support, while its security features and
    integrations with Firebase and Google Cloud Platform (GCP) accelerate
    building truly serverless apps.
    """

    def GetDocument(self, request, context):
        """Gets a single document.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDocuments(self, request, context):
        """Lists documents.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDocument(self, request, context):
        """Updates or inserts a document.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDocument(self, request, context):
        """Deletes a document.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetDocuments(self, request, context):
        """Gets multiple documents.

        Documents returned by this method are not guaranteed to be returned in the
        same order that they were requested.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BeginTransaction(self, request, context):
        """Starts a new transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Commit(self, request, context):
        """Commits a transaction, while optionally updating documents.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Rollback(self, request, context):
        """Rolls back a transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunQuery(self, request, context):
        """Runs a query.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PartitionQuery(self, request, context):
        """Partitions a query by returning partition cursors that can be used to run
        the query in parallel. The returned partition cursors are split points that
        can be used by RunQuery as starting/end points for the query results.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request_iterator, context):
        """Streams batches of document updates and deletes, in order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Listen(self, request_iterator, context):
        """Listens to changes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCollectionIds(self, request, context):
        """Lists all the collection IDs underneath a document.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchWrite(self, request, context):
        """Applies a batch of write operations.

        The BatchWrite method does not apply the write operations atomically
        and can apply them out of order. Method does not allow more than one write
        per document. Each write succeeds or fails independently. See the
        [BatchWriteResponse][google.firestore.v1.BatchWriteResponse] for the success status of each write.

        If you require an atomically applied set of writes, use
        [Commit][google.firestore.v1.Firestore.Commit] instead.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDocument(self, request, context):
        """Creates a new document.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FirestoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDocument': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDocument,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.GetDocumentRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_document__pb2.Document.SerializeToString,
            ),
            'ListDocuments': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDocuments,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListDocumentsRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListDocumentsResponse.SerializeToString,
            ),
            'UpdateDocument': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDocument,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.UpdateDocumentRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_document__pb2.Document.SerializeToString,
            ),
            'DeleteDocument': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDocument,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.DeleteDocumentRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'BatchGetDocuments': grpc.unary_stream_rpc_method_handler(
                    servicer.BatchGetDocuments,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BatchGetDocumentsRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BatchGetDocumentsResponse.SerializeToString,
            ),
            'BeginTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.BeginTransaction,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BeginTransactionRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BeginTransactionResponse.SerializeToString,
            ),
            'Commit': grpc.unary_unary_rpc_method_handler(
                    servicer.Commit,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.CommitRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.CommitResponse.SerializeToString,
            ),
            'Rollback': grpc.unary_unary_rpc_method_handler(
                    servicer.Rollback,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.RollbackRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RunQuery': grpc.unary_stream_rpc_method_handler(
                    servicer.RunQuery,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.RunQueryRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.RunQueryResponse.SerializeToString,
            ),
            'PartitionQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.PartitionQuery,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.PartitionQueryRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.PartitionQueryResponse.SerializeToString,
            ),
            'Write': grpc.stream_stream_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.WriteRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.WriteResponse.SerializeToString,
            ),
            'Listen': grpc.stream_stream_rpc_method_handler(
                    servicer.Listen,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListenRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListenResponse.SerializeToString,
            ),
            'ListCollectionIds': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCollectionIds,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListCollectionIdsRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.ListCollectionIdsResponse.SerializeToString,
            ),
            'BatchWrite': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchWrite,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BatchWriteRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_firestore__pb2.BatchWriteResponse.SerializeToString,
            ),
            'CreateDocument': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDocument,
                    request_deserializer=google_dot_firestore_dot_v1_dot_firestore__pb2.CreateDocumentRequest.FromString,
                    response_serializer=google_dot_firestore_dot_v1_dot_document__pb2.Document.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.firestore.v1.Firestore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Firestore(object):
    """Specification of the Firestore API.

    The Cloud Firestore service.

    Cloud Firestore is a fast, fully managed, serverless, cloud-native NoSQL
    document database that simplifies storing, syncing, and querying data for
    your mobile, web, and IoT apps at global scale. Its client libraries provide
    live synchronization and offline support, while its security features and
    integrations with Firebase and Google Cloud Platform (GCP) accelerate
    building truly serverless apps.
    """

    @staticmethod
    def GetDocument(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/GetDocument',
            google_dot_firestore_dot_v1_dot_firestore__pb2.GetDocumentRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_document__pb2.Document.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDocuments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/ListDocuments',
            google_dot_firestore_dot_v1_dot_firestore__pb2.ListDocumentsRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_firestore__pb2.ListDocumentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDocument(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/UpdateDocument',
            google_dot_firestore_dot_v1_dot_firestore__pb2.UpdateDocumentRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_document__pb2.Document.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDocument(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/DeleteDocument',
            google_dot_firestore_dot_v1_dot_firestore__pb2.DeleteDocumentRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchGetDocuments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/google.firestore.v1.Firestore/BatchGetDocuments',
            google_dot_firestore_dot_v1_dot_firestore__pb2.BatchGetDocumentsRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_firestore__pb2.BatchGetDocumentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BeginTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/BeginTransaction',
            google_dot_firestore_dot_v1_dot_firestore__pb2.BeginTransactionRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_firestore__pb2.BeginTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Commit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/Commit',
            google_dot_firestore_dot_v1_dot_firestore__pb2.CommitRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_firestore__pb2.CommitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Rollback(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/Rollback',
            google_dot_firestore_dot_v1_dot_firestore__pb2.RollbackRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/google.firestore.v1.Firestore/RunQuery',
            google_dot_firestore_dot_v1_dot_firestore__pb2.RunQueryRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_firestore__pb2.RunQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PartitionQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/PartitionQuery',
            google_dot_firestore_dot_v1_dot_firestore__pb2.PartitionQueryRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_firestore__pb2.PartitionQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/google.firestore.v1.Firestore/Write',
            google_dot_firestore_dot_v1_dot_firestore__pb2.WriteRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_firestore__pb2.WriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Listen(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/google.firestore.v1.Firestore/Listen',
            google_dot_firestore_dot_v1_dot_firestore__pb2.ListenRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_firestore__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCollectionIds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/ListCollectionIds',
            google_dot_firestore_dot_v1_dot_firestore__pb2.ListCollectionIdsRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_firestore__pb2.ListCollectionIdsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchWrite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/BatchWrite',
            google_dot_firestore_dot_v1_dot_firestore__pb2.BatchWriteRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_firestore__pb2.BatchWriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDocument(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.firestore.v1.Firestore/CreateDocument',
            google_dot_firestore_dot_v1_dot_firestore__pb2.CreateDocumentRequest.SerializeToString,
            google_dot_firestore_dot_v1_dot_document__pb2.Document.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
