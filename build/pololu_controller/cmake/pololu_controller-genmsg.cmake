# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "pololu_controller: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ipololu_controller:/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(pololu_controller_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg" NAME_WE)
add_custom_target(_pololu_controller_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pololu_controller" "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(pololu_controller
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pololu_controller
)

### Generating Services

### Generating Module File
_generate_module_cpp(pololu_controller
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pololu_controller
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(pololu_controller_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(pololu_controller_generate_messages pololu_controller_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg" NAME_WE)
add_dependencies(pololu_controller_generate_messages_cpp _pololu_controller_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pololu_controller_gencpp)
add_dependencies(pololu_controller_gencpp pololu_controller_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pololu_controller_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(pololu_controller
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pololu_controller
)

### Generating Services

### Generating Module File
_generate_module_eus(pololu_controller
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pololu_controller
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(pololu_controller_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(pololu_controller_generate_messages pololu_controller_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg" NAME_WE)
add_dependencies(pololu_controller_generate_messages_eus _pololu_controller_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pololu_controller_geneus)
add_dependencies(pololu_controller_geneus pololu_controller_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pololu_controller_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(pololu_controller
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pololu_controller
)

### Generating Services

### Generating Module File
_generate_module_lisp(pololu_controller
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pololu_controller
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(pololu_controller_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(pololu_controller_generate_messages pololu_controller_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg" NAME_WE)
add_dependencies(pololu_controller_generate_messages_lisp _pololu_controller_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pololu_controller_genlisp)
add_dependencies(pololu_controller_genlisp pololu_controller_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pololu_controller_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(pololu_controller
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pololu_controller
)

### Generating Services

### Generating Module File
_generate_module_nodejs(pololu_controller
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pololu_controller
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(pololu_controller_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(pololu_controller_generate_messages pololu_controller_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg" NAME_WE)
add_dependencies(pololu_controller_generate_messages_nodejs _pololu_controller_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pololu_controller_gennodejs)
add_dependencies(pololu_controller_gennodejs pololu_controller_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pololu_controller_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(pololu_controller
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_controller
)

### Generating Services

### Generating Module File
_generate_module_py(pololu_controller
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_controller
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(pololu_controller_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(pololu_controller_generate_messages pololu_controller_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/pololu_controller/msg/MotorCommand.msg" NAME_WE)
add_dependencies(pololu_controller_generate_messages_py _pololu_controller_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pololu_controller_genpy)
add_dependencies(pololu_controller_genpy pololu_controller_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pololu_controller_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pololu_controller)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pololu_controller
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(pololu_controller_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pololu_controller)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pololu_controller
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(pololu_controller_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pololu_controller)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pololu_controller
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(pololu_controller_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pololu_controller)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pololu_controller
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(pololu_controller_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_controller)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_controller\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_controller
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_controller
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_controller/.+/__init__.pyc?$"
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(pololu_controller_generate_messages_py std_msgs_generate_messages_py)
endif()
