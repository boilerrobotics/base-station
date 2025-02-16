from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="joy",
                executable="joy_node",
            ),
            Node(
                package="joystick",
                executable="control_rover",
            ),
            Node(
                package="image_view",
                executable="image_view",
                remappings=[
                    ("image/compressed", "/zed/zed_node/rgb/image_rect_color/compressed")
                ],
                parameters=[
                    {"image_transport": "compressed"}
                ]
            )
        ]
    )


