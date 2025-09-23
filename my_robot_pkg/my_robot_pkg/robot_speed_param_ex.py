import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class robot_speed(Node):
    def __init__(self):
        super().__init__('robot_speed')
        self.declare_parameter('robot_speed', 123)
        speed = self.get_parameter('robot speed').get_parameter_value().integer_value
        self.get_logger().info(f'B2S current speed is: {speed}/h')

def main(args = None):
    rclpy.init(args=args)
    node = robot_speed()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()