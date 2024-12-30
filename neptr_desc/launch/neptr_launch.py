import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # starts ign gazebo sim and rviz2
    custom_world = '/home/brian/neptr2_ws/neptr_desc/worlds/canyonview_field.world'
    sdf_file = '/home/brian/neptr2_ws/neptr_desc/model/model/neptr_sdf'
    rviz_config_file = '/home/brian/neptr2_ws/neptr_desc/rviz/neptr_config.rviz'
    
    # MoveIt 2 configuration
    # moveit_config_package = 'your_moveit_config_package'
    # moveit_config_file = 'your_moveit_config_file'


    return LaunchDescription([
        # Start Ignition Gazebo with the SDF file
        ExecuteProcess(
            cmd=['ign', 'gazebo', sdf_file],
            output='screen'
        ),

        # Start RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_file]
        ),

        # Start the ROS2 bridge
        ExecuteProcess(
            cmd=['ros2', 'run', 'ros_ign_bridge', 'parameter_bridge', 
                 '/model/neptr/joint_state@sensor_msgs/msg/JointState@ignition.msgs.Model',
                 '/model/neptr/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist'],
            output='screen'
        ),
    ])