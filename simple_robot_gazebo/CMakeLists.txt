cmake_minimum_required(VERSION 3.5)
project(simple_robot_gazebo)


find_package(ament_cmake REQUIRED)
find_package(gazebo_ros REQUIRED)


install(DIRECTORY launch urdf worlds
DESTINATION share/${PROJECT_NAME}
)


ament_package()