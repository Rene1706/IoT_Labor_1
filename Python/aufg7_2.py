import threading
import time
from math import sin, pi
import RPi.GPIO as GPIO
from servoblaster_ctl import set_pulse_width
import random
# Doing the PWM with our created servoblaster_ctl module

class LED(threading.Thread):
    def __init__(self, pin, freq=100):
        threading.Thread.__init__(self)
        self.pin = pin
        self.freq = freq
        self.running = False
        self.sleepTime = 1/self.freq/100

        set_pulse_width(self.pin, 0) # set initial duty cycle to 0

        self.start()

    def run(self):
        self.running = True
        while self.running:
            for i in range(0, 360):
                duty_cycle = (sin(i * pi / 180) + 1) / 2 # calculate duty cycle as sinusoidal function
                set_pulse_width(self.pin, int(duty_cycle * 100)) # set duty cycle as a percentage
                time.sleep(self.sleepTime)

    def stop(self):
        self.running = False

# Could also be done via polling the Button as LED's are already thread
class Button(threading.Thread):
    def __init__(self, pin, led_threads):
        threading.Thread.__init__(self)
        self.pin = pin
        self.led_threads = led_threads

        self.running = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def run(self):
        self.running = True
        while self.running:
            button_state = GPIO.input(self.pin)
            if button_state == GPIO.LOW:
                new_freq = random.randint(1, 10)
                for led_thread in self.led_threads:
                    led_thread.freq = new_freq
                    led_thread.sleepTime = 1/led_thread.freq/100 # update sleep time based on new frequency
                    print(f"Changed LED {led_thread.pin} frequency to {new_freq}")
                time.sleep(0.5)

    def stop(self):
        self.running = False

# create two LED threads
led_thread1 = LED(pin=17)
led_thread2 = LED(pin=18)

# create a button thread
button_thread = Button(pin=2, led_threads=[led_thread1, led_thread2])

# start all threads
led_thread1.start()
led_thread2.start()
button_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # stop all threads and cleanup GPIO
    led_thread1.stop()
    led_thread2.stop()
    button_thread.stop()
    GPIO.cleanup()
