#!/bin/bash

echo "Starting gromari api server"
python3 coretemp/coretemp.py &
docker-compose -f docker-compose.yml up --force-recreate
