import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from action_exm.action import AddTwoInts
import asyncio

class AddTwoIntsActionServer(Node):
    def __init__(self):
        super().__init__('add_two_ints_server')
        self._action_server = ActionServer(
            self,
            AddTwoInts,
            'add_two_ints',
            self.execute_callback
        )
        self.get_logger().info("✅ Action Server Ready: add_two_ints")

    async def execute_callback(self, goal_handle):
        self.get_logger().info("Goal received")
        a = goal_handle.request.a
        b = goal_handle.request.b

        feedback = AddTwoInts.Feedback()
        result = AddTwoInts.Result()
        result.sum = a + b

        # simulate slow process
        for i in range(1, 6):
            feedback.progress = i * 20.0
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f"Progress: {feedback.progress}%")
            await asyncio.sleep(1.0)

        goal_handle.succeed()
        return result

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsActionServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
