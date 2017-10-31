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
			delay(0.5)
		delay(duration)
		for pin in pins:
			GPIO.output(pin, False)
			delay(0.5)

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
	print(ipstr)
	octets = [int(i) for i in ipstr.split(".")]
	print(octets)
	for octet in octets:
		blink(leds)
		h = octet / 100
		t = (octet % 100) / 10
		o = (octet % 10)
		print([h, t, o])
		blink(leds[4:1:-1])
		blink(leds[2], h)
		blink(leds[3], t)
		blink(leds[4], o)
		blink(leds[4:1:-1])

startup()
writeFile()
blinkIP()
shutdown()