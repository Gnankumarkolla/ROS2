#!/usr/bin/env python 3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
class turtlebot_maze_solver(Node):
   
    def __init__(self):
        super().__init__("turtlebot_maze_solver")
        self.subscription=self.create_subscription(LaserScan,'/scan',self.scan_callback,10)
        self.publisher=self.create_publisher(Twist,"/cmd_vel",10)
    def scan_callback(self,msg):
     try:
        if len(msg.ranges)==0:
                return
        front=msg.ranges[len(msg.ranges)//2]
        left=msg.ranges[len(msg.ranges)//4]
        right=msg.ranges[3*len(msg.ranges)//4]
        cmd=Twist()
        if front<0.7:
            if right>0.5:
                cmd.angular.z=-0.5
                cmd.linear.x=0.0
                print("right")
            elif left>0.5:
                cmd.angular.z=0.5
                cmd.linear.x=0.0
                print("left")
            else:
                cmd.linear.x=-0.2
                cmd.angular.z=0.0
                print("back")
        else:
            cmd.linear.x=0.3
            cmd.angular.z=0.0
            print("front")
        self.publisher.publish(cmd)
     except Exception as e:
             print("error",e)
        
def main(args=None):
    rclpy.init(args=args)
    node=turtlebot_maze_solver()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()