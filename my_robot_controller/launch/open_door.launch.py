#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
                Node(
                    package="my_robot_controller",
                    executable="op_door_server",
                    output="screen"
                ),
                Node(
                    package="my_robot_controller",
                    executable="op_door_client",
                    output="screen"
                )
                
    ])