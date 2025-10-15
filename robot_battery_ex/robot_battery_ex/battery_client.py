import rclpy
from rclpy.node import Node
from robot_battery_ex.srv import BatteryStatus

class BatteryClient(Node):
    def __init__(self):
        super().__init__('battery_client')
        self.cli = self.create_client(BatteryStatus, 'get_battery_status')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for battery service...')
        self.req = BatteryStatus.Request()

    def send_request(self):
        future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main():
    rclpy.init()
    client = BatteryClient()
    response = client.send_request()
    client.get_logger().info(f'Battery percentage: {response.percentage}%')
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
