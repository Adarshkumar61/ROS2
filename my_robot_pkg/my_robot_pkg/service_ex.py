import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts   # Standard service type

class AddTwoIntsService(Node):
    def __init__(self):
        super().__init__('add_two_ints_service')
        # Create service
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().info("Service 'add_two_ints' is ready 🚀")

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Received request: {request.a} + {request.b} = {response.sum}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
