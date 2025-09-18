import rclpy
from rclpy.node import Node

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        # Declare parameter with default value
        self.declare_parameter('max_speed', 1.0)

        # Get the parameter value
        speed = self.get_parameter('max_speed').get_parameter_value().double_value
        self.get_logger().info(f'Robot max speed: {speed} m/s')

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
