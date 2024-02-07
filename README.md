# Base Station repo

This repo contains the code that will be running at the base station.
This repo is a ROS2 workspace that depends on interfaces from [brc_msgs](https://github.com/boilerrobotics/brc_msgs).
Clone or download [brc_msgs](https://github.com/boilerrobotics/brc_msgs) into the same location as this repo is required.

## Setup

First update package dependencies by running following command

```bash
rosdep install --from-paths src --ignore-src
```

To compile or run manually, see the instruction in [rover-code](https://github.com/boilerrobotics/rover-code).

Since this repo depends on [brc_msgs](https://github.com/boilerrobotics/brc_msgs), you will need to build and install packages from `brc_msgs` as well.

### Automated Setup

Run `source setup.bash` for automatic setup.
Then you can run node or launch files.
