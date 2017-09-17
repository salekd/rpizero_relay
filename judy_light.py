import judy
import os
import re
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# Set GPIO 18 for output.
GPIO.setup(18, GPIO.OUT)
#os.system('echo "18" > /sys/class/gpio/export')
#os.system('echo "out" > /sys/class/gpio/gpio18/direction')

# Use USB microphone and
# specify the Pocketshpinx dictionary for the speech recognition.
vin = judy.VoiceIn(adcdev='plughw:0,0',
                   lm='7369.lm',
                   dict='7369.dic')

# Audio output configuration is needed by Judy.
# Nothing will be heard from Raspberry Pi Zero unless
# additional sound devices are used.
vout = judy.VoiceOut(device='plughw:1,0',
                     resources='/home/pi/judy/resources/audio')

def handle(phrase):
    """
    Process the phrase recognized by Pocketsphinx.
    Toggle the relay switch connected to GPIO 18 when 'light' is said.

    """
    print('Heard: {}'.format(phrase))

    #os.system('if [ `cat /sys/class/gpio/gpio18/value` -eq "0" ]; then echo "1" > /sys/class/gpio/gpio18/value; else echo "0" > /sys/class/gpio/gpio18/value; fi')
    if bool(re.search(r'\blight on\b', phrase, re.IGNORECASE)):
        #os.system('echo "1" > /sys/class/gpio/gpio18/value')
        GPIO.output(18, GPIO.HIGH)
    if bool(re.search(r'\blight off\b', phrase, re.IGNORECASE)):
        #os.system('echo "0" > /sys/class/gpio/gpio18/value')
        GPIO.output(18, GPIO.LOW)

try:
    # Call "Judy" to get her attention, then say something (within the vocabulary).
    judy.listen(vin, vout, handle)
except KeyboardInterrupt:
    # Release the GPIO pin.
    #os.system('udo echo "18" > /sys/class/gpio/unexport')
    GPIO.cleanup()
