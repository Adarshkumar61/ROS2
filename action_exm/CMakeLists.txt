find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "action/AddTwoInts.action"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()

