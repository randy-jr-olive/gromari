#!/bin/bash

echo "Starting gromari api server"
RUN mkdir -p ./log/api
RUN touch ./log/api/api.log
python3 coretemp/coretemp.py &
docker-compose -f docker-compose.yml up --force-recreate
