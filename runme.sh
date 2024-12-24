#!/bin/bash
#
# This script runs a Docker container, bind mounting ~/.ssh for git interaction,
# and mounting a Volume which has the repository checked out into it.

echo "Building the image..."

sudo docker build -t pippin-robot .

echo "Running the container..."

sudo docker run -it --rm \
	--mount type=bind,src=/home/dw/.ssh,dst=/root/.ssh \
	--mount type=bind,src=/home/dw/.gitconfig,dst=/root/.gitconfig \
	--mount type=volume,src=pippin,dst=/root/pippin \
       	pippin-robot
