from nrf24 import NRF24
from threading import Thread


uuid = 0xCB15CA;

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