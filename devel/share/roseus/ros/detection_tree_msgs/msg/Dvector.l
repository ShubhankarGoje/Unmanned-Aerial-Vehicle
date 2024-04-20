;; Auto-generated. Do not edit!


(when (boundp 'detection_tree_msgs::Dvector)
  (if (not (find-package "DETECTION_TREE_MSGS"))
    (make-package "DETECTION_TREE_MSGS"))
  (shadow 'Dvector (find-package "DETECTION_TREE_MSGS")))
(unless (find-package "DETECTION_TREE_MSGS::DVECTOR")
  (make-package "DETECTION_TREE_MSGS::DVECTOR"))

(in-package "ROS")
;;//! \htmlinclude Dvector.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass detection_tree_msgs::Dvector
  :super ros::object
  :slots (_dvector_num _camera_header _sub_pt _azimuth _elevation _box_height _box_width _class_id _dobject_num _probability ))

(defmethod detection_tree_msgs::Dvector
  (:init
   (&key
    ((:dvector_num __dvector_num) 0)
    ((:camera_header __camera_header) (instance std_msgs::Header :init))
    ((:sub_pt __sub_pt) (instance geometry_msgs::Point :init))
    ((:azimuth __azimuth) 0.0)
    ((:elevation __elevation) 0.0)
    ((:box_height __box_height) 0)
    ((:box_width __box_width) 0)
    ((:class_id __class_id) "")
    ((:dobject_num __dobject_num) 0)
    ((:probability __probability) 0.0)
    )
   (send-super :init)
   (setq _dvector_num (round __dvector_num))
   (setq _camera_header __camera_header)
   (setq _sub_pt __sub_pt)
   (setq _azimuth (float __azimuth))
   (setq _elevation (float __elevation))
   (setq _box_height (round __box_height))
   (setq _box_width (round __box_width))
   (setq _class_id (string __class_id))
   (setq _dobject_num (round __dobject_num))
   (setq _probability (float __probability))
   self)
  (:dvector_num
   (&optional __dvector_num)
   (if __dvector_num (setq _dvector_num __dvector_num)) _dvector_num)
  (:camera_header
   (&rest __camera_header)
   (if (keywordp (car __camera_header))
       (send* _camera_header __camera_header)
     (progn
       (if __camera_header (setq _camera_header (car __camera_header)))
       _camera_header)))
  (:sub_pt
   (&rest __sub_pt)
   (if (keywordp (car __sub_pt))
       (send* _sub_pt __sub_pt)
     (progn
       (if __sub_pt (setq _sub_pt (car __sub_pt)))
       _sub_pt)))
  (:azimuth
   (&optional __azimuth)
   (if __azimuth (setq _azimuth __azimuth)) _azimuth)
  (:elevation
   (&optional __elevation)
   (if __elevation (setq _elevation __elevation)) _elevation)
  (:box_height
   (&optional __box_height)
   (if __box_height (setq _box_height __box_height)) _box_height)
  (:box_width
   (&optional __box_width)
   (if __box_width (setq _box_width __box_width)) _box_width)
  (:class_id
   (&optional __class_id)
   (if __class_id (setq _class_id __class_id)) _class_id)
  (:dobject_num
   (&optional __dobject_num)
   (if __dobject_num (setq _dobject_num __dobject_num)) _dobject_num)
  (:probability
   (&optional __probability)
   (if __probability (setq _probability __probability)) _probability)
  (:serialization-length
   ()
   (+
    ;; int32 _dvector_num
    4
    ;; std_msgs/Header _camera_header
    (send _camera_header :serialization-length)
    ;; geometry_msgs/Point _sub_pt
    (send _sub_pt :serialization-length)
    ;; float64 _azimuth
    8
    ;; float64 _elevation
    8
    ;; int64 _box_height
    8
    ;; int64 _box_width
    8
    ;; string _class_id
    4 (length _class_id)
    ;; int32 _dobject_num
    4
    ;; float64 _probability
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _dvector_num
       (write-long _dvector_num s)
     ;; std_msgs/Header _camera_header
       (send _camera_header :serialize s)
     ;; geometry_msgs/Point _sub_pt
       (send _sub_pt :serialize s)
     ;; float64 _azimuth
       (sys::poke _azimuth (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _elevation
       (sys::poke _elevation (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int64 _box_height
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _box_height (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _box_height) (= (length (_box_height . bv)) 2)) ;; bignum
              (write-long (ash (elt (_box_height . bv) 0) 0) s)
              (write-long (ash (elt (_box_height . bv) 1) -1) s))
             ((and (class _box_height) (= (length (_box_height . bv)) 1)) ;; big1
              (write-long (elt (_box_height . bv) 0) s)
              (write-long (if (>= _box_height 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _box_height s)(write-long (if (>= _box_height 0) 0 #xffffffff) s)))
     ;; int64 _box_width
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _box_width (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _box_width) (= (length (_box_width . bv)) 2)) ;; bignum
              (write-long (ash (elt (_box_width . bv) 0) 0) s)
              (write-long (ash (elt (_box_width . bv) 1) -1) s))
             ((and (class _box_width) (= (length (_box_width . bv)) 1)) ;; big1
              (write-long (elt (_box_width . bv) 0) s)
              (write-long (if (>= _box_width 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _box_width s)(write-long (if (>= _box_width 0) 0 #xffffffff) s)))
     ;; string _class_id
       (write-long (length _class_id) s) (princ _class_id s)
     ;; int32 _dobject_num
       (write-long _dobject_num s)
     ;; float64 _probability
       (sys::poke _probability (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _dvector_num
     (setq _dvector_num (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; std_msgs/Header _camera_header
     (send _camera_header :deserialize buf ptr-) (incf ptr- (send _camera_header :serialization-length))
   ;; geometry_msgs/Point _sub_pt
     (send _sub_pt :deserialize buf ptr-) (incf ptr- (send _sub_pt :serialization-length))
   ;; float64 _azimuth
     (setq _azimuth (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _elevation
     (setq _elevation (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int64 _box_height
#+(or :alpha :irix6 :x86_64)
      (setf _box_height (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _box_height (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _box_width
#+(or :alpha :irix6 :x86_64)
      (setf _box_width (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _box_width (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; string _class_id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _class_id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _dobject_num
     (setq _dobject_num (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _probability
     (setq _probability (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get detection_tree_msgs::Dvector :md5sum-) "ac5b92b151d663eccd740b80612c355c")
(setf (get detection_tree_msgs::Dvector :datatype-) "detection_tree_msgs/Dvector")
(setf (get detection_tree_msgs::Dvector :definition-)
      "int32 dvector_num
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

")



(provide :detection_tree_msgs/Dvector "ac5b92b151d663eccd740b80612c355c")


