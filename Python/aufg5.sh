#/bin/bash
/home/pi/PiBits/ServoBlaster/user/servod
# Start GPIO17, GPIO18 at pin 11,12
echo 0=0%% > /dev/servoblaster        # Specify as a percentage\n"
echo 0=25%% > /dev/servoblaster
echo 0=50%% > /dev/servoblaster
echo 0=75%% > /dev/servoblaster
echo 0=100%% > /dev/servoblaster
# -min={N|Nus|N%%}    specifies the minimum allowed pulse width, default\n"
# DEFAULT MID --> #define DEFAULT_SERVO_MIN_US	500
# DEFAULT MAX 2500