# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from duckietown_msgs/SceneSegments.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import duckietown_msgs.msg
import std_msgs.msg
import sensor_msgs.msg

class SceneSegments(genpy.Message):
  _md5sum = "2aa3c1097b948038841bf28c11cf95cb"
  _type = "duckietown_msgs/SceneSegments"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """sensor_msgs/Image segimage
duckietown_msgs/Rect[] rects
================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of cameara
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: duckietown_msgs/Rect
# all in pixel coordinate
# (x, y, w, h) defines a rectangle
int32 x
int32 y
int32 w
int32 h
"""
  __slots__ = ['segimage','rects']
  _slot_types = ['sensor_msgs/Image','duckietown_msgs/Rect[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       segimage,rects

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SceneSegments, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.segimage is None:
        self.segimage = sensor_msgs.msg.Image()
      if self.rects is None:
        self.rects = []
    else:
      self.segimage = sensor_msgs.msg.Image()
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
      _x = self
      buff.write(_get_struct_3I().pack(_x.segimage.header.seq, _x.segimage.header.stamp.secs, _x.segimage.header.stamp.nsecs))
      _x = self.segimage.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.segimage.height, _x.segimage.width))
      _x = self.segimage.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.segimage.is_bigendian, _x.segimage.step))
      _x = self.segimage.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
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
      if self.segimage is None:
        self.segimage = sensor_msgs.msg.Image()
      if self.rects is None:
        self.rects = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.segimage.header.seq, _x.segimage.header.stamp.secs, _x.segimage.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.segimage.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.segimage.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.segimage.height, _x.segimage.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.segimage.encoding = str[start:end].decode('utf-8')
      else:
        self.segimage.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.segimage.is_bigendian, _x.segimage.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.segimage.data = str[start:end]
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
      _x = self
      buff.write(_get_struct_3I().pack(_x.segimage.header.seq, _x.segimage.header.stamp.secs, _x.segimage.header.stamp.nsecs))
      _x = self.segimage.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.segimage.height, _x.segimage.width))
      _x = self.segimage.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.segimage.is_bigendian, _x.segimage.step))
      _x = self.segimage.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
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
      if self.segimage is None:
        self.segimage = sensor_msgs.msg.Image()
      if self.rects is None:
        self.rects = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.segimage.header.seq, _x.segimage.header.stamp.secs, _x.segimage.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.segimage.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.segimage.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.segimage.height, _x.segimage.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.segimage.encoding = str[start:end].decode('utf-8')
      else:
        self.segimage.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.segimage.is_bigendian, _x.segimage.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.segimage.data = str[start:end]
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
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_4i = None
def _get_struct_4i():
    global _struct_4i
    if _struct_4i is None:
        _struct_4i = struct.Struct("<4i")
    return _struct_4i
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_BI = None
def _get_struct_BI():
    global _struct_BI
    if _struct_BI is None:
        _struct_BI = struct.Struct("<BI")
    return _struct_BI
