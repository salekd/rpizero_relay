import judy
import re
import RPi.GPIO as GPIO
from pathlib import Path

GPIO.setmode(GPIO.BCM)
# Set GPIO 18 for output.
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH)

file_path = Path(__file__).resolve().parent

# Use USB microphone and
# specify the Pocketshpinx dictionary for the speech recognition.
vin = judy.VoiceIn(adcdev='plughw:0,0',
                   lm=str(file_path / '7369.lm'),
                   dict=str(file_path /'7369.dic'))

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

    if bool(re.search(r'\blight on\b', phrase, re.IGNORECASE)):
        GPIO.output(18, GPIO.LOW)
    if bool(re.search(r'\blight off\b', phrase, re.IGNORECASE)):
        GPIO.output(18, GPIO.HIGH)

try:
    # Call "Judy" to get her attention, then say something (within the vocabulary).
    judy.listen(vin, vout, handle)
except KeyboardInterrupt:
    # Release the GPIO pin.
    GPIO.cleanup()
