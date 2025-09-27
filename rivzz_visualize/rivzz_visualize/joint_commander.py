import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math
import time

class JointPublisher(Node):
    def __init__(self):
        super().__init__('joint_publisher')
        self.pub = self.create_publisher(JointState, 'joint_states', 10)
        self.joint_name = ['base_to_top']
        self.angle = 0.0
        self.timer_period = 0.05  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = self.joint_name
        self.angle += 0.02  # increment angle
        msg.position = [math.sin(self.angle)]
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = JointPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
