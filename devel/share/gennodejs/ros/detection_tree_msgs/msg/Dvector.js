// Auto-generated. Do not edit!

// (in-package detection_tree_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Dvector {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.dvector_num = null;
      this.camera_header = null;
      this.sub_pt = null;
      this.azimuth = null;
      this.elevation = null;
      this.box_height = null;
      this.box_width = null;
      this.class_id = null;
      this.dobject_num = null;
      this.probability = null;
    }
    else {
      if (initObj.hasOwnProperty('dvector_num')) {
        this.dvector_num = initObj.dvector_num
      }
      else {
        this.dvector_num = 0;
      }
      if (initObj.hasOwnProperty('camera_header')) {
        this.camera_header = initObj.camera_header
      }
      else {
        this.camera_header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('sub_pt')) {
        this.sub_pt = initObj.sub_pt
      }
      else {
        this.sub_pt = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('azimuth')) {
        this.azimuth = initObj.azimuth
      }
      else {
        this.azimuth = 0.0;
      }
      if (initObj.hasOwnProperty('elevation')) {
        this.elevation = initObj.elevation
      }
      else {
        this.elevation = 0.0;
      }
      if (initObj.hasOwnProperty('box_height')) {
        this.box_height = initObj.box_height
      }
      else {
        this.box_height = 0;
      }
      if (initObj.hasOwnProperty('box_width')) {
        this.box_width = initObj.box_width
      }
      else {
        this.box_width = 0;
      }
      if (initObj.hasOwnProperty('class_id')) {
        this.class_id = initObj.class_id
      }
      else {
        this.class_id = '';
      }
      if (initObj.hasOwnProperty('dobject_num')) {
        this.dobject_num = initObj.dobject_num
      }
      else {
        this.dobject_num = 0;
      }
      if (initObj.hasOwnProperty('probability')) {
        this.probability = initObj.probability
      }
      else {
        this.probability = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Dvector
    // Serialize message field [dvector_num]
    bufferOffset = _serializer.int32(obj.dvector_num, buffer, bufferOffset);
    // Serialize message field [camera_header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.camera_header, buffer, bufferOffset);
    // Serialize message field [sub_pt]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.sub_pt, buffer, bufferOffset);
    // Serialize message field [azimuth]
    bufferOffset = _serializer.float64(obj.azimuth, buffer, bufferOffset);
    // Serialize message field [elevation]
    bufferOffset = _serializer.float64(obj.elevation, buffer, bufferOffset);
    // Serialize message field [box_height]
    bufferOffset = _serializer.int64(obj.box_height, buffer, bufferOffset);
    // Serialize message field [box_width]
    bufferOffset = _serializer.int64(obj.box_width, buffer, bufferOffset);
    // Serialize message field [class_id]
    bufferOffset = _serializer.string(obj.class_id, buffer, bufferOffset);
    // Serialize message field [dobject_num]
    bufferOffset = _serializer.int32(obj.dobject_num, buffer, bufferOffset);
    // Serialize message field [probability]
    bufferOffset = _serializer.float64(obj.probability, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Dvector
    let len;
    let data = new Dvector(null);
    // Deserialize message field [dvector_num]
    data.dvector_num = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [camera_header]
    data.camera_header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [sub_pt]
    data.sub_pt = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [azimuth]
    data.azimuth = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [elevation]
    data.elevation = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [box_height]
    data.box_height = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [box_width]
    data.box_width = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [class_id]
    data.class_id = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [dobject_num]
    data.dobject_num = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [probability]
    data.probability = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.camera_header);
    length += object.class_id.length;
    return length + 76;
  }

  static datatype() {
    // Returns string type for a message object
    return 'detection_tree_msgs/Dvector';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ac5b92b151d663eccd740b80612c355c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 dvector_num
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Dvector(null);
    if (msg.dvector_num !== undefined) {
      resolved.dvector_num = msg.dvector_num;
    }
    else {
      resolved.dvector_num = 0
    }

    if (msg.camera_header !== undefined) {
      resolved.camera_header = std_msgs.msg.Header.Resolve(msg.camera_header)
    }
    else {
      resolved.camera_header = new std_msgs.msg.Header()
    }

    if (msg.sub_pt !== undefined) {
      resolved.sub_pt = geometry_msgs.msg.Point.Resolve(msg.sub_pt)
    }
    else {
      resolved.sub_pt = new geometry_msgs.msg.Point()
    }

    if (msg.azimuth !== undefined) {
      resolved.azimuth = msg.azimuth;
    }
    else {
      resolved.azimuth = 0.0
    }

    if (msg.elevation !== undefined) {
      resolved.elevation = msg.elevation;
    }
    else {
      resolved.elevation = 0.0
    }

    if (msg.box_height !== undefined) {
      resolved.box_height = msg.box_height;
    }
    else {
      resolved.box_height = 0
    }

    if (msg.box_width !== undefined) {
      resolved.box_width = msg.box_width;
    }
    else {
      resolved.box_width = 0
    }

    if (msg.class_id !== undefined) {
      resolved.class_id = msg.class_id;
    }
    else {
      resolved.class_id = ''
    }

    if (msg.dobject_num !== undefined) {
      resolved.dobject_num = msg.dobject_num;
    }
    else {
      resolved.dobject_num = 0
    }

    if (msg.probability !== undefined) {
      resolved.probability = msg.probability;
    }
    else {
      resolved.probability = 0.0
    }

    return resolved;
    }
};

module.exports = Dvector;
