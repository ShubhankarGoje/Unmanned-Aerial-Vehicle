# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from darknet_ros_msgs/CheckForObjectsResult.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import darknet_ros_msgs.msg
import sensor_msgs.msg
import std_msgs.msg

class CheckForObjectsResult(genpy.Message):
  _md5sum = "8286a88b6c1e84d9074f00e82352f581"
  _type = "darknet_ros_msgs/CheckForObjectsResult"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Result definition
int16 id
darknet_ros_msgs/BoundingBoxes bounding_boxes


================================================================================
MSG: darknet_ros_msgs/BoundingBoxes
Header header
Header image_header
BoundingBox[] bounding_boxes
sensor_msgs/Image image

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
MSG: darknet_ros_msgs/BoundingBox
string Class
float64 probability
int64 xmin
int64 ymin
int64 xmax
int64 ymax


================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
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
"""
  __slots__ = ['id','bounding_boxes']
  _slot_types = ['int16','darknet_ros_msgs/BoundingBoxes']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,bounding_boxes

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CheckForObjectsResult, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.bounding_boxes is None:
        self.bounding_boxes = darknet_ros_msgs.msg.BoundingBoxes()
    else:
      self.id = 0
      self.bounding_boxes = darknet_ros_msgs.msg.BoundingBoxes()

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
      buff.write(_get_struct_h3I().pack(_x.id, _x.bounding_boxes.header.seq, _x.bounding_boxes.header.stamp.secs, _x.bounding_boxes.header.stamp.nsecs))
      _x = self.bounding_boxes.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.bounding_boxes.image_header.seq, _x.bounding_boxes.image_header.stamp.secs, _x.bounding_boxes.image_header.stamp.nsecs))
      _x = self.bounding_boxes.image_header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.bounding_boxes.bounding_boxes)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_boxes.bounding_boxes:
        _x = val1.Class
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_d4q().pack(_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax))
      _x = self
      buff.write(_get_struct_3I().pack(_x.bounding_boxes.image.header.seq, _x.bounding_boxes.image.header.stamp.secs, _x.bounding_boxes.image.header.stamp.nsecs))
      _x = self.bounding_boxes.image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.bounding_boxes.image.height, _x.bounding_boxes.image.width))
      _x = self.bounding_boxes.image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.bounding_boxes.image.is_bigendian, _x.bounding_boxes.image.step))
      _x = self.bounding_boxes.image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.bounding_boxes is None:
        self.bounding_boxes = darknet_ros_msgs.msg.BoundingBoxes()
      end = 0
      _x = self
      start = end
      end += 14
      (_x.id, _x.bounding_boxes.header.seq, _x.bounding_boxes.header.stamp.secs, _x.bounding_boxes.header.stamp.nsecs,) = _get_struct_h3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bounding_boxes.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.bounding_boxes.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.bounding_boxes.image_header.seq, _x.bounding_boxes.image_header.stamp.secs, _x.bounding_boxes.image_header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bounding_boxes.image_header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.bounding_boxes.image_header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_boxes.bounding_boxes = []
      for i in range(0, length):
        val1 = darknet_ros_msgs.msg.BoundingBox()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.Class = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.Class = str[start:end]
        _x = val1
        start = end
        end += 40
        (_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax,) = _get_struct_d4q().unpack(str[start:end])
        self.bounding_boxes.bounding_boxes.append(val1)
      _x = self
      start = end
      end += 12
      (_x.bounding_boxes.image.header.seq, _x.bounding_boxes.image.header.stamp.secs, _x.bounding_boxes.image.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bounding_boxes.image.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.bounding_boxes.image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.bounding_boxes.image.height, _x.bounding_boxes.image.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bounding_boxes.image.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.bounding_boxes.image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.bounding_boxes.image.is_bigendian, _x.bounding_boxes.image.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.bounding_boxes.image.data = str[start:end]
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
      buff.write(_get_struct_h3I().pack(_x.id, _x.bounding_boxes.header.seq, _x.bounding_boxes.header.stamp.secs, _x.bounding_boxes.header.stamp.nsecs))
      _x = self.bounding_boxes.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.bounding_boxes.image_header.seq, _x.bounding_boxes.image_header.stamp.secs, _x.bounding_boxes.image_header.stamp.nsecs))
      _x = self.bounding_boxes.image_header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.bounding_boxes.bounding_boxes)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_boxes.bounding_boxes:
        _x = val1.Class
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_d4q().pack(_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax))
      _x = self
      buff.write(_get_struct_3I().pack(_x.bounding_boxes.image.header.seq, _x.bounding_boxes.image.header.stamp.secs, _x.bounding_boxes.image.header.stamp.nsecs))
      _x = self.bounding_boxes.image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.bounding_boxes.image.height, _x.bounding_boxes.image.width))
      _x = self.bounding_boxes.image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.bounding_boxes.image.is_bigendian, _x.bounding_boxes.image.step))
      _x = self.bounding_boxes.image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
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
      if self.bounding_boxes is None:
        self.bounding_boxes = darknet_ros_msgs.msg.BoundingBoxes()
      end = 0
      _x = self
      start = end
      end += 14
      (_x.id, _x.bounding_boxes.header.seq, _x.bounding_boxes.header.stamp.secs, _x.bounding_boxes.header.stamp.nsecs,) = _get_struct_h3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bounding_boxes.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.bounding_boxes.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.bounding_boxes.image_header.seq, _x.bounding_boxes.image_header.stamp.secs, _x.bounding_boxes.image_header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bounding_boxes.image_header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.bounding_boxes.image_header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_boxes.bounding_boxes = []
      for i in range(0, length):
        val1 = darknet_ros_msgs.msg.BoundingBox()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.Class = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.Class = str[start:end]
        _x = val1
        start = end
        end += 40
        (_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax,) = _get_struct_d4q().unpack(str[start:end])
        self.bounding_boxes.bounding_boxes.append(val1)
      _x = self
      start = end
      end += 12
      (_x.bounding_boxes.image.header.seq, _x.bounding_boxes.image.header.stamp.secs, _x.bounding_boxes.image.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bounding_boxes.image.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.bounding_boxes.image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.bounding_boxes.image.height, _x.bounding_boxes.image.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bounding_boxes.image.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.bounding_boxes.image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.bounding_boxes.image.is_bigendian, _x.bounding_boxes.image.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.bounding_boxes.image.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_BI = None
def _get_struct_BI():
    global _struct_BI
    if _struct_BI is None:
        _struct_BI = struct.Struct("<BI")
    return _struct_BI
_struct_d4q = None
def _get_struct_d4q():
    global _struct_d4q
    if _struct_d4q is None:
        _struct_d4q = struct.Struct("<d4q")
    return _struct_d4q
_struct_h3I = None
def _get_struct_h3I():
    global _struct_h3I
    if _struct_h3I is None:
        _struct_h3I = struct.Struct("<h3I")
    return _struct_h3I
