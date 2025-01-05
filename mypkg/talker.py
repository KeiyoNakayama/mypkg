import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

rclpy.init()
node = Node("random")
pub= node.create_publisher(Int16, "countup", 10)



def cb():
    n = random.randint(1,100)
    msg = Int16()
    msg.data = n
    pub.publish(msg)


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)

