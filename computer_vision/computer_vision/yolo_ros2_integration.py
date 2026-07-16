#!/usr/bin/env python3
import cv2
import rclpy
from rclpy.node import Node
from ultralytics import YOLO
from std_msgs.msg import String
from geometry_msgs.msg import Twist

    
class YOlO_ros2(Node):
    def __init__(self):
        super().__init__("yolo_ros_integration")
        self.model=YOLO("yolo26n.pt")
        self.cap=cv2.VideoCapture(0)
        
        self.publisher=self.create_publisher(String,"/detected_object",10)
        self.cmd_publisher=self.create_publisher(Twist,"/cmd_vel",10)
        self.create_timer(0.03,self.pic_callback)

    def pic_callback(self):
            
            success,img=self.cap.read()
            if cv2.waitKey(1) & 0xFF ==ord('q'):
              self.cap.release()
              cv2.destroyAllWindows()
              rclpy.shutdown()
              return

            label=None
            result=self.model(img)
            for box in result[0].boxes:
                cls=int(box.cls)
                label=self.model.names[cls]
            ann=result[0].plot()
            cv2.imshow("video",ann)

            if not label==None:
                msg=String()
                msg.data=label
                self.publisher.publish(msg)
                self.get_logger().info(msg.data)
                cmd=Twist()
                if msg.data=="bottle":
                    cmd.linear.x=0.0
                    cmd.angular.z=0.0
                elif msg.data=="person":
                    cmd.linear.x=0.5
                    cmd.angular.z=0.0
                else :
                    cmd.linear.x=0.0
                    cmd.angular.z=0.02
                self.cmd_publisher.publish(cmd)
                self.publisher.publish(msg)
cv2.destroyAllWindows()            


def main(args=None):
    rclpy.init(args=args)
    node=YOlO_ros2()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=='__main__':
    main()
    