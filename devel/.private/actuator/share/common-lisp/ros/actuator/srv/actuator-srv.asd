
(cl:in-package :asdf)

(defsystem "actuator-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ActivateActuator" :depends-on ("_package_ActivateActuator"))
    (:file "_package_ActivateActuator" :depends-on ("_package"))
  ))