import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_file = os.path.join(
        get_package_share_directory('urdf_robot_visualize'),
        'urdf',
        'cylinder.urdf.xacro'
    )

