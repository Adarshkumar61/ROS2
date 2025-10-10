from setuptools import setup
import os
from glob import glob

package_name = 'robot_arm_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # everytime you add a launch file, update the following line
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adarsh61',
    maintainer_email='adarshb2k61@gmail.com',
    description='Robot arm simulation package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
setup