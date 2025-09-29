from setuptools import setup

package_name = 'dancing_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=['src'],  # folder where joint_commander.py is
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/gazebo_launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/dancing_robot.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Adarsh',
    maintainer_email='adarsh@example.com',
    description='Simple dancing robot for Gazebo simulation',
    license='MIT',
    entry_points={
        'console_scripts': [
            'joint_commander = src.joint_commander:main',
        ],
    },
)
