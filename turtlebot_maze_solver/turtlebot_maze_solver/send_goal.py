#! usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import Twist
class GoalSender(Node):
    def __init__(self):
        super().__init__("waypoint_navigator")
        self.client=ActionClient(self,NavigateToPose,'navigate_to_pose')
        self.client.wait_for_server()
        self.waypoints=[
            (1.62,0.57),
            (2.28,-0.45),
            (-0.33,-1.5)
        ]
        self.current_waypoint=0
        self.send_goal()
    def send_goal(self):
        if self.current_waypoint>=len(self.waypoints):
            self.get_logger().info("All waypoints reached")
            return
        x,y=self.waypoints[self.current_waypoint]
        goal=NavigateToPose.Goal()
        goal.pose.header.frame_id="map"
        goal.pose.header.stamp=self.get_clock().now().to_msg()
        goal.pose.pose.position.x=x
        goal.pose.pose.position.y=y
        goal.pose.pose.orientation.w=1.0
        self.get_logger().info(f"Going to wapoint {self.current_waypoint+1} ,({x},{y})")
        future=self.client.send_goal_async(goal)
        future.add_done_callback(self.goal_sender_callback)
    def goal_sender_callback (self,future):
        goal_handle=future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal Rejected")
            return
        self.get_logger().info("Goal accepted")
        result_future=goal_handle.get_result_async()
        result_future.add_done_callback(self.goal_result_callback)
    def goal_result_callback(self , future):
        result=future.result()
        self.get_logger().info(f"waypoint {self.current_waypoint+1}")
        self.get_logger().info(f"error= {result.status}")
        self.current_waypoint+=1
        self.send_goal()
def main():
    rclpy.init()
    node=GoalSender()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=='__main__':
    main()