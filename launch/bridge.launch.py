# ファイル: your_package/launch/bridge.launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # /cmd_vel のブリッジ
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='cmd_vel_bridge',
            output='screen',
            arguments=[
                '/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist',
                # 前カメラの CameraInfo
                '/world/default/model/ELM4_Chassis/link/ELM4_Chassis/Base/sensor/camera_front/camera_info'
                '@sensor_msgs/msg/CameraInfo@ignition.msgs.CameraInfo',
                # 後カメラの CameraInfo
                '/world/default/model/ELM4_Chassis/link/ELM4_Chassis/Base/sensor/camera_rear/camera_info'
                '@sensor_msgs/msg/CameraInfo@ignition.msgs.CameraInfo',
            ],
        ),

        # 前カメラの画像ブリッジ
        Node(
            package='ros_gz_image',
            executable='image_bridge',
            name='front_cam_image_bridge',
            output='screen',
            arguments=[
                '/world/default/model/ELM4_Chassis/link/ELM4_Chassis/Base/sensor/camera_front/image'
            ],
        ),

        # 後カメラの画像ブリッジ
        Node(
            package='ros_gz_image',
            executable='image_bridge',
            name='rear_cam_image_bridge',
            output='screen',
            arguments=[
                '/world/default/model/ELM4_Chassis/link/ELM4_Chassis/Base/sensor/camera_rear/image'
            ],
        ),
    ])
