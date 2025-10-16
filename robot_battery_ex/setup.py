from setuptools import setup

package_name = 'robot_battery_ex'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adarsh',
    maintainer_email='',
    description='Battery status service example',
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'battery_server = robot_battery_ex.battery_server:main',
            'battery_client = robot_battery_ex.battery_client:main',
        ],
    },
)
