;; Auto-generated. Do not edit!


(when (boundp 'actuator::ActivateActuator)
  (if (not (find-package "ACTUATOR"))
    (make-package "ACTUATOR"))
  (shadow 'ActivateActuator (find-package "ACTUATOR")))
(unless (find-package "ACTUATOR::ACTIVATEACTUATOR")
  (make-package "ACTUATOR::ACTIVATEACTUATOR"))
(unless (find-package "ACTUATOR::ACTIVATEACTUATORREQUEST")
  (make-package "ACTUATOR::ACTIVATEACTUATORREQUEST"))
(unless (find-package "ACTUATOR::ACTIVATEACTUATORRESPONSE")
  (make-package "ACTUATOR::ACTIVATEACTUATORRESPONSE"))

(in-package "ROS")





(defclass actuator::ActivateActuatorRequest
  :super ros::object
  :slots (_actuatorNumber _activationTime ))

(defmethod actuator::ActivateActuatorRequest
  (:init
   (&key
    ((:actuatorNumber __actuatorNumber) 0)
    ((:activationTime __activationTime) 0)
    )
   (send-super :init)
   (setq _actuatorNumber (round __actuatorNumber))
   (setq _activationTime (round __activationTime))
   self)
  (:actuatorNumber
   (&optional __actuatorNumber)
   (if __actuatorNumber (setq _actuatorNumber __actuatorNumber)) _actuatorNumber)
  (:activationTime
   (&optional __activationTime)
   (if __activationTime (setq _activationTime __activationTime)) _activationTime)
  (:serialization-length
   ()
   (+
    ;; int8 _actuatorNumber
    1
    ;; int32 _activationTime
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _actuatorNumber
       (write-byte _actuatorNumber s)
     ;; int32 _activationTime
       (write-long _activationTime s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _actuatorNumber
     (setq _actuatorNumber (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _actuatorNumber 127) (setq _actuatorNumber (- _actuatorNumber 256)))
   ;; int32 _activationTime
     (setq _activationTime (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass actuator::ActivateActuatorResponse
  :super ros::object
  :slots ())

(defmethod actuator::ActivateActuatorResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass actuator::ActivateActuator
  :super ros::object
  :slots ())

(setf (get actuator::ActivateActuator :md5sum-) "ae4e2550a20f18efb89cde3cf018b8b4")
(setf (get actuator::ActivateActuator :datatype-) "actuator/ActivateActuator")
(setf (get actuator::ActivateActuator :request) actuator::ActivateActuatorRequest)
(setf (get actuator::ActivateActuator :response) actuator::ActivateActuatorResponse)

(defmethod actuator::ActivateActuatorRequest
  (:response () (instance actuator::ActivateActuatorResponse :init)))

(setf (get actuator::ActivateActuatorRequest :md5sum-) "ae4e2550a20f18efb89cde3cf018b8b4")
(setf (get actuator::ActivateActuatorRequest :datatype-) "actuator/ActivateActuatorRequest")
(setf (get actuator::ActivateActuatorRequest :definition-)
      "int8 actuatorNumber
int32 activationTime

---
")

(setf (get actuator::ActivateActuatorResponse :md5sum-) "ae4e2550a20f18efb89cde3cf018b8b4")
(setf (get actuator::ActivateActuatorResponse :datatype-) "actuator/ActivateActuatorResponse")
(setf (get actuator::ActivateActuatorResponse :definition-)
      "int8 actuatorNumber
int32 activationTime

---
")



(provide :actuator/ActivateActuator "ae4e2550a20f18efb89cde3cf018b8b4")


