from setuptools import setup

package_name = 'rivzz_visualize'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/cylinder.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adarsh',
    maintainer_email='adarshb2k61.com',
    description='RViz visualization example',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joint_commander = rivzz_visualize.joint_commander:main',
        ],
    },
)
