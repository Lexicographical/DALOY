import RPi.GPIO as GPIO
import time

leds = [11, 13, 19, 21, 23]

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
cmd = raw_input("RGB & Power: ")
while cmd != "exit":
	toks = cmd.split(" ")
	pin = 19
	if toks[0] == "g":
		pin = 21
	elif toks[0] == "b":
		pin = 23
	GPIO.output(pin, int(toks[1]))
	cmd = raw_input("RGB & Power: ")