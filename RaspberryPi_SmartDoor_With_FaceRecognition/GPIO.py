import RPi.GPIO as GPIO
from time import sleep


def GPIO_Unlock(n):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(n, GPIO.OUT)
    while (True):
        GPIO.output(n, 1)
        sleep(1)

def GPIO_Lock(n):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(n, GPIO.OUT)
    while (True):
        GPIO.output(n, 0)
        sleep(1)
