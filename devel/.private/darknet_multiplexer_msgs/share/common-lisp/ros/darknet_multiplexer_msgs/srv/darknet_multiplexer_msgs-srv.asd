
(cl:in-package :asdf)

(defsystem "darknet_multiplexer_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "DarknetCameras" :depends-on ("_package_DarknetCameras"))
    (:file "_package_DarknetCameras" :depends-on ("_package"))
  ))