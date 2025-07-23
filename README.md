# Bumperbot-Controllers

This Repo contains controller implementations for the Bumperbot robot using "ROS 2 Humble" and "Ignition Gazebo". It provides both custom and differntial drive controller support, allowing flexibility for simulation and experimentation.

---

## 📦 Features

- "Custom Python Controller" : `simple_controller.py` - (Calculates wheel velocities and publishes Odometry + TF)
- "Standard ROS 2 Controller" : `diff_drive_controller` - from the `ros2_control` framework named as bumperbot_controller in the yaml file.

## 📁 Repository Structure
```
Bumperbot-Controllers/
├── bumperbot_controller/                 # Custom and standard controller logic
│ ├── config/                             # YAML config for controllers
│ ├── launch/                             # Launch files for controllers
│ ├── scripts/                            # Utility scripts (e.g., twist conversion)
│ └── bumperbot_controller/               # Python module for controller logic
│
├── bumperbot_description/                # Robot model and simulation files
│ ├── launch/                             # Gazebo launch files
│ ├── meshes/                             # Visual assets
│ └── urdf/                               # URDF / Xacro files for Bumperbot
```
## 🛠️ Installation

Make sure you have ROS 2 and Ignition Gazebo installed. Then clone the package into your ROS 2 workspace:
```
cd ~/bumperbot_ws/src
git clone https://github.com/Puskarish/Bumperbot-Controllers
cd ~/bumperbot_ws
colcon build
source install/setup.bash
```

## 📡 Launching the Robot

1. Gazebo Simulation
   `ros2 launch bumperbot_description gazebo.launch.py`

2. Controller Launch
   `ros2 launch bumperbot_controller controller.launch.py`

## 🎮 Switching Controllers

This repo supports two controller modes:

    🧠 simple_controller: Custom Controller
    ⚙️ diff_drive_controller: Standard ROS 2 controller

You can switch between them manually. Initially it is default set to simple_controller mode, by using `ros2 launch bumperbot_controller controller.launch.py use_simple_controller:=false` you can use diff_drive_controller named as bumperbot_controller.

## 🕹️ Usage Instructions

After launching the bumperbot in the gazebo world and its controller you can move your bumperbot in two ways:

1. Move the Bumperbot via Teleop:
   
- First install ```teleop_twist_keyboard``` with ```sudo apt install ros-humble-teleop-twist-keyboard```.
- The purpose of using `twist_to_twiststamped.py` : teleop twist keyboard publishes on `geometry_msgs/msg/Twist` but Bumperbot subscription message type is `geometry_msgs/msg/TwistStamped`. That's why this file is required.

- On one terminal run `ros2 run bumperbot_controller twist_to_twiststamped.py`.
- In the next terminal run `ros2 run teleop_twist_keyboard teleop_twist_keyboard`.

  After this you can move the Bumperbot by the commands given in `teleop_twist_keyboard`.

2. After launching the controller **Publish msg on topic bumperbot_controller/cmd_vel**:

- In other terminal run
```
ros2 topic pub /bumperbot_controller/cmd_vel geometry_msgs/msg/TwistStamped "header:
  stamp:
    sec: 0
    nanosec: 0
  frame_id: ''
twist:
  linear:
    x: 0.0
    y: 0.0
    z: 0.0
  angular:
    x: 0.0
    y: 0.0
    z: 0.0" 
```
- Now you can change the linear and angular velocity to move the Bumperbot.   

## References

[Bumperbot Github
](https://github.com/AntoBrandi/Self-Driving-and-ROS-2-Learn-by-Doing-Odometry-Control/tree/main/Section9_Odometry/bumperbot_ws/src)
