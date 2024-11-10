#! /usr/bin/python3

import rclpy

from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
import time

class LegController(Node):
    def __init__(self):
        super().__init__('leg_controller')

        # Publishers for each joint control
        self.upper_lower_joint_pub = self.create_publisher(Float64, '/leg/Upper_Lower_Link_joint/command', 10)
        self.lower_foot_joint_pub = self.create_publisher(Float64, '/leg/Lower_Link_foot_joint/command', 10)

        # Initial joint positions
        self.upper_lower_position = 0.0
        self.lower_foot_position = 0.0

        # Create a timer to publish joint commands
        self.timer = self.create_timer(0.1, self.publish_joint_commands)

    def publish_joint_commands(self):
        # Send a command to move the upper-lower joint
        upper_lower_msg = Float64()
        upper_lower_msg.data = self.upper_lower_position
        self.upper_lower_joint_pub.publish(upper_lower_msg)

        # Send a command to move the lower-foot joint
        lower_foot_msg = Float64()
        lower_foot_msg.data = self.lower_foot_position
        self.lower_foot_joint_pub.publish(lower_foot_msg)

    def set_joint_positions(self, upper_lower_position, lower_foot_position):
        self.upper_lower_position = upper_lower_position
        self.lower_foot_position = lower_foot_position


def main(args=None):
    rclpy.init(args=args)
    leg_controller = LegController()

    # Run the node
    rclpy.spin(leg_controller)
    leg_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
