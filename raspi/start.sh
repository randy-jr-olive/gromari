#!/bin/bash

echo "Starting gromari api server"
mkdir -p /home/pi/gromari/raspi/log/api
touch /home/pi/gromari/raspi/log/api/api.log
#watch -n 5 python3 /home/pi/gromari/raspi/coretemp/coretemp.py >> /dev/null &
#watch -n 5 sudo /home/pi/sources/Adafruit_Python_DHT/examples/AdafruitDHT.py 2302 4 >> /dev/null &
cd /home/pi/gromari/raspi/
docker-compose -f docker-compose.yml up --force-recreate
