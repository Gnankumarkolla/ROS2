from launch import LaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription,TimerAction
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_path = get_package_share_directory('robot_description')
    urdf_file = os.path.join(pkg_path, 'urdf', 'robo.urdf')
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        )
    )

    with open(urdf_file, 'r') as infp:
        robot_description = infp.read()

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        ),

        gazebo,

        TimerAction(
            period=3.0,
            actions=[
                    Node(
                        package='gazebo_ros',
                        executable='spawn_entity.py',
                        arguments=[
                            '-topic','robot_description','-entity','my_robot'
                        ],
                        output='screen'
                    )
            ]
        )
    ])