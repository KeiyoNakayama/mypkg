# SPDX-FileCopyrightText: 2025 Keiyo Nakayama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CpuStatsSubscriber(Node):
    def __init__(self):
        super().__init__("cpu_stats_subscriber")
        self.create_subscription(String, "cpu_stats", self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(f"Received CPU stats: {msg.data}")

def main():
    rclpy.init()
    node = CpuStatsSubscriber()
    rclpy.spin(node)
