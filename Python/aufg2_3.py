import threading
import time
import RPi.GPIO as GPIO
import random

class LED(threading.Thread):
    def __init__(self, pin, freq=100):
        threading.Thread.__init__(self)
        self.pin = pin
        self.freq = freq
        self.running = False
        self.sleepTime = 1/freq/2

        GPIO.setmode(GPIO.BMC)
        GPIO.setup(self.pin, GPIO.OUT)

        self.start()

    def run(self):
        self.running = True
        while self.running:
            GPIO.output(self.pin, 1)
            time.sleep(self.sleepTime)
            GPIO.output(self.pin, 0)
            time.sleep(self.sleepTime)

    def stop(self):
        self.running = False
        GPIO.cleanup()

# Could also be done via polling the Button as LED's are already thread
class Button(threading.Thread):
    def __init__(self, pin, led_threads):
        threading.Thread.__init__(self)
        self.pin = pin
        self.led_threads = led_threads
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def run(self):
        while True:
            button_state = GPIO.input(self.pin)
            if button_state == GPIO.LOW:
                new_freq = random.randint(1, 10)
                for led_thread in self.led_threads:
                    led_thread.freq = new_freq
                    print(f"Changed LED {led_thread.pin} frequency to {new_freq}")
                time.sleep(0.5)

    def stop(self):
        GPIO.cleanup()

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


