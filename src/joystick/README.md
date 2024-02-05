# Joystick

We use [Joy](http://wiki.ros.org/joy) package to read the joystick input.
The node `ros2 run joy joy_node` will return an output in `/joy` node with [sensor_msgs/msg/Joy](https://github.com/ros/common_msgs/blob/noetic-devel/sensor_msgs/msg/Joy.msg) message.

`tank_drive.py` consumes raw outputs from `joy_node`. 
Then it processes raw outputs into [DriveCmd](https://github.com/boilerrobotics/brc_msgs/blob/main/msg/DriveCmd.msg).

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
ros2 launch joystick tank_drive_launch.yml
```
