#/bin/bash
/home/pi/PiBits/ServoBlaster/user/servod
# Start GPIO17, GPIO18 at pin 11,12
echo 1=100 > dev/servoblaster
echo 2=100 > dev/servoblaster