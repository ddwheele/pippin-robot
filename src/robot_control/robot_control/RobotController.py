import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.5
        msg.linear.y = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: %f, %f' % (msg.linear.x, msg.linear.y))


def main(args=None):
    rclpy.init(args=args)

    robot_controller = RobotController()

    rclpy.spin(robot_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    robot_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

