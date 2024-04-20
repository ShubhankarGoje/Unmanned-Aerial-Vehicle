; Auto-generated. Do not edit!


(cl:in-package actuator-srv)


;//! \htmlinclude ActivateActuator-request.msg.html

(cl:defclass <ActivateActuator-request> (roslisp-msg-protocol:ros-message)
  ((actuatorNumber
    :reader actuatorNumber
    :initarg :actuatorNumber
    :type cl:fixnum
    :initform 0)
   (activationTime
    :reader activationTime
    :initarg :activationTime
    :type cl:integer
    :initform 0))
)

(cl:defclass ActivateActuator-request (<ActivateActuator-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActivateActuator-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActivateActuator-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name actuator-srv:<ActivateActuator-request> is deprecated: use actuator-srv:ActivateActuator-request instead.")))

(cl:ensure-generic-function 'actuatorNumber-val :lambda-list '(m))
(cl:defmethod actuatorNumber-val ((m <ActivateActuator-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader actuator-srv:actuatorNumber-val is deprecated.  Use actuator-srv:actuatorNumber instead.")
  (actuatorNumber m))

(cl:ensure-generic-function 'activationTime-val :lambda-list '(m))
(cl:defmethod activationTime-val ((m <ActivateActuator-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader actuator-srv:activationTime-val is deprecated.  Use actuator-srv:activationTime instead.")
  (activationTime m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActivateActuator-request>) ostream)
  "Serializes a message object of type '<ActivateActuator-request>"
  (cl:let* ((signed (cl:slot-value msg 'actuatorNumber)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'activationTime)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActivateActuator-request>) istream)
  "Deserializes a message object of type '<ActivateActuator-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'actuatorNumber) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'activationTime) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActivateActuator-request>)))
  "Returns string type for a service object of type '<ActivateActuator-request>"
  "actuator/ActivateActuatorRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActivateActuator-request)))
  "Returns string type for a service object of type 'ActivateActuator-request"
  "actuator/ActivateActuatorRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActivateActuator-request>)))
  "Returns md5sum for a message object of type '<ActivateActuator-request>"
  "ae4e2550a20f18efb89cde3cf018b8b4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActivateActuator-request)))
  "Returns md5sum for a message object of type 'ActivateActuator-request"
  "ae4e2550a20f18efb89cde3cf018b8b4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActivateActuator-request>)))
  "Returns full string definition for message of type '<ActivateActuator-request>"
  (cl:format cl:nil "int8 actuatorNumber~%int32 activationTime~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActivateActuator-request)))
  "Returns full string definition for message of type 'ActivateActuator-request"
  (cl:format cl:nil "int8 actuatorNumber~%int32 activationTime~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActivateActuator-request>))
  (cl:+ 0
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActivateActuator-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ActivateActuator-request
    (cl:cons ':actuatorNumber (actuatorNumber msg))
    (cl:cons ':activationTime (activationTime msg))
))
;//! \htmlinclude ActivateActuator-response.msg.html

(cl:defclass <ActivateActuator-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ActivateActuator-response (<ActivateActuator-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActivateActuator-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActivateActuator-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name actuator-srv:<ActivateActuator-response> is deprecated: use actuator-srv:ActivateActuator-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActivateActuator-response>) ostream)
  "Serializes a message object of type '<ActivateActuator-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActivateActuator-response>) istream)
  "Deserializes a message object of type '<ActivateActuator-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActivateActuator-response>)))
  "Returns string type for a service object of type '<ActivateActuator-response>"
  "actuator/ActivateActuatorResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActivateActuator-response)))
  "Returns string type for a service object of type 'ActivateActuator-response"
  "actuator/ActivateActuatorResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActivateActuator-response>)))
  "Returns md5sum for a message object of type '<ActivateActuator-response>"
  "ae4e2550a20f18efb89cde3cf018b8b4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActivateActuator-response)))
  "Returns md5sum for a message object of type 'ActivateActuator-response"
  "ae4e2550a20f18efb89cde3cf018b8b4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActivateActuator-response>)))
  "Returns full string definition for message of type '<ActivateActuator-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActivateActuator-response)))
  "Returns full string definition for message of type 'ActivateActuator-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActivateActuator-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActivateActuator-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ActivateActuator-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ActivateActuator)))
  'ActivateActuator-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ActivateActuator)))
  'ActivateActuator-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActivateActuator)))
  "Returns string type for a service object of type '<ActivateActuator>"
  "actuator/ActivateActuator")