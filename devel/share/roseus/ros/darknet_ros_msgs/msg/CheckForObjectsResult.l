;; Auto-generated. Do not edit!


(when (boundp 'darknet_ros_msgs::CheckForObjectsResult)
  (if (not (find-package "DARKNET_ROS_MSGS"))
    (make-package "DARKNET_ROS_MSGS"))
  (shadow 'CheckForObjectsResult (find-package "DARKNET_ROS_MSGS")))
(unless (find-package "DARKNET_ROS_MSGS::CHECKFOROBJECTSRESULT")
  (make-package "DARKNET_ROS_MSGS::CHECKFOROBJECTSRESULT"))

(in-package "ROS")
;;//! \htmlinclude CheckForObjectsResult.msg.html


(defclass darknet_ros_msgs::CheckForObjectsResult
  :super ros::object
  :slots (_id _bounding_boxes ))

(defmethod darknet_ros_msgs::CheckForObjectsResult
  (:init
   (&key
    ((:id __id) 0)
    ((:bounding_boxes __bounding_boxes) (instance darknet_ros_msgs::BoundingBoxes :init))
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _bounding_boxes __bounding_boxes)
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:bounding_boxes
   (&rest __bounding_boxes)
   (if (keywordp (car __bounding_boxes))
       (send* _bounding_boxes __bounding_boxes)
     (progn
       (if __bounding_boxes (setq _bounding_boxes (car __bounding_boxes)))
       _bounding_boxes)))
  (:serialization-length
   ()
   (+
    ;; int16 _id
    2
    ;; darknet_ros_msgs/BoundingBoxes _bounding_boxes
    (send _bounding_boxes :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _id
       (write-word _id s)
     ;; darknet_ros_msgs/BoundingBoxes _bounding_boxes
       (send _bounding_boxes :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _id
     (setq _id (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; darknet_ros_msgs/BoundingBoxes _bounding_boxes
     (send _bounding_boxes :deserialize buf ptr-) (incf ptr- (send _bounding_boxes :serialization-length))
   ;;
   self)
  )

(setf (get darknet_ros_msgs::CheckForObjectsResult :md5sum-) "8286a88b6c1e84d9074f00e82352f581")
(setf (get darknet_ros_msgs::CheckForObjectsResult :datatype-) "darknet_ros_msgs/CheckForObjectsResult")
(setf (get darknet_ros_msgs::CheckForObjectsResult :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
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

")



(provide :darknet_ros_msgs/CheckForObjectsResult "8286a88b6c1e84d9074f00e82352f581")

