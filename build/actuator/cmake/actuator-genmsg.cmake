# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "actuator: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg;-Inav_msgs:/opt/ros/melodic/share/nav_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/melodic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(actuator_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv" NAME_WE)
add_custom_target(_actuator_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "actuator" "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(actuator
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/actuator
)

### Generating Module File
_generate_module_cpp(actuator
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/actuator
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(actuator_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(actuator_generate_messages actuator_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv" NAME_WE)
add_dependencies(actuator_generate_messages_cpp _actuator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(actuator_gencpp)
add_dependencies(actuator_gencpp actuator_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS actuator_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(actuator
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/actuator
)

### Generating Module File
_generate_module_eus(actuator
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/actuator
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(actuator_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(actuator_generate_messages actuator_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv" NAME_WE)
add_dependencies(actuator_generate_messages_eus _actuator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(actuator_geneus)
add_dependencies(actuator_geneus actuator_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS actuator_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(actuator
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/actuator
)

### Generating Module File
_generate_module_lisp(actuator
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/actuator
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(actuator_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(actuator_generate_messages actuator_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv" NAME_WE)
add_dependencies(actuator_generate_messages_lisp _actuator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(actuator_genlisp)
add_dependencies(actuator_genlisp actuator_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS actuator_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(actuator
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/actuator
)

### Generating Module File
_generate_module_nodejs(actuator
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/actuator
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(actuator_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(actuator_generate_messages actuator_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv" NAME_WE)
add_dependencies(actuator_generate_messages_nodejs _actuator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(actuator_gennodejs)
add_dependencies(actuator_gennodejs actuator_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS actuator_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(actuator
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/actuator
)

### Generating Module File
_generate_module_py(actuator
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/actuator
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(actuator_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(actuator_generate_messages actuator_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_common/drivers/actuator/srv/ActivateActuator.srv" NAME_WE)
add_dependencies(actuator_generate_messages_py _actuator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(actuator_genpy)
add_dependencies(actuator_genpy actuator_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS actuator_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/actuator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/actuator
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(actuator_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(actuator_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET nav_msgs_generate_messages_cpp)
  add_dependencies(actuator_generate_messages_cpp nav_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(actuator_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/actuator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/actuator
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(actuator_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(actuator_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET nav_msgs_generate_messages_eus)
  add_dependencies(actuator_generate_messages_eus nav_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(actuator_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/actuator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/actuator
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(actuator_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(actuator_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET nav_msgs_generate_messages_lisp)
  add_dependencies(actuator_generate_messages_lisp nav_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(actuator_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/actuator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/actuator
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(actuator_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(actuator_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET nav_msgs_generate_messages_nodejs)
  add_dependencies(actuator_generate_messages_nodejs nav_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(actuator_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/actuator)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/actuator\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/actuator
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(actuator_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(actuator_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET nav_msgs_generate_messages_py)
  add_dependencies(actuator_generate_messages_py nav_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(actuator_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
