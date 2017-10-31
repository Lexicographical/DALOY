from flask import Flask
import json
from nrf24 import NRF24
from threading import Thread

appname = "Daloy"
uuid = 0xCB15CA;

instance = Singleton()
instance.initServer()

class Singleton:
	def __init__(self):
		self.reader = NRFReader()
		self.server = WebServer()

	def initServer(self):
		self.server.initServer()

class NRFReader:
	def __init__(self):
		self.radio = NRF24()
		radio = NRF24()
		radio.begin(1,0,"P9_23", "P9_24") #Set CE and IRQ pins
		radio.setRetries(15,15)
		radio.setPayloadSize(32)
		radio.setChannel(0x60)
		radio.setDataRate(NRF24.BR_250KBPS)
		radio.setPALevel(NRF24.PA_MAX)
		radio.openReadingPipe(1, uuid)

	def run(self):
		print("Hello")

	def start(self):
		thread = Thread(target=self.run)
		thread.start()



class WebServer:
	def __init__(self):
		self.app = Flask(appname)

	def initServer(self):
		global instance
		@app.route("/")
		def index():
			return "Hello";

temp, hum, pressure, alt = 27.3, 77.5, 986.3, 101.9
app = Flask("Daloy")


@app.route("/")
def hello():
	global alt
	alt += 1
	return json.dumps({"temperature": temp, "humidity": hum, "pressure": pressure, "altitude": alt});

# if __name__ == "__main__":
# 	app.run(host = "127.0.0.1")