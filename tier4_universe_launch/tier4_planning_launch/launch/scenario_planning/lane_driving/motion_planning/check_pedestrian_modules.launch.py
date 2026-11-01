# Copyright 2026 nuway
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Reject simultaneous pedestrian alternatives before creating planning nodes."""

from launch import LaunchDescription
from launch.actions import OpaqueFunction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration


PEDESTRIAN_MODULE_FLAGS = (
    'launch_pedestrian_speed_matching_module',
    'launch_people_as_planner_module',
    'launch_sfm_module',
)


def validate_modules(context):
    enabled = [
        flag for flag in PEDESTRIAN_MODULE_FLAGS
        if IfCondition(LaunchConfiguration(flag, default='false')).evaluate(context)]
    if len(enabled) > 1:
        raise RuntimeError(
            'Select one pedestrian velocity module, but ' + ', '.join(enabled) +
            ' are enabled. Set the others to false, e.g. '
            'launch_pedestrian_speed_matching_module:=false when enabling '
            'launch_people_as_planner_module:=true or launch_sfm_module:=true')
    return []


def generate_launch_description():
    return LaunchDescription([OpaqueFunction(function=validate_modules)])
