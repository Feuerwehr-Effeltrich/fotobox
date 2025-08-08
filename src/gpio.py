# import RPi.GPIO as GPIO
# from time import sleep
import cfg
import serial

# GPIO.cleanup()
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(cfg.gpio_pin, GPIO.OUT)

# def gpio_capture():
#     GPIO.output(cfg.gpio_pin, True)
#     sleep(4)
#     GPIO.output(cfg.gpio_pin, False)

def gpio_capture():
    with serial.Serial(cfg.serial_device, cfg.serial_baud, timeout=1) as ser:
        ser.write(b'c')
        ser.flush()
