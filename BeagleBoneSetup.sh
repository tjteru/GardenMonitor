#!/bin/bash

# run git clone git://github.com/tjteru/GardenMonitor.git and then run this file from there

opkg update
opkg install libftdi ntp ntpdate python-pyserial git

rm /etc/localtime

ln -s /usr/share/zoneinfo/Australia/Sydney /etc/localtime
/etc/init.d/ntpd stop
ntpdate pool.ntp.org
/etc/init.d/ntpd start

cd ~/GardenMonitor/BeagleBone/
python main.py