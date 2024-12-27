import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Direct paths to the SDF and RViz configuration files
    sdf_file = '/home/brian/neptr2_ws/neptr_desc/model/model/neptr_sdf'
    rviz_config_file = '/home/brian/neptr2_ws/neptr_desc/rviz/neptr_config.rviz'

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
    ])