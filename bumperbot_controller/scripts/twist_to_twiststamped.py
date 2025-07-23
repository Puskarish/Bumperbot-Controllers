#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped

class TwistToTwistStamped(Node):
    def __init__(self):
        super().__init__('twist_to_twiststamped')
        self.pub = self.create_publisher(TwistStamped, '/bumperbot_controller/cmd_vel', 10)
        self.sub = self.create_subscription(Twist, '/cmd_vel', self.callback, 10)

    def callback(self, msg:Twist):
        stamped_msg = TwistStamped()
        stamped_msg.header.stamp = self.get_clock().now().to_msg()
        stamped_msg.twist = msg
        self.pub.publish(stamped_msg)

def main():
    rclpy.init()
    twist_to_twiststamped = TwistToTwistStamped()
    rclpy.spin(twist_to_twiststamped)
    twist_to_twiststamped.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
