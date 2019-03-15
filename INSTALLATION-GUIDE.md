# ROS + Gazebo Installation Guide
 
 Most of this information is from: http://sdk.rethinkrobotics.com/wiki/Workstation_Setup

# Install Ubuntu

Install Ubuntu 14.04, the guide recommends 14.04.5 but the current LTS 14.04.6 works fine.
http://releases.ubuntu.com/14.04/

If you need a hand doing this there’s heaps of guides online. Also works fine when dual booting with windows. I assume it would work if you run ubuntu in a VM in windows

# Install ROS

ROS Indigo seems to work, so once ubuntu is installed, open a terminal and copy paste these commands:

    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list'

    wget http://packages.ros.org/ros.key -O - | sudo apt-key add -

    sudo apt-get update

    sudo apt-get install ros-indigo-desktop-full

    sudo rosdep init

    rosdep update

    sudo apt-get install python-rosinstall

# Set Up Workspace

Make a directory to be your ROS workspace
    
    mkdir -p ~/ros_ws/src


Add ROS environment functions to your terminal session:

    source /opt/ros/indigo/setup.bash
    
Note!! You’ll need to run this every time you open a new terminal when using ROS, as the environment commands aren’t in the default path, should be able to solved this by editing your bash profile, i will look into this

Build and install
    
    cd ~/ros_ws
    
    catkin_make
    
    catkin_make install

# Baxter SDK

Install dependencies

    sudo apt-get update
    sudo apt-get install git-core python-argparse python-wstool python-vcstools python-rosdep ros-indigo-control-msgs ros-indigo-joystick-drivers

Install SDK

    cd ~/ros_ws/src
    wstool init .
    wstool merge https://raw.githubusercontent.com/RethinkRobotics/baxter/master/baxter_sdk.rosinstall
    wstool update

Not sure if this is necessary, but the guide says to Add ROS environment functions to your terminal session… Again

Add ROS environment functions to your terminal session:

    source /opt/ros/indigo/setup.bash

Build and install again

    cd ~/ros_ws

    catkin_make
    
    catkin_make install

# Configure Baxter Communication/ROS Workspace

    wget https://github.com/RethinkRobotics/baxter/raw/master/baxter.sh

    chmod u+x baxter.sh

The next step is to customise the baxter.sh script you just downloaded so you can connect to baxter over the network. Haven’t been able to try this obviously yet so I will update once we’ve met our friend rosie. The description on how to do this is step 6 of the guide linked at the start of this document.

# Gazebo Installation

Gazebo is a robot simulation software that emulates the environment we will be using when actually communicating with baxter.

Install baxter simulator

    sudo apt-get install gazebo2 ros-indigo-qt-build ros-indigo-driver-common ros-indigo-gazebo-ros-control ros-indigo-gazebo-ros-pkgs ros-indigo-ros-control ros-indigo-control-toolbox ros-indigo-realtime-tools ros-indigo-ros-controllers ros-indigo-xacro python-wstool ros-indigo-tf-conversions ros-indigo-kdl-parser

    cd ~/ros_ws/src

    wstool init .

May get an error here, it’s okay to ignore I think

    wstool merge https://raw.githubusercontent.com/RethinkRobotics/baxter_simulator/master/baxter_simulator.rosinstall

    wstool update

Again build the source

    source /opt/ros/indigo/setup.bash

    cd ~/ros_ws

    catkin_make

    cp src/baxter/baxter.sh .

Edit the baxter.sh file in ~/ros_ws/ with your text editor of choice
Near the top of this file there will be two lines:

    your_ip="192.168.XXX.XXX"
    #your_hostname="my_computer.local"

You can either enter your local ip address in the your_ip field, or a better option is to comment out the your_ip field and use your_hostname instead. It will error out if both fields are present. For example:

    #your_ip="192.168.XXX.XXX"
    your_hostname="<<hostname>>.local"

I changed mine to:

    #your_ip="192.168.XXX.XXX"
    your_hostname="lach-linux.local"

# Gazebo Simulation environment

There is an issue with Gazebo where a setup file has the wrong UR, to fix this edit the files at /usr/share/gazebo/setup.sh and /usr/share/gazebo-2.2/setup.sh

Find the line:
    export GAZEBO_MODEL_DATABASE_URI=http://gazebosim.org/models
Change it to:
    export GAZEBO_MODEL_DATABASE_URI=http://old.gazebosim.org/models

Run Gazebo

    cd ~/ros-ws/

    ./baxter.sh sim

    roslaunch baxter_gazebo baxter_world.launch

You should see baxter in a new window, wait about 30 second until the notification stating: Gravity compensation was turned off

To run one of the included example processes, open another terminal session and run:

    cd ~/ros-ws/
    ./baxter.sh sim
    rosrun baxter_examples joint_velocity_wobbler.py

This runs an example file located in ~/ros_ws/src/baxter_examples/scripts/
Have a look in this folder to see the kind of python programming require to get this guy moving.

Also check out the link: http://sdk.rethinkrobotics.com/wiki/Hello_Baxter
Particularly step 5, you should be able to manipulate baxter in the gazebo environment using python at this point (make sure you stop the joint_velocity_wobbler.py process before you try!)