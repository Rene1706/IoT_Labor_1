#/bin/bash

cd /home/pi

mkdir Group03
sudo cp -R /home/pi/src /home/pi/Group03/src
sudo chmod -R pi /home/pi/Group03/src
grep -r "AUFGABE" /home/pi/Group03/src

echo 17 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio17/direction
echo 18 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio18/direction

# Abfrage GPIO17
cat /sys/class/gpio/gpio17/value

# Schreiben Value
echo 1 > /sys/class/gpio/gpio17/value
