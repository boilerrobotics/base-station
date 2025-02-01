import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data, qos_profile_system_default
from rclpy.qos import QoSProfile,HistoryPolicy, DurabilityPolicy, Duration, LivelinessPolicy, ReliabilityPolicy

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class RoverControlPublisherNode(Node):

    def __init__(self):
        super().__init__("rover_manual_control_publisher")
        qos_profile = QoSProfile(
            history = HistoryPolicy.KEEP_LAST,
            reliability = ReliabilityPolicy.BEST_EFFORT,
            depth = 5,
            durability = DurabilityPolicy.VOLATILE,
            liveliness = LivelinessPolicy.AUTOMATIC,
            lifespan = Duration(seconds=.1, nanoseconds=0)
        )
        self.subscription = self.create_subscription(
            Joy, "joy", self.controller_callback, qos_profile
        )
        self.publisher_ = self.create_publisher(
            Twist,
            "cmd_vel",
            qos_profile_sensor_data,
            # Might need to modify QOS policy.
            # Better to use sensor data but it is not compatible with Gazebo policy
            # It could be fixed by changing gazebo policy
        )

    def controller_callback(self, controller: Joy):
        """
        Map controller input to Twist message.
        Left analog (axis 1) control speed -> twist.linear.x
        Right analog (axis 3) control steering -> twist.angular.z
        """

        msg = Twist()
        msg.linear.x = controller.axes[1]
        msg.angular.z = controller.axes[3]

        self.publisher_.publish(msg)
        self.get_logger().debug(f"speed: {msg.linear.x}, steering: {msg.angular.z}")


def main(args=None):
    rclpy.init(args=args)

    publisher = RoverControlPublisherNode()
    rclpy.spin(publisher)

    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
