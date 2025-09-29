import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class DanceRobot(Node):
    def __init__(self):
        super().__init__('dance_robot')

        # Joint topics
        self.joint_topics = {
            'left_arm_joint': '/left_arm_joint_position_controller/command',
            'right_arm_joint': '/right_arm_joint_position_controller/command',
            'left_leg_joint': '/left_leg_joint_position_controller/command',
            'right_leg_joint': '/right_leg_joint_position_controller/command'
        }

        self.publishers = {}
        for joint, topic in self.joint_topics.items():
            self.publishers[joint] = self.create_publisher(Float64, topic, 10)

        self.step = 0
        self.timer = self.create_timer(0.5, self.dance_step)

    def dance_step(self):
        positions = [
            {'left_arm_joint': 0.5, 'right_arm_joint': -0.5, 'left_leg_joint': 0.3, 'right_leg_joint': -0.3},
            {'left_arm_joint': -0.5, 'right_arm_joint': 0.5, 'left_leg_joint': -0.3, 'right_leg_joint': 0.3}
        ]
        current = positions[self.step % 2]

        for joint, angle in current.items():
            msg = Float64()
            msg.data = angle
            self.publishers[joint].publish(msg)

        self.step += 1

def main(args=None):
    rclpy.init(args=args)
    node = DanceRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
