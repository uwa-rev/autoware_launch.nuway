# Copyright 2021 the Autoware Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Co-developed by Tier IV, Inc. and Apex.AI, Inc.

from launch import LaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.actions import LoadComposableNodes, Node
from launch_ros.descriptions import ComposableNode
from ament_index_python import get_package_share_directory
import os

def generate_launch_description():
    # decl_package = DeclareLaunchArgument("package", "socketcan")

    config_path = os.path.join(get_package_share_directory("nuway_sensor_kit_launch"), "config", "test.yaml")

    component_node = Node(
        package="rclcpp_components",
        executable="component_container",
        name="lidar_container",
        # parameters=[{"thread_num" : 2}],
        arguments=['--ros-args', '--log-level', "info"],
        output="screen"
    )

    load_composable_nodes = LoadComposableNodes(
        target_container="lidar_container",
        composable_node_descriptions=[
            ComposableNode(
                package="nebula_ros",
                plugin="VelodyneRosWrapper",
                name="velodyne_ros_wrapper_node",
                parameters=[config_path],
        )])
    
    return LaunchDescription([
        component_node,
        load_composable_nodes
    ])

