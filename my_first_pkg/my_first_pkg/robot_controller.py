# import rclpy
# # rclpy is the ROS2 Python client library. 
# # It provides functions to initialise/shutdown ROS2 and to work with nodes, parameters, timers, topics, etc.

# from rclpy.node import Node
# # Node is the base class you inherit from to make a ROS2 node
# # (a running process that can publish/subscribe, offer services, have parameters, log messages, etc.).

# class RobotController(Node): #You define a new node class called RobotController.
#     # This class is a ROS2 node because it inherits from Node.

#     def __init__(self):
#         super().__init__('robot_controller') #This calls the parent Node constructor and names the node "robot_controller".
        
#         # Declare parameter with default value
#         self.declare_parameter('max_speed', 1.0)
#         #Declaring is important: it registers the parameter with the node and sets a default type (here a floating point number).

#         # Get the parameter value
#         speed = self.get_parameter('max_speed').get_parameter_value().double_value
#         #.get_parameter_value() returns a ParameterValue object that can hold various typed fields (int, double, bool, string, etc.).

#         #self.get_parameter('max_speed') returns a Parameter object for max_speed.

#         self.get_logger().info(f'Robot max speed: {speed} m/s')
#         #get_logger() Logs an informational message to the console.
#         # get_logger() gives you a logger scoped to this node name
# def main(args=None):
#     rclpy.init(args=args)
#     rclpy.init() #initializes ROS2 for this process. It must be called before creating nodes.
#     node = RobotController()
#     rclpy.spin(node) #Keeps the node alive and responsive.
#     # spin enters a loop that processes incoming events (timers, subscriptions, service requests, parameter updates, etc.).
#     # In your current code there are no timers/subscriptions/services,
#     #  but spin is still necessary to keep the process running so it can accept parameter updates 
#     # (if your code handled them) or be cleanly shut down.

#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

#to get robot batterly level
# import rclpy
# from rclpy.node import Node

# class RobotBattery(Node):
#     def __init__(self):
#         super().__init__('robot_battery_level')
#         self.declare_parameter('robot_battery', 67)
#         battery = self.get_parameter('robot_battery').get_parameter_value().double_value
#         self.get_logger.info(f'RVA current battery level is: {battery}%')

# def main(args = None):
#     rclpy.init(args= args)
#     node = RobotBattery()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()
# if __name__ == '__main__':
#     main()

import rclpy
from rclpy.node import Node

class RobotBattery(Node):
    def __init__(self):
        super().__init__('robot_battery_level')  # ✅ node name is lowercase, consistent

        # ✅ Declare parameter with correct name
        self.declare_parameter('battery_level', 67)

        # ✅ Read the same parameter
        battery = self.get_parameter('battery_level').get_parameter_value().integer_value

        # ✅ Use .info() to log
        self.get_logger().info(f'RVA current battery level is: {battery}%')

def main(args=None):
    rclpy.init(args=args)  # ✅ only once
    node = RobotBattery()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
