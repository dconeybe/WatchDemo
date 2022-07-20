# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/firestore/v1/document.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"google/firestore/v1/document.proto\x12\x13google.firestore.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18google/type/latlng.proto\"\x80\x02\n\x08\x44ocument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x39\n\x06\x66ields\x18\x02 \x03(\x0b\x32).google.firestore.v1.Document.FieldsEntry\x12/\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1aI\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.firestore.v1.Value:\x02\x38\x01\"\xae\x03\n\x05Value\x12\x30\n\nnull_value\x18\x0b \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00\x12\x17\n\rboolean_value\x18\x01 \x01(\x08H\x00\x12\x17\n\rinteger_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x03 \x01(\x01H\x00\x12\x35\n\x0ftimestamp_value\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12\x16\n\x0cstring_value\x18\x11 \x01(\tH\x00\x12\x15\n\x0b\x62ytes_value\x18\x12 \x01(\x0cH\x00\x12\x19\n\x0freference_value\x18\x05 \x01(\tH\x00\x12.\n\x0fgeo_point_value\x18\x08 \x01(\x0b\x32\x13.google.type.LatLngH\x00\x12\x36\n\x0b\x61rray_value\x18\t \x01(\x0b\x32\x1f.google.firestore.v1.ArrayValueH\x00\x12\x32\n\tmap_value\x18\x06 \x01(\x0b\x32\x1d.google.firestore.v1.MapValueH\x00\x42\x0c\n\nvalue_type\"8\n\nArrayValue\x12*\n\x06values\x18\x01 \x03(\x0b\x32\x1a.google.firestore.v1.Value\"\x90\x01\n\x08MapValue\x12\x39\n\x06\x66ields\x18\x01 \x03(\x0b\x32).google.firestore.v1.MapValue.FieldsEntry\x1aI\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.firestore.v1.Value:\x02\x38\x01\x42\xc6\x01\n\x17\x63om.google.firestore.v1B\rDocumentProtoP\x01Z<google.golang.org/genproto/googleapis/firestore/v1;firestore\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1b\x06proto3')



_DOCUMENT = DESCRIPTOR.message_types_by_name['Document']
_DOCUMENT_FIELDSENTRY = _DOCUMENT.nested_types_by_name['FieldsEntry']
_VALUE = DESCRIPTOR.message_types_by_name['Value']
_ARRAYVALUE = DESCRIPTOR.message_types_by_name['ArrayValue']
_MAPVALUE = DESCRIPTOR.message_types_by_name['MapValue']
_MAPVALUE_FIELDSENTRY = _MAPVALUE.nested_types_by_name['FieldsEntry']
Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENT_FIELDSENTRY,
    '__module__' : 'google.firestore.v1.document_pb2'
    # @@protoc_insertion_point(class_scope:google.firestore.v1.Document.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'google.firestore.v1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.Document)
  })
_sym_db.RegisterMessage(Document)
_sym_db.RegisterMessage(Document.FieldsEntry)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'google.firestore.v1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.Value)
  })
_sym_db.RegisterMessage(Value)

ArrayValue = _reflection.GeneratedProtocolMessageType('ArrayValue', (_message.Message,), {
  'DESCRIPTOR' : _ARRAYVALUE,
  '__module__' : 'google.firestore.v1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.ArrayValue)
  })
_sym_db.RegisterMessage(ArrayValue)

MapValue = _reflection.GeneratedProtocolMessageType('MapValue', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAPVALUE_FIELDSENTRY,
    '__module__' : 'google.firestore.v1.document_pb2'
    # @@protoc_insertion_point(class_scope:google.firestore.v1.MapValue.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _MAPVALUE,
  '__module__' : 'google.firestore.v1.document_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.MapValue)
  })
_sym_db.RegisterMessage(MapValue)
_sym_db.RegisterMessage(MapValue.FieldsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.google.firestore.v1B\rDocumentProtoP\001Z<google.golang.org/genproto/googleapis/firestore/v1;firestore\242\002\004GCFS\252\002\031Google.Cloud.Firestore.V1\312\002\031Google\\Cloud\\Firestore\\V1\352\002\034Google::Cloud::Firestore::V1'
  _DOCUMENT_FIELDSENTRY._options = None
  _DOCUMENT_FIELDSENTRY._serialized_options = b'8\001'
  _MAPVALUE_FIELDSENTRY._options = None
  _MAPVALUE_FIELDSENTRY._serialized_options = b'8\001'
  _DOCUMENT._serialized_start=149
  _DOCUMENT._serialized_end=405
  _DOCUMENT_FIELDSENTRY._serialized_start=332
  _DOCUMENT_FIELDSENTRY._serialized_end=405
  _VALUE._serialized_start=408
  _VALUE._serialized_end=838
  _ARRAYVALUE._serialized_start=840
  _ARRAYVALUE._serialized_end=896
  _MAPVALUE._serialized_start=899
  _MAPVALUE._serialized_end=1043
  _MAPVALUE_FIELDSENTRY._serialized_start=332
  _MAPVALUE_FIELDSENTRY._serialized_end=405
# @@protoc_insertion_point(module_scope)
