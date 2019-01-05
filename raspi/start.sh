#!/bin/bash

echo "Starting gromari api server"
python3 raspi/coretemp/coretemp.py &
docker-compose -f docker-compose.yml up --force-recreate
