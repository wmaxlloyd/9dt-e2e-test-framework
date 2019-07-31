FROM python:3.7-alpine

# Install Python2, Setup and App dependencies
RUN apk add python2 py-pip curl unzip

# Copy setup files and run setup script
COPY ./requirements.txt /home/requirements.txt
COPY ./setup /home/setup
RUN /home/setup

# Copy Source code
COPY . /home
WORKDIR /home
