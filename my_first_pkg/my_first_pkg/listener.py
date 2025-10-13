# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String

# class MinimalSubscriber(Node):
#     def __init__(self):
#         super().__init__('minimal_subscriber')
#         self.subscription = self.create_subscription(
#             String,
#             'chatter',
#             self.listener_callback,
#             10)
#         self.subscription  # prevent unused variable warning

#     def listener_callback(self, msg):
#         self.get_logger().info(f'I heard: "{msg.data}"')

# def main(args=None):
#     rclpy.init(args=args)
#     node = MinimalSubscriber()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__('listener')
        # ✅ Correct attribute name
        self.subscription = self.create_subscription(
            String,
            'chatter',   # topic name
            self.listener_callback,
            10           # queue size
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
