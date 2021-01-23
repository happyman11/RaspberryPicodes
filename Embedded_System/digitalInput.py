import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

switch = 18
GPIO.setup(switch,GPIO.IN,pull_up_down = GPIO.PUD_UP)

while True:
		if(GPIO.input(switch) == 0):
				print("Sensor detected")

