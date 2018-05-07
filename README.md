# GripperRobot
Semester Project for the course Machine Learning

# About
A simulation of a robotic arm in a 3D environment, with 6 joints learning to reach a target object using Reinforcement Learning.

This project requires Gazebo and Robotic Operating System (ROS) Kinetic to be installed on Ubuntu 16.0.4.

The file must be in the script folder under catkin_ws/src/test

The project also required the gripper_robot.urdf file to be in the urdf folder under catkin_ws/src/test

# Setup

  cd catkin_ws/
  source devel/setup.bash
  cd src/
  catkin_crt_package test
  catkin_create_pkg test
  cd ..
  catkin_make
  rosrun gazebo_ros gazebo
  roscd test
  cd urdf/
  rosrun gazebo_ros spawn_model -file gripper_robot.urdf -urdf -model gripper_robot

# Start:

  cd script/
  chmod +x get_joint_and_link_status.py 
  chmod +x RL_brain.py
  rosrun test get_joint_and_link_status.py
