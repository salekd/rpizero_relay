from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)

try:  
    while True:
        GPIO.wait_for_edge(14, GPIO.FALLING)  
        # If we are here, an edge was recognized
        # Debounce for 200 ms
        sleep(0.2)
        # Only react to valid edges
        if GPIO.input(18) == 0:
            GPIO.output(18, not GPIO.input(18))
            sleep(1)
              
except KeyboardInterrupt:  
    # Clean up GPIO on CTRL+C exit  
    GPIO.cleanup()
