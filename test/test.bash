#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Keiyo Nakayama
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws


colcon build

source $dir/.bashrc

timeout 30 ros2 launch mypkg cpustats.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep -E 'Context Switches: [0-9]+, Interrupts: [0-9]+, Soft Interrupts: [0-9]+, Syscalls: [0-9]+'

