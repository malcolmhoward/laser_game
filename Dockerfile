# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /code

# Set the working directory to /code
WORKDIR /code

# Copy the current directory contents into the container at /code
ADD . /code/

# Update the image to the latest packages
RUN apt-get update && apt-get upgrade -y

# Install basic unix tools. Add whatever to this.
RUN apt-get install less nano -y

# Install git and other dev tools.
RUN apt-get install git build-essential python-dev -y
# TODO: ^^^^ Make sure the above Python libraries are compatible with the version of Python included in this base image

# **Optional** Clone the repository if the Docker image doesn't contain the latest version of the project code
# RUN git clone https://github.com/JosiahDub/laser_game.git

# Update to the latest version of pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Clone and install the Adafruit library
RUN git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
RUN cd Adafruit_Python_PCA9685
RUN python setup.py install

# Alternatively you can install from pip with:
# RUN sudo pip install adafruit-pca9685
# Note that the pip install method won't install the example code.


# Docker Command Cheat Sheet
############################
# sudo docker run -it --name laser-game-ctnr laser-game  # <-- Run this to launch the container as an interactive bash shell
#^^^^^ TODO: Figure out why this crashes when not run as an interactive bash shell (i.e. without using "-it")


# "sudo docker build --rm -t image_name ."  # Build a docker image named image_name using the Dockefile in the current directory
# "sudo docker run -d -p 8005:8001 --name container_name image_name"  # Example command to start a container with an image
# "sudo docker run -d -p host_port:container_port --name container_name image_name"  # Start a docker container named container_name based off of a docker image named image_name
# "sudo docker stop container_name"  # Stop docker container named container_name (needed for graceful deletion)
# "sudo docker rm container_name"  # Remove docker container named container_name
# "sudo docker image rm image_name"  # Remove docker image named image_name
# "sudo docker ps"  # list all RUNNING containers
# "sudo docker ps --all"  # list all containers
# https://docs.docker.com/engine/reference/commandline/run/#options
# -d or --detach runs the container in the background
# -p or --publish publishes a container's port(s) to the host
# -it creates interactive bash shell in the container
# --rm removes intermediate images
# TODO: Figure out how to mount a volume to the container or save the container on exit, so that any data can persist
# "docker-machine create machine_name"  # Create a docker machine named machine_name
