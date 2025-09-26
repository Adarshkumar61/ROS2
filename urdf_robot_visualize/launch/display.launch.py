from launch import LaunchDescription
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Path to your URDF file
    urdf_file = os.path.join(
        get_package_share_directory('urdf_robot_visualize'),
        'urdf',
        'my_robot.urdf'
    )

    return LaunchDescription([
        # Robot State Publisher (publishes TF from URDF)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            arguments=[urdf_file],
            output='screen'
        ),

        # RViz2 to visualize
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        ),
    ])
