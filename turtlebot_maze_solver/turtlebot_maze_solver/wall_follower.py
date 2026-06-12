#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
class wallFollower(Node):
    def __init__(self):
        super().__init__("wall_follower")
        self.subscription=self.create_subscription(LaserScan,"/scan",self.scan_callback,10)
        self.publisher=self.create_publisher(Twist,"/cmd_vel",10)
    def scan_callback(self,msg):
        front=msg.ranges[len(msg.ranges)//2]
        left=msg.ranges[len(msg.ranges)//4]
        right=msg.ranges[3*len(msg.ranges)//4]
        cmd=Twist()
        if front<0.5:
            cmd.angular.z=-0.2
            cmd.linear.x=0.0
        elif right<0.6:
            cmd.linear.x=0.0
            cmd.angular.z=0.2
        else:
            cmd.linear.x=0.2
            cmd.angular.z=0.0
        self.publisher.publish(cmd)
def main(args=None):
    rclpy.init(args=args)
    node=wallFollower()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()