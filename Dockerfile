# This file started from https://github.com/osrf/docker_images/blob/0038f1c3a11aa0fc573d698b39ab5c204aad5a40/ros/jazzy/ubuntu/noble/perception/Dockerfile

# which was a link from here https://hub.docker.com/_/ros/tags

FROM ros:jazzy-ros-base-noble

# install ros2 packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-jazzy-desktop \
    && rm -rf /var/lib/apt/lists/*

# install ros2 packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-jazzy-perception \
    && rm -rf /var/lib/apt/lists/*

RUN echo "alias sr='source /opt/ros/jazzy/setup.bash'" >> ~/.bashrc

# install other useful tools
RUN apt-get update && apt-get install -y vim
RUN apt-get update && apt-get install -y wget
