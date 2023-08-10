import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64  
from example_interfaces.srv import SetBool


class NumberCounter(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("number_counter") # MODIFY NAME
        self.declare_parameter=("testing_param",0)
        self.counter_ = 0
        self.publisher_ = self.create_publisher(Int64,"num_count",10)
        self.subscriber_ = self.create_subscription(Int64, "num_channel", self.callback_robot_news, 10)
        self.server_ = self.create_service(
            SetBool, "reset_counter", self.callback_add_two_ints)
        self.get_logger().info("Number coutner has been started")
        self.get_logger().info("reset counter server has been started.")

    def callback_robot_news(self, msg):
        self.counter_ += msg.data
        new_msg = Int64()
        new_msg.data = self.counter_
        self.publisher_.publish(new_msg)
    def callback_add_two_ints(self, request, response):
        if (request.data):
            self.counter_ = 0
            response.message = "counter sucessfully reset"
            response.success = True
            self.get_logger().info(response.message)
        else:
            response.success = False
            response.message = "counter reset failed"
            self.get_logger().info(response.message)

        return response


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounter() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()