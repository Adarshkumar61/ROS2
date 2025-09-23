import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class robotspeed(Node):
    def __init__(self):
        super().__init__('robot_speed')
        self.declare_parameter('robot_speed', 123)
        speed = self.get_parameter('robot_speed').value
        self.get_logger().info(f'B2S current speed is: {speed}/h')

def main(args = None):
    rclpy.init(args=args)
    node = robotspeed()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()