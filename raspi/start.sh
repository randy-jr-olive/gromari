#!/bin/bash

echo "Starting gromari api server"
mkdir -p ./log/api
touch ./log/api/api.log
watch -n 5 python3 coretemp/coretemp.py &
docker-compose -f docker-compose.yml up --force-recreate
