#!/usr/bin/python
#
#
#
#
#
#

import time, datetime
import serial


f = open('/home/pi/GardenMonitor/BeagleBone/log.csv','a', 0)
ser = serial.Serial('/dev/ttyUSB0', 115200)
ser.flush()

while True:
    sensors = ser.readline().strip().split(",")
    output = ""
    ts = time.time()
    output += str(ts) + ', '
    output += datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    for i in sensors:
        output += ', '
        output += i.strip()
    f.write(output+'\n')
    f.flush()
    print output

f.close()
