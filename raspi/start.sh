#!/bin/bash

echo "Starting gromari api server"
mkdir -p ./log/api
touch ./log/api/api.log
watch -n 5 python3 coretemp/coretemp.py >> /dev/null &
watch -n 5 sudo /home/pi/sources/Adafruit_Python_DHT/examples/AdafruitDHT.py 2302 4 >> /dev/null &
docker-compose -f docker-compose.yml up --force-recreate
