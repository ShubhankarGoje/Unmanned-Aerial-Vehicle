; Auto-generated. Do not edit!


(cl:in-package darknet_ros_msgs-msg)


;//! \htmlinclude BoundingBoxes.msg.html

(cl:defclass <BoundingBoxes> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (image_header
    :reader image_header
    :initarg :image_header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (bounding_boxes
    :reader bounding_boxes
    :initarg :bounding_boxes
    :type (cl:vector darknet_ros_msgs-msg:BoundingBox)
   :initform (cl:make-array 0 :element-type 'darknet_ros_msgs-msg:BoundingBox :initial-element (cl:make-instance 'darknet_ros_msgs-msg:BoundingBox)))
   (image
    :reader image
    :initarg :image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass BoundingBoxes (<BoundingBoxes>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BoundingBoxes>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BoundingBoxes)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name darknet_ros_msgs-msg:<BoundingBoxes> is deprecated: use darknet_ros_msgs-msg:BoundingBoxes instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <BoundingBoxes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:header-val is deprecated.  Use darknet_ros_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'image_header-val :lambda-list '(m))
(cl:defmethod image_header-val ((m <BoundingBoxes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:image_header-val is deprecated.  Use darknet_ros_msgs-msg:image_header instead.")
  (image_header m))

(cl:ensure-generic-function 'bounding_boxes-val :lambda-list '(m))
(cl:defmethod bounding_boxes-val ((m <BoundingBoxes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:bounding_boxes-val is deprecated.  Use darknet_ros_msgs-msg:bounding_boxes instead.")
  (bounding_boxes m))

(cl:ensure-generic-function 'image-val :lambda-list '(m))
(cl:defmethod image-val ((m <BoundingBoxes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:image-val is deprecated.  Use darknet_ros_msgs-msg:image instead.")
  (image m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BoundingBoxes>) ostream)
  "Serializes a message object of type '<BoundingBoxes>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image_header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'bounding_boxes))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'bounding_boxes))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BoundingBoxes>) istream)
  "Deserializes a message object of type '<BoundingBoxes>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image_header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'bounding_boxes) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'bounding_boxes)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'darknet_ros_msgs-msg:BoundingBox))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BoundingBoxes>)))
  "Returns string type for a message object of type '<BoundingBoxes>"
  "darknet_ros_msgs/BoundingBoxes")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BoundingBoxes)))
  "Returns string type for a message object of type 'BoundingBoxes"
  "darknet_ros_msgs/BoundingBoxes")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BoundingBoxes>)))
  "Returns md5sum for a message object of type '<BoundingBoxes>"
  "73082496dd4b884fcf28c2780a201ac5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BoundingBoxes)))
  "Returns md5sum for a message object of type 'BoundingBoxes"
  "73082496dd4b884fcf28c2780a201ac5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BoundingBoxes>)))
  "Returns full string definition for message of type '<BoundingBoxes>"
  (cl:format cl:nil "Header header~%Header image_header~%BoundingBox[] bounding_boxes~%sensor_msgs/Image image~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: darknet_ros_msgs/BoundingBox~%string Class~%float64 probability~%int64 xmin~%int64 ymin~%int64 xmax~%int64 ymax~%~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BoundingBoxes)))
  "Returns full string definition for message of type 'BoundingBoxes"
  (cl:format cl:nil "Header header~%Header image_header~%BoundingBox[] bounding_boxes~%sensor_msgs/Image image~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: darknet_ros_msgs/BoundingBox~%string Class~%float64 probability~%int64 xmin~%int64 ymin~%int64 xmax~%int64 ymax~%~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BoundingBoxes>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image_header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'bounding_boxes) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BoundingBoxes>))
  "Converts a ROS message object to a list"
  (cl:list 'BoundingBoxes
    (cl:cons ':header (header msg))
    (cl:cons ':image_header (image_header msg))
    (cl:cons ':bounding_boxes (bounding_boxes msg))
    (cl:cons ':image (image msg))
))
