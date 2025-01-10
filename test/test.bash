#!/bin/bash -xv
#SPDX-FileCopyrightText: 2025 Keiyo Nakayama
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 75 ros2 launch mypkg cpustats.launch.py | tee - /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Context Switches:, Interrupts:, Soft Interrupts:, Syscall:'
