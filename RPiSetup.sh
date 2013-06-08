#!/bin/bash

# Run git clone git://github.com/tjteru/GardenMonitor.git and then run this file from there


echo "Please type the root password to allow apt-get to install packages:"

sudo apt-get install python-setuptools python-mysqldb screen 
sudo easy_install PySerial MySQL-python

git clone git://github.com/kasun/python-tail.git

cd python-tail

sudo python setup.py install

cd ../
rm -rf python-tail/