# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "darknet_multiplexer_msgs: 0 messages, 1 services")

set(MSG_I_FLAGS "")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(darknet_multiplexer_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv" NAME_WE)
add_custom_target(_darknet_multiplexer_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "darknet_multiplexer_msgs" "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(darknet_multiplexer_msgs
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/darknet_multiplexer_msgs
)

### Generating Module File
_generate_module_cpp(darknet_multiplexer_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/darknet_multiplexer_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(darknet_multiplexer_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(darknet_multiplexer_msgs_generate_messages darknet_multiplexer_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv" NAME_WE)
add_dependencies(darknet_multiplexer_msgs_generate_messages_cpp _darknet_multiplexer_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(darknet_multiplexer_msgs_gencpp)
add_dependencies(darknet_multiplexer_msgs_gencpp darknet_multiplexer_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS darknet_multiplexer_msgs_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(darknet_multiplexer_msgs
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/darknet_multiplexer_msgs
)

### Generating Module File
_generate_module_eus(darknet_multiplexer_msgs
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/darknet_multiplexer_msgs
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(darknet_multiplexer_msgs_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(darknet_multiplexer_msgs_generate_messages darknet_multiplexer_msgs_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv" NAME_WE)
add_dependencies(darknet_multiplexer_msgs_generate_messages_eus _darknet_multiplexer_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(darknet_multiplexer_msgs_geneus)
add_dependencies(darknet_multiplexer_msgs_geneus darknet_multiplexer_msgs_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS darknet_multiplexer_msgs_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(darknet_multiplexer_msgs
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/darknet_multiplexer_msgs
)

### Generating Module File
_generate_module_lisp(darknet_multiplexer_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/darknet_multiplexer_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(darknet_multiplexer_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(darknet_multiplexer_msgs_generate_messages darknet_multiplexer_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv" NAME_WE)
add_dependencies(darknet_multiplexer_msgs_generate_messages_lisp _darknet_multiplexer_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(darknet_multiplexer_msgs_genlisp)
add_dependencies(darknet_multiplexer_msgs_genlisp darknet_multiplexer_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS darknet_multiplexer_msgs_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(darknet_multiplexer_msgs
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/darknet_multiplexer_msgs
)

### Generating Module File
_generate_module_nodejs(darknet_multiplexer_msgs
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/darknet_multiplexer_msgs
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(darknet_multiplexer_msgs_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(darknet_multiplexer_msgs_generate_messages darknet_multiplexer_msgs_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv" NAME_WE)
add_dependencies(darknet_multiplexer_msgs_generate_messages_nodejs _darknet_multiplexer_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(darknet_multiplexer_msgs_gennodejs)
add_dependencies(darknet_multiplexer_msgs_gennodejs darknet_multiplexer_msgs_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS darknet_multiplexer_msgs_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(darknet_multiplexer_msgs
  "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/darknet_multiplexer_msgs
)

### Generating Module File
_generate_module_py(darknet_multiplexer_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/darknet_multiplexer_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(darknet_multiplexer_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(darknet_multiplexer_msgs_generate_messages darknet_multiplexer_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/shubhankargoje/catkin_ws/src/cusub-develop/cusub_perception/darknet_multiplexer/darknet_multiplexer_msgs/srv/DarknetCameras.srv" NAME_WE)
add_dependencies(darknet_multiplexer_msgs_generate_messages_py _darknet_multiplexer_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(darknet_multiplexer_msgs_genpy)
add_dependencies(darknet_multiplexer_msgs_genpy darknet_multiplexer_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS darknet_multiplexer_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/darknet_multiplexer_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/darknet_multiplexer_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/darknet_multiplexer_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/darknet_multiplexer_msgs
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/darknet_multiplexer_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/darknet_multiplexer_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/darknet_multiplexer_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/darknet_multiplexer_msgs
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/darknet_multiplexer_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/darknet_multiplexer_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/darknet_multiplexer_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
