from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_path
import os


def generate_launch_description():

    robot_description_pkg = get_package_share_path(
        "ackerman_vehicle_description"
    )

    urdf_path = os.path.join(
        robot_description_pkg,
        "urdf",
        "jorgito_description.xacro"
    )

    rviz_config_path = os.path.join(
        robot_description_pkg,
        "rviz",
        "rviz_config.rviz"
    )

    robot_description = ParameterValue(
        Command([
            "xacro ",
            urdf_path
        ]),
        value_type=str
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        parameters=[
            {
                "robot_description": robot_description
            }
        ]
    )

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui"
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=["-d", rviz_config_path]
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz_node
    ])