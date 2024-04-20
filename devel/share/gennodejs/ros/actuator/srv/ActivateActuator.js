// Auto-generated. Do not edit!

// (in-package actuator.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ActivateActuatorRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.actuatorNumber = null;
      this.activationTime = null;
    }
    else {
      if (initObj.hasOwnProperty('actuatorNumber')) {
        this.actuatorNumber = initObj.actuatorNumber
      }
      else {
        this.actuatorNumber = 0;
      }
      if (initObj.hasOwnProperty('activationTime')) {
        this.activationTime = initObj.activationTime
      }
      else {
        this.activationTime = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ActivateActuatorRequest
    // Serialize message field [actuatorNumber]
    bufferOffset = _serializer.int8(obj.actuatorNumber, buffer, bufferOffset);
    // Serialize message field [activationTime]
    bufferOffset = _serializer.int32(obj.activationTime, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActivateActuatorRequest
    let len;
    let data = new ActivateActuatorRequest(null);
    // Deserialize message field [actuatorNumber]
    data.actuatorNumber = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [activationTime]
    data.activationTime = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'actuator/ActivateActuatorRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ae4e2550a20f18efb89cde3cf018b8b4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 actuatorNumber
    int32 activationTime
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ActivateActuatorRequest(null);
    if (msg.actuatorNumber !== undefined) {
      resolved.actuatorNumber = msg.actuatorNumber;
    }
    else {
      resolved.actuatorNumber = 0
    }

    if (msg.activationTime !== undefined) {
      resolved.activationTime = msg.activationTime;
    }
    else {
      resolved.activationTime = 0
    }

    return resolved;
    }
};

class ActivateActuatorResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ActivateActuatorResponse
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActivateActuatorResponse
    let len;
    let data = new ActivateActuatorResponse(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'actuator/ActivateActuatorResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ActivateActuatorResponse(null);
    return resolved;
    }
};

module.exports = {
  Request: ActivateActuatorRequest,
  Response: ActivateActuatorResponse,
  md5sum() { return 'ae4e2550a20f18efb89cde3cf018b8b4'; },
  datatype() { return 'actuator/ActivateActuator'; }
};
