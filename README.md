# Jorgito Coitito — ROS 2 Ackermann Rover

Simulation and description package for an Ackermann-steering mobile rover using **ROS 2 Jazzy** and **Gazebo Harmonic**.

The project integrates a modular Xacro-based robot model with multiple perception sensors and a ROS 2 ↔ Gazebo communication layer using `ros_gz_bridge`.

## Features

* Ackermann-steering mobile robot model.
* Modular URDF/Xacro architecture.
* Gazebo Harmonic simulation.
* Four directional cameras:

  * Front
  * Rear
  * Left
  * Right
* Forward-facing RGB-D camera.
* 2D planar LiDAR with 360° horizontal scanning.
* 6-axis IMU.
* ROS 2 sensor interfaces through `ros_gz_bridge`.
* TF tree generated from robot joints and sensor frames.
* RViz configuration for sensor visualization.
* Single launch file for Gazebo, robot state publisher, bridge and RViz.

## Sensor Interfaces

| Sensor            | Gazebo topic               | ROS 2 type                    |
| ----------------- | -------------------------- | ----------------------------- |
| Front camera      | `/camera_front`            | `sensor_msgs/msg/Image`       |
| Rear camera       | `/camera_rear`             | `sensor_msgs/msg/Image`       |
| Left camera       | `/camera_left`             | `sensor_msgs/msg/Image`       |
| Right camera      | `/camera_right`            | `sensor_msgs/msg/Image`       |
| RGB-D color       | `/rgbd_camera/image`       | `sensor_msgs/msg/Image`       |
| RGB-D depth       | `/rgbd_camera/depth_image` | `sensor_msgs/msg/Image`       |
| RGB-D camera info | `/rgbd_camera/camera_info` | `sensor_msgs/msg/CameraInfo`  |
| RGB-D point cloud | `/rgbd_camera/points`      | `sensor_msgs/msg/PointCloud2` |
| LiDAR             | `/scan`                    | `sensor_msgs/msg/LaserScan`   |
| IMU               | `/imu`                     | `sensor_msgs/msg/Imu`         |
| Joint states      | `/joint_states`            | `sensor_msgs/msg/JointState`  |
| Velocity command  | `/cmd_vel`                 | `geometry_msgs/msg/Twist`     |

## Robot Frames

The robot model contains dedicated frames for the main body, wheels, steering links and sensors.

Sensor frames include:

* `camera_front`
* `camera_rear`
* `camera_left`
* `camera_right`
* `rgbd_camera_link`
* `lidar_link`
* `imu_link`

The TF tree is generated from the robot model and the simulated joint states.

## Requirements

* Ubuntu 24.04 LTS
* ROS 2 Jazzy
* Gazebo Harmonic
* `ros_gz_sim`
* `ros_gz_bridge`
* `xacro`
* `robot_state_publisher`
* RViz 2

## Installation

Create a ROS 2 workspace and clone this repository into the `src` directory:

```bash
mkdir -p ~/workspaces_/sm26_ws/src
cd ~/workspaces_/sm26_ws/src
git clone https://github.com/RataCuco25/Jorgito_coitito.git
```

Install dependencies:

```bash
cd ~/workspaces_/sm26_ws
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths src --ignore-src -r -y
```

Build the workspace:

```bash
colcon build --symlink-install
```

Source the workspace:

```bash
source install/setup.bash
```

## Launch the Simulation

The complete simulation can be started with:

```bash
source /opt/ros/jazzy/setup.bash
source ~/workspaces_/sm26_ws/install/setup.bash
ros2 launch ackerman_vehicle_description jorgito.launch.py
```

The launch file starts:

1. Gazebo Harmonic.
2. The robot state publisher.
3. The ROS 2 ↔ Gazebo bridge.
4. The Jorgito rover model.
5. RViz 2 with the configured sensor visualization.

## RViz

A dedicated RViz configuration is included at:

```text
rviz/jorgito_cameras.rviz
```

It provides visualization for the rover's TF tree and camera sensors.

The general RViz configuration is also available at:

```text
rviz/rviz_config.rviz
```

## Package Structure

```text
ackerman_vehicle_description/
├── config/
│   └── gz_bridge.yaml
├── launch/
│   ├── display.launch.py
│   └── jorgito.launch.py
├── rviz/
│   ├── jorgito_cameras.rviz
│   └── rviz_config.rviz
├── urdf/
│   ├── cameras.xacro
│   ├── imu.xacro
│   ├── jorgito_description.xacro
│   ├── jorgito_gazebo.xacro
│   ├── jorgito_robot.xacro
│   ├── lidar.xacro
│   └── rgbd_camera.xacro
├── worlds/
│   └── jorgito_world.sdf
├── CMakeLists.txt
└── package.xml
```

## Xacro Architecture

The main robot file includes the individual robot and sensor definitions:

```text
jorgito_robot.xacro
├── jorgito_description.xacro
├── lidar.xacro
├── cameras.xacro
├── rgbd_camera.xacro
├── imu.xacro
└── jorgito_gazebo.xacro
```

This modular structure allows individual sensors and robot components to be maintained independently.

## ROS 2 ↔ Gazebo Bridge

The bridge configuration is located at:

```text
config/gz_bridge.yaml
```

It maps Gazebo Transport messages to standard ROS 2 message types for the rover's cameras, RGB-D camera, LiDAR, IMU and joint states.

## License

This project is licensed under the Apache License 2.0.

See the [LICENSE](LICENSE) file for the complete license text.

## Author

**Luis Héctor Muñoz Del Razo**

Mechatronics Engineering
Tecnológico de Monterrey — Campus Puebla
