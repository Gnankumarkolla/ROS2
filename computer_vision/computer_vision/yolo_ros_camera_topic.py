#!/usr/bin/env python3
import cv2
import rclpy
from rclpy.node import Node
from ultralytics import YOLO
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

    
class CameraSubscriber(Node):
    def __init__(self):
        super().__init__("camera_subscriber")
        self.model=YOLO("yolo26n.pt")
        self.bridge=CvBridge()
        
        self.imgmsg_subscriber=self.create_subscription(Image,"/camera/image_raw",self.pic_callback,10)
        self.publisher=self.create_publisher(String,"/detected_object",10)
        self.cmd_publisher=self.create_publisher(Twist,"/cmd_vel",10)
        

    def pic_callback(self,msg):
            
            img=self.bridge.imgmsg_to_cv2(msg,"bgr8")
            label=None
            result=self.model(img)
            for box in result[0].boxes:
                cls=int(box.cls)
                label=self.model.names[cls]
            ann=result[0].plot()
            cv2.imshow("video",ann)
            cv2.waitKey(1)

            if not label==None:
                object_msg=String()
                object_msg.data=label
                cmd=Twist()
                if object_msg.data=="bottle":
                    cmd.linear.x=0.0
                    cmd.angular.z=0.0
                elif object_msg.data=="person":
                    cmd.linear.x=0.5
                    cmd.angular.z=0.0
                else :
                    cmd.linear.x=0.0
                    cmd.angular.z=0.02
                
                self.cmd_publisher.publish(cmd)
                self.publisher.publish(object_msg)
cv2.destroyAllWindows()            


def main(args=None):
    rclpy.init(args=args)
    node=CameraSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=='__main__':
    main()
    