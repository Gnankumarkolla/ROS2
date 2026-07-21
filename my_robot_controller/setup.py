from setuptools import find_packages, setup
import os 
from glob import glob

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),glob('launch/*.launch.py')),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gnan',
    maintainer_email='gnan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "test_node= my_robot_controller.my_first_node:main",
            "draw_circle=my_robot_controller.draw_circle:main",
            "pose_subscriber=my_robot_controller.pose_subscriber:main",
            "turtle_controller=my_robot_controller.turtle_controller:main",
            "add_two_ints_server=my_robot_controller.add_two_ints_service:main",
            "add_two_ints_client=my_robot_controller.add_two_ints_client:main",
            "op_door_server=my_robot_controller.open_door_service:main",
            "op_door_client=my_robot_controller.open_door_client:main",
            "mv_rob_ser=my_robot_controller.move_robot_action_server:main",
            "mv_rob_cli=my_robot_controller.move_robot_action_client:main",
        ],
    },
)
