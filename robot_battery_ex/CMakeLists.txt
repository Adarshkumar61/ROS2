cmake_minimum_required(VERSION 3.8)
project(robot_battery_ex)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/BatteryStatus.srv"
)

ament_export_dependencies(rosidl_default_runtime)

install(
  DIRECTORY robot_battery_ex/
  DESTINATION lib/python3.10/site-packages/robot_battery_ex
)

install(PROGRAMS
  robot_battery_ex/battery_server.py
  robot_battery_ex/battery_client.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
