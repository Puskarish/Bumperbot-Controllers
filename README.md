# Bumperbot-Controllers

This Repo contains controller implementations for the Bumperbot robot using "ROS 2 Humble" and "Ignition Gazebo". It provides both custom and differntial drive controller support, allowing flexibility for simulation and experimentation.

---

## 📦 Features

- "Custom Python Controller" : "simple_controller.py" - (Calculates wheel velocities and publishes Odometry + TF)
- "Standard ROS 2 Controller" : "diff_drive_controller" - from the "ros2_control" framework.

## 📁 Repository Structure

Bumperbot-Controllers/
├── bumperbot_controller/                 # Custom and standard controller logic
│ ├── config/                             # YAML config for controllers
│ ├── launch/                             # Launch files for controllers
│ ├── scripts/                            # Utility scripts (e.g., twist conversion)
│ └── bumperbot_controller/               # Python module for controller logic
│
├── bumperbot_description/                # Robot model and simulation files
│ ├── launch/                             # Gazebo and RViz launch files
│ ├── meshes/                             # Visual assets
│ ├── rviz/                               # RViz config
│ └── urdf/                               # URDF / Xacro files for Bumperbot

## 🛠️ Installation

Make sure you have ROS 2 and Ignition Gazebo installed. Then clone the package into your ROS 2 workspace:

cd ~/bumperbot_ws/src
git clone 
