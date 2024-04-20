; Auto-generated. Do not edit!


(cl:in-package darknet_multiplexer_msgs-srv)


;//! \htmlinclude DarknetCameras-request.msg.html

(cl:defclass <DarknetCameras-request> (roslisp-msg-protocol:ros-message)
  ((actives
    :reader actives
    :initarg :actives
    :type (cl:vector cl:boolean)
   :initform (cl:make-array 0 :element-type 'cl:boolean :initial-element cl:nil)))
)

(cl:defclass DarknetCameras-request (<DarknetCameras-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DarknetCameras-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DarknetCameras-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name darknet_multiplexer_msgs-srv:<DarknetCameras-request> is deprecated: use darknet_multiplexer_msgs-srv:DarknetCameras-request instead.")))

(cl:ensure-generic-function 'actives-val :lambda-list '(m))
(cl:defmethod actives-val ((m <DarknetCameras-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_multiplexer_msgs-srv:actives-val is deprecated.  Use darknet_multiplexer_msgs-srv:actives instead.")
  (actives m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DarknetCameras-request>) ostream)
  "Serializes a message object of type '<DarknetCameras-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'actives))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if ele 1 0)) ostream))
   (cl:slot-value msg 'actives))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DarknetCameras-request>) istream)
  "Deserializes a message object of type '<DarknetCameras-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'actives) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'actives)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:not (cl:zerop (cl:read-byte istream)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DarknetCameras-request>)))
  "Returns string type for a service object of type '<DarknetCameras-request>"
  "darknet_multiplexer_msgs/DarknetCamerasRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DarknetCameras-request)))
  "Returns string type for a service object of type 'DarknetCameras-request"
  "darknet_multiplexer_msgs/DarknetCamerasRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DarknetCameras-request>)))
  "Returns md5sum for a message object of type '<DarknetCameras-request>"
  "f6d950e5bb479bad2da2554e46987675")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DarknetCameras-request)))
  "Returns md5sum for a message object of type 'DarknetCameras-request"
  "f6d950e5bb479bad2da2554e46987675")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DarknetCameras-request>)))
  "Returns full string definition for message of type '<DarknetCameras-request>"
  (cl:format cl:nil "# How to publish from cmd line: rosservice call darknet_multiplexer/configure_active_cameras \"{actives:[1,0,1,0,1,0]}\"~%# DOWNCAM_INDEX=5~%# NUMBER_CAMERAS=6~%bool[] actives~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DarknetCameras-request)))
  "Returns full string definition for message of type 'DarknetCameras-request"
  (cl:format cl:nil "# How to publish from cmd line: rosservice call darknet_multiplexer/configure_active_cameras \"{actives:[1,0,1,0,1,0]}\"~%# DOWNCAM_INDEX=5~%# NUMBER_CAMERAS=6~%bool[] actives~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DarknetCameras-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'actives) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DarknetCameras-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DarknetCameras-request
    (cl:cons ':actives (actives msg))
))
;//! \htmlinclude DarknetCameras-response.msg.html

(cl:defclass <DarknetCameras-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass DarknetCameras-response (<DarknetCameras-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DarknetCameras-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DarknetCameras-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name darknet_multiplexer_msgs-srv:<DarknetCameras-response> is deprecated: use darknet_multiplexer_msgs-srv:DarknetCameras-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <DarknetCameras-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_multiplexer_msgs-srv:success-val is deprecated.  Use darknet_multiplexer_msgs-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DarknetCameras-response>) ostream)
  "Serializes a message object of type '<DarknetCameras-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DarknetCameras-response>) istream)
  "Deserializes a message object of type '<DarknetCameras-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DarknetCameras-response>)))
  "Returns string type for a service object of type '<DarknetCameras-response>"
  "darknet_multiplexer_msgs/DarknetCamerasResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DarknetCameras-response)))
  "Returns string type for a service object of type 'DarknetCameras-response"
  "darknet_multiplexer_msgs/DarknetCamerasResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DarknetCameras-response>)))
  "Returns md5sum for a message object of type '<DarknetCameras-response>"
  "f6d950e5bb479bad2da2554e46987675")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DarknetCameras-response)))
  "Returns md5sum for a message object of type 'DarknetCameras-response"
  "f6d950e5bb479bad2da2554e46987675")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DarknetCameras-response>)))
  "Returns full string definition for message of type '<DarknetCameras-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DarknetCameras-response)))
  "Returns full string definition for message of type 'DarknetCameras-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DarknetCameras-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DarknetCameras-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DarknetCameras-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DarknetCameras)))
  'DarknetCameras-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DarknetCameras)))
  'DarknetCameras-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DarknetCameras)))
  "Returns string type for a service object of type '<DarknetCameras>"
  "darknet_multiplexer_msgs/DarknetCameras")