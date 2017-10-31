import RPi.GPIO as GPIO
import time
import commands

leds = [11, 13, 19, 21, 23]
# red, green, rgb_red, rgb_green, rgb_blue
duration = 0.5

def delay(n):
	time.sleep(n)

def led(pins, on = True):
	if pins is not list:
		pins = [pins]
	for pin in pins:
		GPIO.output(pin, on)

def blink(pins, count = 0):
	global duration
	if pins is not list:
		pins = [pins]
	for i in range(count):
		for pin in pins:
			GPIO.output(pin, True)
		delay(duration)
		for pin in pins:
			GPIO.output(pin, False)
		delay(duration)

def startup():
	global duration
	GPIO.setmode(GPIO.BOARD)
	for l in leds:
		GPIO.setup(l, GPIO.OUT)
	led(leds[0]) # red light during initialization
	delay(duration)

def shutdown():
	global duration
	led(leds, False)
	led(leds[1]) # green light after initialization
	delay(duration)
	led(leds[1], False)
	GPIO.cleanup()

def writeFile():
	f = open("test.txt", "w")
	f.write("sample words\n")
	f.write(str(time.time()))
	f.close()

def blinkIP():
	ipstr = commands.getoutput("hostname -I")
	octets = [int(i) for i in ipstr.split(".")]
	for octet in octets:
		blink(leds)
		for i in range(octet):
			h = i / 100
			t = (i % 100) / 10
			o = (i % 10)
			blink(leds[2], h)
			blink(leds[1], t)
			blink(leds[0], o)
			blink(leds[2:5])

startup()
writeFile()
blinkIP()
shutdown()