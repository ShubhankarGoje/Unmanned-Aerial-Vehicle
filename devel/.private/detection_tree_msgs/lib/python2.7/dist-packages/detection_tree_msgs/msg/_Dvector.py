# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from detection_tree_msgs/Dvector.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class Dvector(genpy.Message):
  _md5sum = "ac5b92b151d663eccd740b80612c355c"
  _type = "detection_tree_msgs/Dvector"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 dvector_num
std_msgs/Header camera_header
geometry_msgs/Point sub_pt
float64 azimuth
float64 elevation
int64 box_height
int64 box_width
string class_id
int32 dobject_num
float64 probability
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
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['dvector_num','camera_header','sub_pt','azimuth','elevation','box_height','box_width','class_id','dobject_num','probability']
  _slot_types = ['int32','std_msgs/Header','geometry_msgs/Point','float64','float64','int64','int64','string','int32','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       dvector_num,camera_header,sub_pt,azimuth,elevation,box_height,box_width,class_id,dobject_num,probability

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Dvector, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.dvector_num is None:
        self.dvector_num = 0
      if self.camera_header is None:
        self.camera_header = std_msgs.msg.Header()
      if self.sub_pt is None:
        self.sub_pt = geometry_msgs.msg.Point()
      if self.azimuth is None:
        self.azimuth = 0.
      if self.elevation is None:
        self.elevation = 0.
      if self.box_height is None:
        self.box_height = 0
      if self.box_width is None:
        self.box_width = 0
      if self.class_id is None:
        self.class_id = ''
      if self.dobject_num is None:
        self.dobject_num = 0
      if self.probability is None:
        self.probability = 0.
    else:
      self.dvector_num = 0
      self.camera_header = std_msgs.msg.Header()
      self.sub_pt = geometry_msgs.msg.Point()
      self.azimuth = 0.
      self.elevation = 0.
      self.box_height = 0
      self.box_width = 0
      self.class_id = ''
      self.dobject_num = 0
      self.probability = 0.

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
      buff.write(_get_struct_i3I().pack(_x.dvector_num, _x.camera_header.seq, _x.camera_header.stamp.secs, _x.camera_header.stamp.nsecs))
      _x = self.camera_header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_5d2q().pack(_x.sub_pt.x, _x.sub_pt.y, _x.sub_pt.z, _x.azimuth, _x.elevation, _x.box_height, _x.box_width))
      _x = self.class_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_id().pack(_x.dobject_num, _x.probability))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.camera_header is None:
        self.camera_header = std_msgs.msg.Header()
      if self.sub_pt is None:
        self.sub_pt = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.dvector_num, _x.camera_header.seq, _x.camera_header.stamp.secs, _x.camera_header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.camera_header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.camera_header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.sub_pt.x, _x.sub_pt.y, _x.sub_pt.z, _x.azimuth, _x.elevation, _x.box_height, _x.box_width,) = _get_struct_5d2q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.class_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.class_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.dobject_num, _x.probability,) = _get_struct_id().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_i3I().pack(_x.dvector_num, _x.camera_header.seq, _x.camera_header.stamp.secs, _x.camera_header.stamp.nsecs))
      _x = self.camera_header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_5d2q().pack(_x.sub_pt.x, _x.sub_pt.y, _x.sub_pt.z, _x.azimuth, _x.elevation, _x.box_height, _x.box_width))
      _x = self.class_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_id().pack(_x.dobject_num, _x.probability))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.camera_header is None:
        self.camera_header = std_msgs.msg.Header()
      if self.sub_pt is None:
        self.sub_pt = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.dvector_num, _x.camera_header.seq, _x.camera_header.stamp.secs, _x.camera_header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.camera_header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.camera_header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.sub_pt.x, _x.sub_pt.y, _x.sub_pt.z, _x.azimuth, _x.elevation, _x.box_height, _x.box_width,) = _get_struct_5d2q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.class_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.class_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.dobject_num, _x.probability,) = _get_struct_id().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_5d2q = None
def _get_struct_5d2q():
    global _struct_5d2q
    if _struct_5d2q is None:
        _struct_5d2q = struct.Struct("<5d2q")
    return _struct_5d2q
_struct_i3I = None
def _get_struct_i3I():
    global _struct_i3I
    if _struct_i3I is None:
        _struct_i3I = struct.Struct("<i3I")
    return _struct_i3I
_struct_id = None
def _get_struct_id():
    global _struct_id
    if _struct_id is None:
        _struct_id = struct.Struct("<id")
    return _struct_id