from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH)
sleep(0.05)
GPIO.output(17, GPIO.LOW)
GPIO.cleanup()
