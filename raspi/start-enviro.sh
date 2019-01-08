while true
do
    sudo rm -rf /home/pi/gromari/raspi/enviro/enviro.value
    sudo /home/pi/sources/Adafruit_Python_DHT/examples/AdafruitDHT.py 2302 4 >> /home/pi/gromari/raspi/enviro/enviro.value
done
