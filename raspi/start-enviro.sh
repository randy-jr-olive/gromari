while true
do
    sudo /home/pi/sources/Adafruit_Python_DHT/examples/AdafruitDHT.py 2302 4 | sudo tee /home/pi/gromari/raspi/enviro/enviro.value
done
