from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py'])
    )

    robot_model = os.path.join(
        get_package_share_directory('leg_control'),
        'sdf',
        'NeptR_model.sdf')  

    spawn_entity = Node(
        package='gazebo_ros', executable='spawn_entity.py',
        arguments=['-file', robot_model, '-entity', 'leg'],
        output='screen')

    return LaunchDescription([
        gazebo,
        spawn_entity,
    ])
