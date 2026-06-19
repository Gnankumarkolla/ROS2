#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import speech_recognition as sr
recognizer=sr.Recognizer()
class voice_controller(Node):
    def __init__(self):
        super().__init__("Voice_controll_robot")
        self.publisher=self.create_publisher(Twist,"cmd_vel",10)
    def voice_callback(self):
        cmd=Twist()
        with sr.Microphone() as source :
            self.get_logger().info("Listening")
            recognizer.adjust_for_ambient_noise(source)
            audio=recognizer.listen(source)
        try:
            text=recognizer.recognize_google(audio)
            try:
                if text=="forward" :
                    cmd.linear.x=0.2
                    cmd.angular.z=0.0
                elif text=="backward":
                    cmd.linear.x=-0.2
                    cmd.angular.z=0.0
                elif text=="right":
                    cmd.linear.x=-0.0
                    cmd.angular.z=-0.5
                elif text=="left":
                    cmd.linear.x=0.0
                    cmd.angular.z=0.5
            except:
                self.get_logger().info("please tell any direction")
        except sr.UnknownValueError:
            self.get_logger().info("couldn't understand")
        except sr.RequestError:
            self.get_logger().info("check your internet connection ")
        self.publisher.publish(cmd)
def main(args=None):
    rclpy.init(args=args)
    node=voice_controller()
    node.voice_callback()
    node.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()