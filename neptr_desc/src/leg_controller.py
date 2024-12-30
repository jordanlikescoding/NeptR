import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class LegController(Node):
    def __init__(self):
        super().__init__('leg_controller')
        # Create publishers for each joint of the robot's leg
        self.joint1_pub = self.create_publisher(Float64, '/robot/Upper_Lower_Link_joint_position', 10)
        self.joint2_pub = self.create_publisher(Float64, '/robot/Lower_Foot_joint_position', 10)

        # Timer to periodically publish joint commands (every 0.1 seconds)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        # Example of controlling joint angles (in radians)
        joint1_msg = Float64()
        joint1_msg.data = 0.5  # Joint 1 position, e.g., move leg forward
        
        joint2_msg = Float64()
        joint2_msg.data = -0.5  # Joint 2 position, e.g., bend the leg
        # Publish the commands
        self.joint1_pub.publish(joint1_msg)
        self.joint2_pub.publish(joint2_msg)

def main(args=None):
    rclpy.init(args=args)

    leg_controller = LegController()

    # Spin the node to keep it alive and handling callbacks
    rclpy.spin(leg_controller)

    # Shutdown the ROS client library for Python
    rclpy.shutdown()

if __name__ == '__main__':
    main()