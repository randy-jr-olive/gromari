while true
do
    sudo /home/pi/sources/Adafruit_Python_DHT/examples/AdafruitDHT.py 2302 4 2>&1 | tee enviro/enviro.value
done