import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class RobotSpeed(Node):
    def __init__(self):
        super().__init__('robot_speed')
        self.declare_parameter('robot_speed', 200)
        speed = self.get_parameter('robot_speed').value
        self.get_logger().info(f'B2S current speed is : {speed}km/h')
        self.add_on_set_parameters_callback(self.parameter_callback)

    def parameter_callback(self, params):
        for param in params:
            if self.name == 'robot_speed':
                self.get_logger().info(f'B2S speed updated to: {param.value}km/h')
        return rclpy.parameter.ParameterEventHandler.Result(successful=True)
    
def main(args = None):
    rclpy.init(args= args)
    node = RobotSpeed()
    rclpy.spin(node)
    node.destroy_node() 
    rclpy.shutdown()

if __name__ == '__main__':
    main()