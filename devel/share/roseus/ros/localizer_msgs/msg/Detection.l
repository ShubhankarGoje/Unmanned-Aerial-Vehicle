;; Auto-generated. Do not edit!


(when (boundp 'localizer_msgs::Detection)
  (if (not (find-package "LOCALIZER_MSGS"))
    (make-package "LOCALIZER_MSGS"))
  (shadow 'Detection (find-package "LOCALIZER_MSGS")))
(unless (find-package "LOCALIZER_MSGS::DETECTION")
  (make-package "LOCALIZER_MSGS::DETECTION"))

(in-package "ROS")
;;//! \htmlinclude Detection.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass localizer_msgs::Detection
  :super ros::object
  :slots (_class_id _pose ))

(defmethod localizer_msgs::Detection
  (:init
   (&key
    ((:class_id __class_id) "")
    ((:pose __pose) (instance geometry_msgs::PoseStamped :init))
    )
   (send-super :init)
   (setq _class_id (string __class_id))
   (setq _pose __pose)
   self)
  (:class_id
   (&optional __class_id)
   (if __class_id (setq _class_id __class_id)) _class_id)
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:serialization-length
   ()
   (+
    ;; string _class_id
    4 (length _class_id)
    ;; geometry_msgs/PoseStamped _pose
    (send _pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _class_id
       (write-long (length _class_id) s) (princ _class_id s)
     ;; geometry_msgs/PoseStamped _pose
       (send _pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _class_id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _class_id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/PoseStamped _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;;
   self)
  )

(setf (get localizer_msgs::Detection :md5sum-) "1ab6ad1647bd08390b58954f48ea7686")
(setf (get localizer_msgs::Detection :datatype-) "localizer_msgs/Detection")
(setf (get localizer_msgs::Detection :definition-)
      "string class_id
geometry_msgs/PoseStamped pose

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

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
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :localizer_msgs/Detection "1ab6ad1647bd08390b58954f48ea7686")


