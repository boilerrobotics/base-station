from setuptools import find_packages, setup

package_name = 'frontend_connector'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tam',
    maintainer_email='thirawat.tam@gmail.com',
    description='Link ROS and web fronetnd',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mqtt_bridge = frontend_connector.mqtt_bridge:main',
        ],
    },
)
