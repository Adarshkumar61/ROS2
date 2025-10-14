#!/usr/bin/env python3

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from my_robot_interfaces.action import AddTwoInt
import time


class AddTwoIntActionServer(Node):
    def __init__(self):
        super().__init__('add_two_int_action_server')
        self._action_server = ActionServer(
            self,
            AddTwoInt,
            'add_two_int',
            self.execute_callback
        )
        self.get_logger().info('Action Server has been started')

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        
        # Get the goal values
        a = goal_handle.request.a
        b = goal_handle.request.b
        
        # Create feedback message
        feedback_msg = AddTwoInt.Feedback()
        
        # Simulate some work being done (adding in steps)
        # This shows how feedback works
        for i in range(1, 6):
            feedback_msg.progress_percentage = i * 20
            self.get_logger().info(f'Feedback: {feedback_msg.progress_percentage}%')
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.5)  # Simulate some computation time
        
        # Mark as succeeded and return result
        goal_handle.succeed()
        
        # Create result
        result = AddTwoInt.Result()
        result.sum = a + b
        
        self.get_logger().info(f'Result: {a} + {b} = {result.sum}')
        return result


def main(args=None):
    rclpy.init(args=args)
    action_server = AddTwoIntActionServer()
    
    try:
        rclpy.spin(action_server)
    except KeyboardInterrupt:
        pass
    
    action_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()