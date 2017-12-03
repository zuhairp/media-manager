# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common.messages.fileslist_pb2 as fileslist__pb2
import common.messages.unrar_pb2 as unrar__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='meda_manager',
  syntax='proto3',
  serialized_pb=_b('\n\rmessage.proto\x12\x0cmeda_manager\x1a\x0f\x66ileslist.proto\x1a\x0bunrar.proto\"w\n\x07Request\x12\x35\n\tfilenames\x18\x01 \x01(\x0b\x32 .media_manager.fileslist.RequestH\x00\x12-\n\x05unrar\x18\x02 \x01(\x0b\x32\x1c.media_manager.unrar.RequestH\x00\x42\x06\n\x04type\"z\n\x08Response\x12\x36\n\tfilenames\x18\x01 \x01(\x0b\x32!.media_manager.fileslist.ResponseH\x00\x12.\n\x05unrar\x18\x02 \x01(\x0b\x32\x1d.media_manager.unrar.ResponseH\x00\x42\x06\n\x04typeb\x06proto3')
  ,
  dependencies=[fileslist__pb2.DESCRIPTOR,unrar__pb2.DESCRIPTOR,])




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='meda_manager.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filenames', full_name='meda_manager.Request.filenames', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unrar', full_name='meda_manager.Request.unrar', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='meda_manager.Request.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=61,
  serialized_end=180,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='meda_manager.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filenames', full_name='meda_manager.Response.filenames', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unrar', full_name='meda_manager.Response.unrar', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='meda_manager.Response.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=182,
  serialized_end=304,
)

_REQUEST.fields_by_name['filenames'].message_type = fileslist__pb2._REQUEST
_REQUEST.fields_by_name['unrar'].message_type = unrar__pb2._REQUEST
_REQUEST.oneofs_by_name['type'].fields.append(
  _REQUEST.fields_by_name['filenames'])
_REQUEST.fields_by_name['filenames'].containing_oneof = _REQUEST.oneofs_by_name['type']
_REQUEST.oneofs_by_name['type'].fields.append(
  _REQUEST.fields_by_name['unrar'])
_REQUEST.fields_by_name['unrar'].containing_oneof = _REQUEST.oneofs_by_name['type']
_RESPONSE.fields_by_name['filenames'].message_type = fileslist__pb2._RESPONSE
_RESPONSE.fields_by_name['unrar'].message_type = unrar__pb2._RESPONSE
_RESPONSE.oneofs_by_name['type'].fields.append(
  _RESPONSE.fields_by_name['filenames'])
_RESPONSE.fields_by_name['filenames'].containing_oneof = _RESPONSE.oneofs_by_name['type']
_RESPONSE.oneofs_by_name['type'].fields.append(
  _RESPONSE.fields_by_name['unrar'])
_RESPONSE.fields_by_name['unrar'].containing_oneof = _RESPONSE.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:meda_manager.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:meda_manager.Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
