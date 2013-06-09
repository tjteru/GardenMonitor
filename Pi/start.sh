#!/bin/bash

# Put this line in crontab with crontab -e
# @reboot sleep 30 && /Full/Path/To/GardenMonitor/Pi/start.sh


screen -dmS GetData /home/pi/GardenMonitor/Pi/GetData.py


screen -dmS PushData /home/pi/GardenMonitor/Pi/PushData-incremental.py


