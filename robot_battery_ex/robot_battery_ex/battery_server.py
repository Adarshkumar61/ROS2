import rclpy
from rclpy.node import Node
from robot_battery_ex.srv import BatteryStatus

class BatteryServer(Node):
    def __init__(self):
        super().__init__('battery_server')
        self.srv = self.create_service(BatteryStatus, 'get_battery_status', self.get_battery_status)
        self.get_logger().info('Battery Service Ready ✅')

    def get_battery_status(self, request, response):
        response.percentage = 76.5
        self.get_logger().info(f'Sending battery status: {response.percentage}%')
        return response

def main():
    rclpy.init()
    node = BatteryServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
