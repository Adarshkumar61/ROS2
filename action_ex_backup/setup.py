from setuptools import setup

package_name = 'action_ex'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Adarsh',
    maintainer_email='adarshb2k61@.com',
    description='ROS2 Python Action Example',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fibonacci_action_server = action_ex.fibonacci_action_server:main',
            'fibonacci_action_client = action_ex.fibonacci_action_client:main',
        ],
    },
)
