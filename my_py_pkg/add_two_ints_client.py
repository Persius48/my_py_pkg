#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts


class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.call_add_two_ints_server(6, 7)
        self.call_add_two_ints_server(3, 1)
        self.call_add_two_ints_server(5, 2)

    def call_add_two_ints_server(self, x, y):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Add Two Ints...")

        request = AddTwoInts.Request()
        request.a = x
        request.b = y

        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_add_two_ints, p = x, q = y))

    def callback_call_add_two_ints(self, future, p, q):
        try:
            response = future.result()
            self.get_logger().info(str(p) + " + " +
                                   str(q) + " = " + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()