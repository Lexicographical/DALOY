import RPi.GPIO as GPIO
import time

def led(pins, on = True):
	if pins is not list:
		pins = [pins]
	for pin in pins:
		GPIO.output(pin, on)

def startup():
	GPIO.setmode(GPIO.BOARD)
	for l in leds:
		GPIO.setup(l, GPIO.OUT)

def shutdown():
	led(leds, False)
	GPIO.cleanup()

startup()
cmd = raw_input("Pin & Power: ")
while cmd != "exit":
	pin, power = [int(i) for i in cmd.split(" ")]
	GPIO.output(pin, power)
	cmd = raw_input("Pin & Power: ")