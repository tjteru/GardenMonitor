#!/usr/bin/python
#
#
#
#
#
#

import time, datetime
import serial

from localInfo import *

f = open(logfile,'a', 0)
ser = serial.Serial('/dev/ttyUSB0', 115200)
ser.flush()

while True:
    sensors = ser.readline().strip().split(",")
    if len(sensors) == 13:
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
    else:
        print "Malformed Data encountered...  Ignoring."

f.close()
