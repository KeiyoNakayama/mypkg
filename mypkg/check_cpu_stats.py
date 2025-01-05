# SPDX-FileCopyrightText: 2025 Keiyo Nakayama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil

class CpuStatsPublisher(Node):
    def __init__(self):
       super().__init__('cpu_stats_publisher')
       self.publisher = self.create_publisher(String, 'cpu_stats', 10)
       self.timer = self.create_timer(1.0, self.publish_cpu_stats)

    def publish_cpu_stats(self):
        stats = psutil.cpu_stats()
        context_switches = stats.ctx_switches
        interrupts = stats.interrupts
        soft_interrupts = stats.soft_interrupts
        syscalls = stats.syscalls
        message = String()
        message.data = (
            f"Context Switches: {context_switches}, Interrupts: {interrupts}, "
            f"Soft Interrupts: {soft_interrupts}, Syscalls: {syscalls}"
        )

        self.publisher.publish(message)

def main():
    rclpy.init()
    node = CpuStatsPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()




