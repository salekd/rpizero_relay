# -*- coding: utf-8-*-
import re
import RPi.GPIO as GPIO
import os

WORDS = ["LIGHT", "LIGHTS"]


def handle(text, mic, profile):
    """
        Responds to the keyword 'light' by switching on/off GPIO pins
        connected to a light, for example through a relay.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    print("Light")
    os.system('if [ `cat /sys/class/gpio/gpio18/value` -eq "0" ]; then echo "1" > /sys/class/gpio/gpio18/value; else echo "0" > /sys/class/gpio/gpio18/value; fi')


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    #return True
    return bool(re.search(r'\blight\b', text, re.IGNORECASE))
