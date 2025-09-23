import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class robot_speed(Node):
    def __init__(self):
        super().__init__('robot_speed')
        self.declare_parameter('robot_speed', 1.0)
        speed = self.get_parameter('robot speed').get_parameter_value().integer_value
        