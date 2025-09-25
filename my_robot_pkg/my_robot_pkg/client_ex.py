import rclpy 
import sys
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class addtwointclient(Node):
    def __init__(self):
        super().__init__('add two int')
        self.client = self.create_client(AddTwoInts, 'add two int')
        while not self.client.wait_for_service(timeout_sec= 1.0):
            self.get_logger().info('waiting..')
    

    def send_request(self, a, b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()
    
def main(args = None):
    rclpy.init(args=args)
    node = addtwointclient()
    a = int(sys.argv[1]) if len(sys.argv)<1 else 3
    b = int(sys.argv[2]) if len(sys.argv)>2 else 4
    response = node.send_request(a,b)
    node.get_logger().info(f'Result of {a} + {b} is: {response.sum}')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()