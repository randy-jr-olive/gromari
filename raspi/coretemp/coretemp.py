import os
import time

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

while True:
        print("getting temp:")
        print(measure_temp())
        print(measure_temp(), file=open("./coretemp/coretemp.value", "w"))
time.sleep(5)
