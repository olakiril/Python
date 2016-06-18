
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN)

class licked:
    """ this class handles the licks
    """

    def __init__(self):
        self.prev_input = 0

    def lick(self):
        input = GPIO.input(26)
        # if (not self.prev_input) and input:
        #    return True
        #else:
        #    return False
        self.prev_input = input
        if input:
            return True
        else:
            return False


