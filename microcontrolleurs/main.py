import psutil 
import time

def temp(n):
    while True:
        time.sleep(n)
        tps = psutil.sensors_temperatures()
        tempe = tps['coretemp'][1].current
        print(tempe)

temp(1)