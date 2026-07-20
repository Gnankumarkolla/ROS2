#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interface.srv import OpenDoor

class OpenDoorClient(Node):

    def __init__(self):
        super().__init__("open_door_client")
        self.client=self.create_client(OpenDoor,"open_door")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(">>>waiting for server...")
        self.request=OpenDoor.Request()
        a=int(input("enter 1 for true and 0 for false: "))
        if a==1:
            self.request.open=True
        else:
            self.request.open=False
        self.future=self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self,self.future)
        response=self.future.result()
        print(response.success)
        print(response.message)


def main(args=None):
    rclpy.init(args=args)
    node=OpenDoorClient()
    node.destroy_node()
    rclpy.shutdown()