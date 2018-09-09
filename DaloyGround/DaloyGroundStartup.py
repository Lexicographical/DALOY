import time
import Adafruit_SSD1306

from PIL import Image, ImageDraw, ImageFont

RST = 24
dsp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3c)

dsp.begin()
dsp.clear()
dsp.display()

w, h = dsp.width, dsp.height

image = Image.new('1', (w, h))
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, w, h), outline=0, fill=0)

font = ImageFont.truetype("res/PNova.ttf", 12)
draw.text((5, 5), "Hello", font=font, fill=255)
draw.text((5, 25), "World!", font=font, fill=255)

dsp.image(image)
dsp.display()