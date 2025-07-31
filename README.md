
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
