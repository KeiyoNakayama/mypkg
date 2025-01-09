#!/bin/bash -xv
#SPDX-FileCopyrightText: 2025 Keiyo Nakayama
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg check_cpu_stats > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'data: Context Switches:, Interrupts:, Soft Interrupts:, Syscalls:'
