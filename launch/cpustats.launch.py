# SPDX-FileCopyrightText: 2025 Keiyo Nakayama
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    check_cpu_stats = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'check_cpu_stats',
            )

    listener_cpu_stats = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'listener_cpu_stats',
            output = 'screen'
            )

    return launch.LaunchDescription([check_cpu_stats, listener_cpu_stats])
