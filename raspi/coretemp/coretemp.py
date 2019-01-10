import os

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

print(measure_temp(), file=open("/home/pi/gromari/raspi/coretemp/coretemp.value", "w"))
