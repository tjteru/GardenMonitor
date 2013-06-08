#!/bin/bash

# Run git clone git://github.com/tjteru/GardenMonitor.git and then run this file from there

echo "WARNING: This is currently broken... Do not use.  Hit control+c within the next 5 sec to cancel."

sleep 5

echo "Continuing..."

sleep 2

opkg update
opkg install libftdi ntp ntpdate python-pyserial git

rm /etc/localtime

ln -s /usr/share/zoneinfo/America/Los_Angeles /etc/localtime

# This does not work for some unknown reason
/etc/init.d/ntpd stop
ntpdate pool.ntp.org
/etc/init.d/ntpd start