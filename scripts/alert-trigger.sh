#!/bin/sh

#This shell script triggers the python script with the change in the number of entries in the alert file (snort logs).
#Keep both scripts in /etc/snort directory.

#Get current line count
LINES='sudo wc -l /var/log/snort/alert | tr -d -c 0-9'

while [ true ]
do
NEWCOUNT='sudo wc -l /var/log/snort/alert | tr -d -c 0-9'  #Get new line count
if [ $LINES != $NEWCOUNT ]
  then
    DIFF='expr $NEWCOUNT - $LINES'        #Get the difference
    LINES=$NEWCOUNT                       #Set the line count to the new count
    ./prevention.py
    sleep 20                              #Sleeps for 20 seconds
fi
done
