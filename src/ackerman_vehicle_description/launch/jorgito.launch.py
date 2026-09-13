from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
import os


def generate_launch_description():

    package_dir = get_package_share_directory(
        'ackerman_vehicle_description'
    )

    world_file = os.path.join(
        package_dir,
        'worlds',
        'jorgito_world.sdf'
    )

    bridge_config = os.path.join(
        package_dir,
        'config',
        'gz_bridge.yaml'
    )

    rviz_config = os.path.join(
        package_dir,
        'rviz',
        'jorgito_cameras.rviz'
    )

    xacro_file = os.path.join(
        package_dir,
        'urdf',
        'jorgito_robot.xacro'
    )

    robot_description = Command([
        'xacro ',
        xacro_file
    ])

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': f'-r {world_file}'
        }.items()
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {
                'robot_description': robot_description
            }
        ]
    )

    spawn_robot = TimerAction(
        period=3.0,
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('ros_gz_sim'),
                        'launch',
                        'gz_spawn_model.launch.py'
                    )
                ),
                launch_arguments={
                    'world': 'jorgito_world',
                    'topic': '/robot_description',
                    'entity_name': 'jorgito',
                    'z': '0.1'
                }.items()
            )
        ]
    )

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='ros_gz_bridge',
        output='screen',
        parameters=[
            {
                'config_file': bridge_config
            }
        ]
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config]
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        bridge,
        spawn_robot,
        rviz
    ])
