# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/ByteMultiArray.proto

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
  name='proto/ByteMultiArray.proto',
  package='duckietown.fleet_comms',
  serialized_pb=_b('\n\x1aproto/ByteMultiArray.proto\x12\x16\x64uckietown.fleet_comms\"B\n\x13MultiArrayDimension\x12\r\n\x05label\x18\x01 \x02(\t\x12\x0c\n\x04size\x18\x02 \x01(\r\x12\x0e\n\x06stride\x18\x03 \x01(\r\"a\n\x10MultiArrayLayout\x12\x38\n\x03\x64im\x18\x01 \x03(\x0b\x32+.duckietown.fleet_comms.MultiArrayDimension\x12\x13\n\x0b\x64\x61ta_offset\x18\x02 \x02(\r\"X\n\x0e\x42yteMultiArray\x12\x38\n\x06layout\x18\x01 \x01(\x0b\x32(.duckietown.fleet_comms.MultiArrayLayout\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MULTIARRAYDIMENSION = _descriptor.Descriptor(
  name='MultiArrayDimension',
  full_name='duckietown.fleet_comms.MultiArrayDimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='duckietown.fleet_comms.MultiArrayDimension.label', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='duckietown.fleet_comms.MultiArrayDimension.size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stride', full_name='duckietown.fleet_comms.MultiArrayDimension.stride', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=120,
)


_MULTIARRAYLAYOUT = _descriptor.Descriptor(
  name='MultiArrayLayout',
  full_name='duckietown.fleet_comms.MultiArrayLayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dim', full_name='duckietown.fleet_comms.MultiArrayLayout.dim', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_offset', full_name='duckietown.fleet_comms.MultiArrayLayout.data_offset', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=219,
)


_BYTEMULTIARRAY = _descriptor.Descriptor(
  name='ByteMultiArray',
  full_name='duckietown.fleet_comms.ByteMultiArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layout', full_name='duckietown.fleet_comms.ByteMultiArray.layout', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='duckietown.fleet_comms.ByteMultiArray.data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=221,
  serialized_end=309,
)

_MULTIARRAYLAYOUT.fields_by_name['dim'].message_type = _MULTIARRAYDIMENSION
_BYTEMULTIARRAY.fields_by_name['layout'].message_type = _MULTIARRAYLAYOUT
DESCRIPTOR.message_types_by_name['MultiArrayDimension'] = _MULTIARRAYDIMENSION
DESCRIPTOR.message_types_by_name['MultiArrayLayout'] = _MULTIARRAYLAYOUT
DESCRIPTOR.message_types_by_name['ByteMultiArray'] = _BYTEMULTIARRAY

MultiArrayDimension = _reflection.GeneratedProtocolMessageType('MultiArrayDimension', (_message.Message,), dict(
  DESCRIPTOR = _MULTIARRAYDIMENSION,
  __module__ = 'proto.ByteMultiArray_pb2'
  # @@protoc_insertion_point(class_scope:duckietown.fleet_comms.MultiArrayDimension)
  ))
_sym_db.RegisterMessage(MultiArrayDimension)

MultiArrayLayout = _reflection.GeneratedProtocolMessageType('MultiArrayLayout', (_message.Message,), dict(
  DESCRIPTOR = _MULTIARRAYLAYOUT,
  __module__ = 'proto.ByteMultiArray_pb2'
  # @@protoc_insertion_point(class_scope:duckietown.fleet_comms.MultiArrayLayout)
  ))
_sym_db.RegisterMessage(MultiArrayLayout)

ByteMultiArray = _reflection.GeneratedProtocolMessageType('ByteMultiArray', (_message.Message,), dict(
  DESCRIPTOR = _BYTEMULTIARRAY,
  __module__ = 'proto.ByteMultiArray_pb2'
  # @@protoc_insertion_point(class_scope:duckietown.fleet_comms.ByteMultiArray)
  ))
_sym_db.RegisterMessage(ByteMultiArray)


# @@protoc_insertion_point(module_scope)
