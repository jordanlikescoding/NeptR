import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.substitutions import FindPackageShare

# def generate_launch_description():
#     pkg_share = os.path.join(os.getenv('COLCON_PREFIX_PATH'), 'neptr_description', 'share', 'neptr_description')
#     urdf_file = os.path.join(pkg_share, 'urdf', 'neptr.urdf.xacro')

#     return LaunchDescription([
#         Node(
#             package='robot_state_publisher',
#             executable='robot_state_publisher',
#             name='robot_state_publisher',
#             output='screen',
#             parameters=[{'robot_description': os.popen(f'xacro {urdf_file}').read()}]
#         ),
#         Node(
#             package='rviz2',
#             executable='rviz2',
#             name='rviz2',
#             output='screen',
#         ),
#     ])

def generate_launch_description():
    package_share_dir = FindPackageShare("neptr_description").find("neptr_description")
    urdf_file_path = package_share_dir + "/urdf/neptr.urdf.xacro"

    return LaunchDescription([
        # Node to execute xacro and generate robot_description
        Node(
            package='xacro',
            executable='xacro',
            name='xacro_to_urdf',
            output='screen',
            arguments=[urdf_file_path],  # Argument to specify the xacro file
            # This will publish the robot_description parameter
            parameters=[{
                'robot_description': Command(['xacro ', urdf_file_path])
            }]
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', urdf_file_path])
            }]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
        )
    ])
