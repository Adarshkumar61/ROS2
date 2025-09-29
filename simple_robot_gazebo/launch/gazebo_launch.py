import os


from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('simple_robot_gazebo')
    urdf_file = os.path.join(pkg_share, 'urdf', 'simple_robot.urdf')
    world_file = os.path.join(pkg_share, 'worlds', 'empty.world')
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={'world': world_file}.items()
    )
    with open(urdf_file, 'r') as inf:
        robot_description = inf.read()
    
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )
    jsp_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{'use_gui': True}]
    )
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'simple_robot', '-file', urdf_file],
        output='screen'
    )
    spawn_delay = TimerAction(period=3.0, actions=[spawn_entity])
    return LaunchDescription([
        gazebo_launch,
        rsp_node,
        jsp_node,
        spawn_delay,
   ])