// Auto-generated. Do not edit!

// (in-package darknet_multiplexer_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class DarknetCamerasRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.actives = null;
    }
    else {
      if (initObj.hasOwnProperty('actives')) {
        this.actives = initObj.actives
      }
      else {
        this.actives = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DarknetCamerasRequest
    // Serialize message field [actives]
    bufferOffset = _arraySerializer.bool(obj.actives, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DarknetCamerasRequest
    let len;
    let data = new DarknetCamerasRequest(null);
    // Deserialize message field [actives]
    data.actives = _arrayDeserializer.bool(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.actives.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'darknet_multiplexer_msgs/DarknetCamerasRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '08e5da29f61cb9a8287af04c34f32436';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # How to publish from cmd line: rosservice call darknet_multiplexer/configure_active_cameras "{actives:[1,0,1,0,1,0]}"
    # DOWNCAM_INDEX=5
    # NUMBER_CAMERAS=6
    bool[] actives
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DarknetCamerasRequest(null);
    if (msg.actives !== undefined) {
      resolved.actives = msg.actives;
    }
    else {
      resolved.actives = []
    }

    return resolved;
    }
};

class DarknetCamerasResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DarknetCamerasResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DarknetCamerasResponse
    let len;
    let data = new DarknetCamerasResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'darknet_multiplexer_msgs/DarknetCamerasResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '358e233cde0c8a8bcfea4ce193f8fc15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DarknetCamerasResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: DarknetCamerasRequest,
  Response: DarknetCamerasResponse,
  md5sum() { return 'f6d950e5bb479bad2da2554e46987675'; },
  datatype() { return 'darknet_multiplexer_msgs/DarknetCameras'; }
};
