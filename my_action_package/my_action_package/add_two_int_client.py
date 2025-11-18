
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from my_robot_interfaces.action import AddTwoInt


class AddTwoIntActionClient(Node):
    def __init__(self):
        super().__init__('add_two_int_action_client')
        self._action_client = ActionClient(self, AddTwoInt, 'add_two_int')

    def send_goal(self, a, b):
        self.get_logger().info('Waiting for action server...')
        self._action_client.wait_for_server()
        
        goal_msg = AddTwoInt.Goal()
        goal_msg.a = a
        goal_msg.b = b
        
        self.get_logger().info(f'Sending goal: {a} + {b}')
        
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future): 
        goal_handle = future.result()
        
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return
        
        self.get_logger().info('Goal accepted')
        
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Result received: {result.sum}')
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Received feedback: {feedback.progress_percentage}%')


def main(args=None):
    rclpy.init(args=args)
    
    action_client = AddTwoIntActionClient()
    
    # Send goal with numbers 15 and 27
    action_client.send_goal(15, 27)
    
    rclpy.spin(action_client)


if __name__ == '__main__':
    main()