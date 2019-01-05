# This Dockerfile is used to build an image containing the python
# gromari api, a grow room management tool.

FROM ubuntu:rolling
MAINTAINER Randy Olive <randy.jr.olive@gmail.com>

# Add apt-cacher proxy
RUN echo 'Acquire::http::Proxy "http://10.0.1.210:3142";' | tee /etc/apt/apt.conf.d/01proxy

# Install apt-utils
RUN apt-get update \
    && apt-get install apt-utils -y

# Make sure the package repository is up to date.
RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y dist-upgrade

# Install packages needed for running the app
RUN apt-get update && apt-get install -y \
    nano \
    python3 \
    python3-pip

# Use pip3 to install python dependencies
RUN pip3 install --no-cache-dir\
    django \
    gunicorn \
    redis

# Clean up apt after installations
RUN apt-get autoremove --purge -y \
    && apt-get autoclean \
    && apt-get clean \
    && echo "removing apt lists" \
    && rm -rf /var/lib/apt/lists/* \
    && echo "removing apt cache" \
    && rm -rf /var/cache/apt/archives/*

# Set the working directory inside the container
RUN mkdir /code
WORKDIR /code
RUN mkdir /code/log/api
RUN touch /code/log/api/api.log
