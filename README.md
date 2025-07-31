
# dependencies

- ros2 humble
- ignition gazebo fortress

動作確認
```sh
ign gazebo shapes.sdf
```

# spawn

```sh
export IGN_GAZEBO_RESOURCE_PATH=$IGN_GAZEBO_RESOURCE_PATH:/home/eletim/ros2_ws/src/fortress_sim
export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:/home/eletim/ros2_ws/src/fortress_sim
ign gazebo worlds/ELM4.world
```

# cmd_vel

terminal 1:
```sh
export IGN_GAZEBO_RESOURCE_PATH=$IGN_GAZEBO_RESOURCE_PATH:/home/eletim/ros2_ws/src/fortress_sim
export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:/home/eletim/ros2_ws/src/fortress_sim
ign gazebo worlds/ELM4.world
```

terminal 2:
```sh
 ros2 run ros_gz_bridge parameter_bridge \
  /cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist
```

terminal 3:
```sh
ros2 run teleop_twist_keyboard teleop_twist_keyboard 
```

