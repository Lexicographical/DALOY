import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD
import time
import commands

lcd = Adafruit_CharLCD()
duration = 0.5
leds = [11, 13, 23, 21, 19]
# red, green, rgb_blue, rgb_green, rgb_red

def delay(n):
	time.sleep(n)

def led(pin, on = True):
	GPIO.output(pin, on)

def startup():
	global duration
	lcd.begin(16,2)
	lcd.clear()
	lcd.message("Initializing...")
	GPIO.setmode(GPIO.BOARD)
	for l in leds:
		GPIO.setup(l, GPIO.OUT)
	led(leds[0]) # red light during initialization
	delay(duration)

def shutdown():
	global duration
	lcd.clear()
	lcd.message("Shutdown...")
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

def showIP():
	ipstr = commands.getoutput("hostname -I")
	print(ipstr)
	lcd.clear()
	lcd.message("IP Address:\n")
	lcd.message(ipstr)

startup()
writeFile()
showIP()
shutdown()