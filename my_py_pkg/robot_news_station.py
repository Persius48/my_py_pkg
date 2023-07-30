#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class RobotNewStationNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("robot_new_station") # MODIFY NAME
        self.robot_name_ = "C3PO"
        self.publisher_ = self.create_publisher(String,"robot_news",10)
        self.timer_ = self.create_timer(0.5,self.publish_news)
        self.get_logger().info("Robot news station has been started")

    def publish_news(self):
        msg = String()
        msg.data = "Hello I am " + self.robot_name_
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewStationNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()