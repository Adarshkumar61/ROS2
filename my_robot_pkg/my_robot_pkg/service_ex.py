import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Addtwoint(Node):
    def __init__(self):
        super().__init__('Add two int')
        self.srv = self.create_service(AddTwoInts, 'Add two intt', self.callback)
        self.get_logger().info('Add two int is ready')

    def callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Recieved request: {request.a} + {request.b}')
        return response
    
def main(args = None):
    rclpy.init(args=args)
    node = Addtwoint()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '_main__':
    main()