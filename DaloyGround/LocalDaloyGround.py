import RPi.GPIO as GPIO
import time
import commands

leds = [11, 13, 19, 21, 23]
duration = 1
# red, green, rgb_red, rgb_green, rgb_blue

def led(pin, on=True):
    GPIO.output(pin, on)

def blink(pin, duration):
    led(pin)
    time.sleep(duration)
    led(pin, False)
    time.sleep(duration)
    
def blinkMulti(pins, duration):
    for i in pins:
        led(i)
    time.sleep(duration)
    for i in pins:
        led(i, False)
    time.sleep(duration)
    
def blinkNum(pow10, val):
    global duration
    if pow10 == 0:
        # red
        for i in range(val):
            blink(leds[2], duration)
    elif pow10 == 1:
        # green
        for i in range(val):
            blink(leds[3], duration)
    elif pow10 == 2:
        # blue
        for i in range(val):
            blink(leds[4], duration)
    else:
        # anuna
        blink(leds[0], duration)
    # white
    blinkMulti(leds[2:5], duration)

# startup
GPIO.setmode(GPIO.BOARD)
for l in leds:
    GPIO.setup(l, GPIO.OUT)
led(leds[0])
time.sleep(1)

f = open("test.txt", "w")
f.write("sample words\n")
f.write(str(time.time()))
f.close()
ipstr = commands.getoutput("hostname -I")
octets = [int(i) for i in ipstr.split(".")]
for octet in octets:
    blinkMulti(leds, duration)
    for i in range(octet):
        hundreds = i / 100
        tens = (i % 100) / 10
        ones = (i % 10)
        blinkNum(2, hundreds)
        blinkNum(1, tens)
        blinkNum(0, ones)
        
# blink for ip address

led(leds[0], False)
led(leds[1])
time.sleep(1)
led(leds[1], False)
GPIO.cleanup();