import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN)
prev_input = 0
while True:
	input = GPIO.input(26)
	if ((not prev_input) and input):
		print("LICK")
	prev_input = input
	time.sleep(0.05)
