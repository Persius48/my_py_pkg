import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisher(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("number_publisher") # MODIFY NAME
        self.number_ = 2
        self.publisher_ = self.create_publisher(Int64,"num_channel",10)
        self.timer_ = self.create_timer(0.5,self.publish_num)
        self.get_logger().info("Number publishing has been started")

    def publish_num(self):
        msg = Int64()
        msg.data = self.number_
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()