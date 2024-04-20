
(cl:in-package :asdf)

(defsystem "detection_tree_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Dvector" :depends-on ("_package_Dvector"))
    (:file "_package_Dvector" :depends-on ("_package"))
  ))