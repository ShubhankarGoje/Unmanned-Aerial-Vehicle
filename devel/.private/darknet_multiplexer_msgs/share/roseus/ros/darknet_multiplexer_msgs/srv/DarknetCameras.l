;; Auto-generated. Do not edit!


(when (boundp 'darknet_multiplexer_msgs::DarknetCameras)
  (if (not (find-package "DARKNET_MULTIPLEXER_MSGS"))
    (make-package "DARKNET_MULTIPLEXER_MSGS"))
  (shadow 'DarknetCameras (find-package "DARKNET_MULTIPLEXER_MSGS")))
(unless (find-package "DARKNET_MULTIPLEXER_MSGS::DARKNETCAMERAS")
  (make-package "DARKNET_MULTIPLEXER_MSGS::DARKNETCAMERAS"))
(unless (find-package "DARKNET_MULTIPLEXER_MSGS::DARKNETCAMERASREQUEST")
  (make-package "DARKNET_MULTIPLEXER_MSGS::DARKNETCAMERASREQUEST"))
(unless (find-package "DARKNET_MULTIPLEXER_MSGS::DARKNETCAMERASRESPONSE")
  (make-package "DARKNET_MULTIPLEXER_MSGS::DARKNETCAMERASRESPONSE"))

(in-package "ROS")





(defclass darknet_multiplexer_msgs::DarknetCamerasRequest
  :super ros::object
  :slots (_actives ))

(defmethod darknet_multiplexer_msgs::DarknetCamerasRequest
  (:init
   (&key
    ((:actives __actives) (let (r) (dotimes (i 0) (push nil r)) r))
    )
   (send-super :init)
   (setq _actives __actives)
   self)
  (:actives
   (&optional __actives)
   (if __actives (setq _actives __actives)) _actives)
  (:serialization-length
   ()
   (+
    ;; bool[] _actives
    (* 1    (length _actives)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool[] _actives
     (write-long (length _actives) s)
     (dotimes (i (length _actives))
       (if (elt _actives i) (write-byte -1 s) (write-byte 0 s))
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool[] _actives
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _actives (make-list n))
     (dotimes (i n)
     (setf (elt _actives i) (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
     ))
   ;;
   self)
  )

(defclass darknet_multiplexer_msgs::DarknetCamerasResponse
  :super ros::object
  :slots (_success ))

(defmethod darknet_multiplexer_msgs::DarknetCamerasResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass darknet_multiplexer_msgs::DarknetCameras
  :super ros::object
  :slots ())

(setf (get darknet_multiplexer_msgs::DarknetCameras :md5sum-) "f6d950e5bb479bad2da2554e46987675")
(setf (get darknet_multiplexer_msgs::DarknetCameras :datatype-) "darknet_multiplexer_msgs/DarknetCameras")
(setf (get darknet_multiplexer_msgs::DarknetCameras :request) darknet_multiplexer_msgs::DarknetCamerasRequest)
(setf (get darknet_multiplexer_msgs::DarknetCameras :response) darknet_multiplexer_msgs::DarknetCamerasResponse)

(defmethod darknet_multiplexer_msgs::DarknetCamerasRequest
  (:response () (instance darknet_multiplexer_msgs::DarknetCamerasResponse :init)))

(setf (get darknet_multiplexer_msgs::DarknetCamerasRequest :md5sum-) "f6d950e5bb479bad2da2554e46987675")
(setf (get darknet_multiplexer_msgs::DarknetCamerasRequest :datatype-) "darknet_multiplexer_msgs/DarknetCamerasRequest")
(setf (get darknet_multiplexer_msgs::DarknetCamerasRequest :definition-)
      "# How to publish from cmd line: rosservice call darknet_multiplexer/configure_active_cameras \"{actives:[1,0,1,0,1,0]}\"
# DOWNCAM_INDEX=5
# NUMBER_CAMERAS=6
bool[] actives
---
bool success
")

(setf (get darknet_multiplexer_msgs::DarknetCamerasResponse :md5sum-) "f6d950e5bb479bad2da2554e46987675")
(setf (get darknet_multiplexer_msgs::DarknetCamerasResponse :datatype-) "darknet_multiplexer_msgs/DarknetCamerasResponse")
(setf (get darknet_multiplexer_msgs::DarknetCamerasResponse :definition-)
      "# How to publish from cmd line: rosservice call darknet_multiplexer/configure_active_cameras \"{actives:[1,0,1,0,1,0]}\"
# DOWNCAM_INDEX=5
# NUMBER_CAMERAS=6
bool[] actives
---
bool success
")



(provide :darknet_multiplexer_msgs/DarknetCameras "f6d950e5bb479bad2da2554e46987675")


