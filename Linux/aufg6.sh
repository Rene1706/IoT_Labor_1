#/bin/bash

#echo 2 > /sys/class/gpio/export
#echo in > /sys/class/gpio/gpio2/direction

while true
do
  #tasterOutput=(cat /sys/class/gpio/gpio2/value)
  testOutput="0"
  echo "Taster Output: ${testOutput}"
  sleep 1
done

