execute_process(COMMAND "/home/yunfantang/duckietown/catkin_ws/build_isolated/line_detector/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/yunfantang/duckietown/catkin_ws/build_isolated/line_detector/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
