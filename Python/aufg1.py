import time
import RPi.GPIO as GPIO

LED1= #TODO
LED2= #TODO
GPIO.setmode(GPIO.BMC)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
while True:
    GPIO.output(LED1, 1)
    time.sleep(1)
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 1)
    time.sleep(1)
    GPIO.output(LED2, 0)
