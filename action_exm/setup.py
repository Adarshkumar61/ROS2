from setuptools import setup
from glob import glob
import os

package_name = 'action_exm'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],  # Must match your module folder
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/action', glob('action/*.action')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adarsh61',
    maintainer_email='adarshb2k61@gmail.com',
    description='Example action package',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'add_two_ints_action_server = action_exm.add_two_ints_action_server:main',
            'add_two_ints_action_client = action_exm.add_two_ints_action_client:main',
        ],
    },
)
