GardenMonitor
=============

A system for monitoring a garden with many sensors

Currently we use a ChipKit Uno (Arduino like) board to collect data from a set os sensors installed in the garden.  
This is, in turn, connected to a Raspberry Pi (or eventually a BeagleBone) which parses the data and stuffs it into 
a MySQL database.  This database is updated everytime there is a new sample from the sensors.  The data is then 
displayed on a webpage using HighCharts, which can show the data updating live.
