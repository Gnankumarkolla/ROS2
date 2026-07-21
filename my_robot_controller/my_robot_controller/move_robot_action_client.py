#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from my_robot_interface.action import MoveRobot

class MoveRobotClient(Node):

    def __init__(self):
        super().__init__("move_robot_client")
        self._action_client=ActionClient(self,MoveRobot,"move_robot_server")
        
    def send_goal(self):
        goal_msg=MoveRobot.Goal()
        goal_msg.distance=int(input("Enter distance: "))
        self._action_client.wait_for_server()
        self.send_goal_future=self._action_client.send_goal_async(goal_msg,feedback_callback=self.feedback_callback)
        self.send_goal_future.add_done_callback(self.send_goal_callback)

    def send_goal_callback(self,future):
        goal_handle=future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal Rejected")
            return
        self.get_logger().info("Goal Accepted")
        self.result_future=goal_handle.get_result_async()
        self.result_future.add_done_callback(self.get_result_callback)
    
    def get_result_callback(self,future):
        result=future.result().result
        self.get_logger().info(f"success{result.success}")
        self.get_logger().info(result.message)
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node=MoveRobotClient()
    node.send_goal()
    rclpy.spin(node)

if __name__=="__main__":
    main()