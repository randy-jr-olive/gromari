import os

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

print(measure_temp(), file=open("./coretemp/coretemp.value", "w"))
