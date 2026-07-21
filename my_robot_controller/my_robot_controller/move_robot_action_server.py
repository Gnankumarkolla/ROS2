#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from my_robot_interface.action import MoveRobot
import time

class MoveRobotServer(Node):

    def __init__(self):
        super().__init__("move_robot_server")
        self.server=ActionServer(self,MoveRobot,"move_robot_server",self.callback)

    def callback(self,goal_handle):
        dist=goal_handle.request.distance
        feedback_msg=MoveRobot.Feedback()
        for i in range (1,11):
            time.sleep(1)
            feedback_msg.percentage_completed=i*10.0
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f"Progress:{feedback_msg.percentage_completed}")
        goal_handle.succeed()
        result=MoveRobot.Result()
        result.success=True
        result.message=f"distance moved {dist}m"
        return result
    
def main(args=None):
    rclpy.init(args=args)
    node=MoveRobotServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
    