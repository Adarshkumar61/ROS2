import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from action_exm.action import AddTwoInts

class AddTwoIntsActionClient(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')
        self._client = ActionClient(self, AddTwoInts, 'add_two_ints')

    def send_goal(self, a, b):
        goal_msg = AddTwoInts.Goal()
        goal_msg.a = a
        goal_msg.b = b

        self._client.wait_for_server()
        self.get_logger().info('Sending goal request...')
        self._send_goal_future = self._client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return
        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Feedback: {feedback.progress}%')

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Result: {result.sum}')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsActionClient()
    node.send_goal(10, 20)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
