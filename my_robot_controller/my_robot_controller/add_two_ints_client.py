#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsclient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client=self.create_client(AddTwoInts,"add_two_ints")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("waiting for server...")
        self.request=AddTwoInts.Request()
        self.request.a=int(input("Enter a: "))
        self.request.b=int(input("Enter b: "))
        self.future=self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self,self.future)
        response=self.future.result()
        print(response.sum)

def main(args=None):
    rclpy.init(args=args)
    node=AddTwoIntsclient()
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()