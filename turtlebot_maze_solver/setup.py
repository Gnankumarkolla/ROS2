from setuptools import find_packages, setup

package_name = 'turtlebot_maze_solver'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gnan',
    maintainer_email='gnankumarkolla@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "turtlebot_movement=turtlebot_maze_solver.obstacle:main",
            "wall_follower=turtlebot_maze_solver.wall_follower:main",
            "waypoint_navigator=turtlebot_maze_solver.send_goal:main",
            "voice_controller=turtlebot_maze_solver.voice_controll_robot:main",
        ],
    },
)
