#/bin/bash

while true
do
  echo "GPIO17 1"
  #echo 1 > /sys/class/gpio/gpio17/value
  sleep 1
  echo "GPIO17 0"
  #echo 0 > /sys/class/gpio/gpio17/value
  echo "GPIO18 1"
  #echo 1 > /sys/class/gpio/gpio18/value
  sleep 1
  echo "GPIO18 0"
  #echo 0 > /sys/class/gpio/gpio18/value
done
