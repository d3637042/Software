# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from duckietown_msgs/Rects.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import duckietown_msgs.msg

class Rects(genpy.Message):
  _md5sum = "f5b74b2b15b5d4d2f299389f9f4ca7f8"
  _type = "duckietown_msgs/Rects"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """duckietown_msgs/Rect[] rects
================================================================================
MSG: duckietown_msgs/Rect
# all in pixel coordinate
# (x, y, w, h) defines a rectangle
int32 x
int32 y
int32 w
int32 h
"""
  __slots__ = ['rects']
  _slot_types = ['duckietown_msgs/Rect[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       rects

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Rects, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.rects is None:
        self.rects = []
    else:
      self.rects = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.rects)
      buff.write(_struct_I.pack(length))
      for val1 in self.rects:
        _x = val1
        buff.write(_get_struct_4i().pack(_x.x, _x.y, _x.w, _x.h))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.rects is None:
        self.rects = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.rects = []
      for i in range(0, length):
        val1 = duckietown_msgs.msg.Rect()
        _x = val1
        start = end
        end += 16
        (_x.x, _x.y, _x.w, _x.h,) = _get_struct_4i().unpack(str[start:end])
        self.rects.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.rects)
      buff.write(_struct_I.pack(length))
      for val1 in self.rects:
        _x = val1
        buff.write(_get_struct_4i().pack(_x.x, _x.y, _x.w, _x.h))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.rects is None:
        self.rects = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.rects = []
      for i in range(0, length):
        val1 = duckietown_msgs.msg.Rect()
        _x = val1
        start = end
        end += 16
        (_x.x, _x.y, _x.w, _x.h,) = _get_struct_4i().unpack(str[start:end])
        self.rects.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4i = None
def _get_struct_4i():
    global _struct_4i
    if _struct_4i is None:
        _struct_4i = struct.Struct("<4i")
    return _struct_4i
