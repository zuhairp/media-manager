# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enums.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='enums.proto',
  package='media_manager',
  syntax='proto3',
  serialized_pb=_b('\n\x0b\x65nums.proto\x12\rmedia_manager*3\n\x08Location\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tDOWNLOADS\x10\x01\x12\x0b\n\x07STAGING\x10\x02\x62\x06proto3')
)

_LOCATION = _descriptor.EnumDescriptor(
  name='Location',
  full_name='media_manager.Location',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOADS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAGING', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=30,
  serialized_end=81,
)
_sym_db.RegisterEnumDescriptor(_LOCATION)

Location = enum_type_wrapper.EnumTypeWrapper(_LOCATION)
UNKNOWN = 0
DOWNLOADS = 1
STAGING = 2


DESCRIPTOR.enum_types_by_name['Location'] = _LOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
