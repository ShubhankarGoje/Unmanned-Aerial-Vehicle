execute_process(COMMAND "/home/shubhankargoje/catkin_ws/build/planner/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/shubhankargoje/catkin_ws/build/planner/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
