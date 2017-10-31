import RPi.GPIO as GPIO
import time
import commands

leds = [11, 13, 23, 21, 19]
# red, green, rgb_blue, rgb_green, rgb_red
duration = 0.5

def delay(n):
	time.sleep(n)

def led(pins, on = True):
	if pins is not list:
		pins = [pins]
	for pin in pins:
		GPIO.output(pin, on)

def runled(pins):
	for pin in pins:
		GPIO.output(pin, True)
		delay(0.2)
	for pin in pins[::-1]:
		GPIO.output(pin, False)
		delay(0.2)

def blink(pins, count = 0):
	global duration
	if pins is not list:
		pins = [pins]
	for i in range(count):
		count = 0
		for pin in pins:
			if count == 0:
				count += 1
				delay(0.2)
			GPIO.output(pin, True)
		delay(duration)
		count = 0
		for pin in pins:
			if count == 0:
				count += 1
				delay(0.2)
			GPIO.output(pin, False)

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
	runled(leds)
	led(leds[0])
	for octet in octets:
		blink(leds)
		h = octet / 100
		t = (octet % 100) / 10
		o = (octet % 10)
		print([h, t, o])
		blink(leds[4], h)
		blink(leds[3], t)
		blink(leds[2], o)
		runled(leds)
		led(leds[0])

startup()
writeFile()
blinkIP()
shutdown()