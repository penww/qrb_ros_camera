# Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause-Clear

import launch
import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression


def generate_launch_description():
    config_dir = get_package_share_directory('qrb_ros_camera')

    camera_id_arg = DeclareLaunchArgument(
        'camera_id', default_value='4',
        description='QCarCam inputId for the D457')

    camera_info_path_arg = DeclareLaunchArgument(
        'camera_info_path',
        default_value=os.path.join(config_dir, 'config', 'camera_info_OX03F10_yuv.yaml'),
        description='Absolute path to camera intrinsic YAML file')

    dump_arg = DeclareLaunchArgument(
        'dump', default_value='False',
        description='Dump received frames to disk (debug)')

    camera_id        = LaunchConfiguration('camera_id')
    camera_info_path = LaunchConfiguration('camera_info_path')
    dump             = LaunchConfiguration('dump')

    dump_image_topic       = PythonExpression(["'/cam' + '", camera_id, "' + '_stream1'"])
    dump_camera_info_topic = PythonExpression(["'/cam' + '", camera_id, "' + '_stream1_camera_info'"])

    container = ComposableNodeContainer(
        name='camera_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='qrb_ros_camera',
                plugin='qrb_ros::camera::CameraNode',
                name='camera_node',
                parameters=[{
                    'camera_id':        PythonExpression(["int('", camera_id, "')"]),
                    'stream_size':      3,
                    'stream_name':      ['stream0', 'stream1', 'stream2'],
                    'stream0.width':    1280,
                    'stream0.height':   720,
                    'stream0.fps':      30,
                    'stream0.format':   'mipi16',   # Depth
                    'stream1.width':    1280,
                    'stream1.height':   720,
                    'stream1.fps':      30,
                    'stream1.format':   'nv12',     # Color
                    'stream2.width':    1280,
                    'stream2.height':   720,
                    'stream2.fps':      30,
                    'stream2.format':   'mipi8',    # IR
                    'camera_info_path': camera_info_path,
                }],
            ),
            ComposableNode(
                package='qrb_ros_camera',
                plugin='qrb_ros::camera::TestNode',
                name='test',
                remappings=[
                    ('/image',       dump_image_topic),
                    ('/camera_info', dump_camera_info_topic),
                ],
                parameters=[{
                    'dump':             dump,
                    'dump_camera_info': False,
                }],
            ),
        ],
        output='screen',
    )

    return launch.LaunchDescription([
        camera_id_arg,
        camera_info_path_arg,
        dump_arg,
        container,
    ])
