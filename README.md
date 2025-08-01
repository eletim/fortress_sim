
# robots

https://app.gazebosim.org/fuel/models

- ELM4_Chassis: https://app.gazebosim.org/BloodyUpwork/fuel/models/ELM4-Chassis



# dependencies

- ros2 humble
- ignition gazebo fortress
- ros-humble-ros-gz-image

```sh
sudo apt update
sudo apt install ros-humble-ros-gz-image
```

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
ros2 launch launch/bridge.launch.py
```

terminal 3:
```sh
ros2 run teleop_twist_keyboard teleop_twist_keyboard 
```

ign topic確認
```sh
ign topic -l
```
