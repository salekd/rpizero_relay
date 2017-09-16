import judy
import os

vin = judy.VoiceIn(adcdev='plughw:0,0',
                   lm='/home/pi/judy/resources/lm/0931.lm',
                   dict='/home/pi/judy/resources/lm/0931.dic')

vout = judy.VoiceOut(device='plughw:1,0',
                     resources='/home/pi/judy/resources/audio')

def handle(phrase):
    print 'Heard:', phrase
    os.system('if [ `cat /sys/class/gpio/gpio18/value` -eq "0" ]; then echo "1" > /sys/class/gpio/gpio18/value; else echo "0" > /sys/class/gpio/gpio18/value; fi')

judy.listen(vin, vout, handle)
