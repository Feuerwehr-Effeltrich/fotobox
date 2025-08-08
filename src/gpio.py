import RPi.GPIO as GPIO
from time import sleep
import cfg

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(cfg.gpio_pin, GPIO.OUT)

def gpio_capture():
    GPIO.output(cfg.gpio_pin, True)
    sleep(4)
    GPIO.output(cfg.gpio_pin, False)
