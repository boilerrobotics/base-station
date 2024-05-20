# Joystick

We use [Joy](http://wiki.ros.org/joy) package to read the joystick input.
The node `ros2 run joy joy_node` will return an output in `/joy` node with [sensor_msgs/msg/Joy](https://docs.ros2.org/foxy/api/sensor_msgs/msg/Joy.html) message.

`diff_drive.py` consumes raw outputs from `joy_node`.
Then it processes raw outputs into [Twist](https://docs.ros2.org/galactic/api/geometry_msgs/msg/Twist.html) message.

## Testing joystick

Once plugin, you should see the `jsX` when you run

```bash
ls /dev/input
```

`X` is the number of joystick. If you connect only one, it is likely to be `js0`.
You can test the joystick by running

```bash
jstest /dev/input/jsX
```

Or use the GUI application `jstest-gtk`.
Noted: you might need to install `sudo apt install jstest-gtk` before running `jstest`

## Running

```bash
ros2 launch joystick diff_drive_launch.yml
```
