import rclpy
from rclpy.node import Node

import board
from adafruit_motorkit import MotorKit

from geometry_msgs.msg import Twist

class MotorDriver(Node):

    def __init__(self):
        super().__init__('motor_driver')
        self.kit = MotorKit(i2c=board.I2C())
	self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.kit = MotorKit(i2c=board.I2C())

    def listener_callback(self, msg):
        self.get_logger().info('I heard: %f,%f' % (msg.linear.x, msg.linear.y))
        self.kit.motor1.throttle = msg.linear.x
        self.kit.motor3.throttle = msg.linear.x

def main(args=None):
    rclpy.init(args=args)

    motor_driver = MotorDriver()

    rclpy.spin(motor_driver)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    motor_driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
