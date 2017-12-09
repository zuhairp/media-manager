# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unrar.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='unrar.proto',
  package='media_manager.unrar',
  syntax='proto3',
  serialized_pb=_b('\n\x0bunrar.proto\x12\x13media_manager.unrar\"\'\n\x07Request\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"\xbd\x02\n\x08Response\x12\n\n\x02id\x18\x01 \x01(\t\x12:\n\x08\x61\x63\x63\x65pted\x18\x02 \x01(\x0b\x32&.media_manager.unrar.Response.AcceptedH\x00\x12\x36\n\x06status\x18\x03 \x01(\x0b\x32$.media_manager.unrar.Response.StatusH\x00\x12<\n\tcompleted\x18\x04 \x01(\x0b\x32\'.media_manager.unrar.Response.CompletedH\x00\x1a\x1e\n\x08\x41\x63\x63\x65pted\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\x1a*\n\x06Status\x12\x11\n\tcompleted\x18\x01 \x01(\x05\x12\r\n\x05total\x18\x02 \x01(\x05\x1a\x1f\n\tCompleted\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\x42\x06\n\x04typeb\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='media_manager.unrar.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='media_manager.unrar.Request.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='media_manager.unrar.Request.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  ],
  serialized_start=36,
  serialized_end=75,
)


_RESPONSE_ACCEPTED = _descriptor.Descriptor(
  name='Accepted',
  full_name='media_manager.unrar.Response.Accepted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='successful', full_name='media_manager.unrar.Response.Accepted.successful', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  ],
  serialized_start=280,
  serialized_end=310,
)

_RESPONSE_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='media_manager.unrar.Response.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='completed', full_name='media_manager.unrar.Response.Status.completed', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='media_manager.unrar.Response.Status.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  ],
  serialized_start=312,
  serialized_end=354,
)

_RESPONSE_COMPLETED = _descriptor.Descriptor(
  name='Completed',
  full_name='media_manager.unrar.Response.Completed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='successful', full_name='media_manager.unrar.Response.Completed.successful', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  ],
  serialized_start=356,
  serialized_end=387,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='media_manager.unrar.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='media_manager.unrar.Response.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accepted', full_name='media_manager.unrar.Response.accepted', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='media_manager.unrar.Response.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='completed', full_name='media_manager.unrar.Response.completed', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_ACCEPTED, _RESPONSE_STATUS, _RESPONSE_COMPLETED, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='media_manager.unrar.Response.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=78,
  serialized_end=395,
)

_RESPONSE_ACCEPTED.containing_type = _RESPONSE
_RESPONSE_STATUS.containing_type = _RESPONSE
_RESPONSE_COMPLETED.containing_type = _RESPONSE
_RESPONSE.fields_by_name['accepted'].message_type = _RESPONSE_ACCEPTED
_RESPONSE.fields_by_name['status'].message_type = _RESPONSE_STATUS
_RESPONSE.fields_by_name['completed'].message_type = _RESPONSE_COMPLETED
_RESPONSE.oneofs_by_name['type'].fields.append(
  _RESPONSE.fields_by_name['accepted'])
_RESPONSE.fields_by_name['accepted'].containing_oneof = _RESPONSE.oneofs_by_name['type']
_RESPONSE.oneofs_by_name['type'].fields.append(
  _RESPONSE.fields_by_name['status'])
_RESPONSE.fields_by_name['status'].containing_oneof = _RESPONSE.oneofs_by_name['type']
_RESPONSE.oneofs_by_name['type'].fields.append(
  _RESPONSE.fields_by_name['completed'])
_RESPONSE.fields_by_name['completed'].containing_oneof = _RESPONSE.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'unrar_pb2'
  # @@protoc_insertion_point(class_scope:media_manager.unrar.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Accepted = _reflection.GeneratedProtocolMessageType('Accepted', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ACCEPTED,
    __module__ = 'unrar_pb2'
    # @@protoc_insertion_point(class_scope:media_manager.unrar.Response.Accepted)
    ))
  ,

  Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_STATUS,
    __module__ = 'unrar_pb2'
    # @@protoc_insertion_point(class_scope:media_manager.unrar.Response.Status)
    ))
  ,

  Completed = _reflection.GeneratedProtocolMessageType('Completed', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_COMPLETED,
    __module__ = 'unrar_pb2'
    # @@protoc_insertion_point(class_scope:media_manager.unrar.Response.Completed)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'unrar_pb2'
  # @@protoc_insertion_point(class_scope:media_manager.unrar.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Accepted)
_sym_db.RegisterMessage(Response.Status)
_sym_db.RegisterMessage(Response.Completed)


# @@protoc_insertion_point(module_scope)