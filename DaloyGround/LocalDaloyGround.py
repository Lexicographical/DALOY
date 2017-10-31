import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD
import time
import commands

lcd_rs         = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 8
lcd_d4        = 6
lcd_d5        = 13
lcd_d6        = 19
lcd_d7        = 26
lcd_backlight = 7
lcd = None

duration = 0.5
leds = [17, 27, 11, 9, 10]
# red, green, rgb_blue, rgb_green, rgb_red

def delay(n):
	time.sleep(n)

def led(pin, on = True):
	GPIO.output(pin, on)

def startup():
	global duration, lcd
	for l in leds:
		GPIO.setup(l, GPIO.OUT)
	led(leds[0]) # red light during initialization

	lcd = Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 16, 2, lcd_backlight)
	lcd.clear()
	lcd.message("Initializing...")
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

def showIP():
	ipstr = commands.getoutput("hostname -I")
	print(ipstr)
	lcd.clear()
	lcd.message("IP Address:\n")
	lcd.message(ipstr)
	delay(5)

startup()
writeFile()
showIP()
shutdown()