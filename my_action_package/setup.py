from setuptools import setup

package_name = 'my_action_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Adarsh',
    maintainer_email='adarshb2k61@gmail.com',
    description='ROS2 Action Server and Client',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'add_two_int_server = my_action_package.add_two_int_server:main',
            'add_two_int_client = my_action_package.add_two_int_client:main',
        ],
    },
)