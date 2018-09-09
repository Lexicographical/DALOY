import time
import Adafruit_SSD1306
import commands
from threading import Thread, Event

from PIL import Image, ImageDraw, ImageFont

RST = 24
dsp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3c)

dsp.begin()
dsp.clear()
dsp.display()

w, h = dsp.width, dsp.height
font = ImageFont.truetype("res/PNova.ttf", 17)
fontIP = ImageFont.truetype("res/PNova.ttf", 17)
image = Image.new('1', (w, h))
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, w, h), outline=0, fill=0)

class Looper(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        global draw, dsp, image, font
        while not self.stopped.wait(5):
            ip = commands.getoutput("hostname -I")
            draw.text((0, 0), "IP Address", font=font, fill=255)
            draw.text((0, 20), ip, font=fontIP, fill=255)

            dsp.image(image)
            dsp.display()

stopFlag = Event()
thread = Looper(stopFlag)
thread.start()