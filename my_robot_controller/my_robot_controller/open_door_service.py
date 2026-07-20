#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interface.srv import OpenDoor

class OpenDoorService(Node):

    def __init__(self):
        super().__init__("open_door_service")
        self.server=self.create_service(OpenDoor,"open_door",self.callback)

    def callback(self,request,response):
        if request.open:
            response.success=True
            response.message="opening the door..."
        else:
            response.success=False
            response.message="not opening..."
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node=OpenDoorService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()