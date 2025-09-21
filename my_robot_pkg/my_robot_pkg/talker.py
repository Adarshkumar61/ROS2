import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher:
    def __init__(self):
        super().__init__('Publisher')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)