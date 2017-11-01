import DaloyGround
from nrf24 import NRF24
from threading import Thread
from struct import *

uuid = 0xCB15CA;
Packet = namedtuple("Packet", ["temperature", "humidity", "pressure", "altitude"])


class NRFReader:
	def __init__(self):
		self.radio = NRF24()
		self.radio.begin(1, 0, "P8_23", "P8_24")

		self.radio.setRetries(3, 5)

		self.radio.setPayloadSize(32)
		self.radio.setChannel(0x60)
		self.radio.setDataRate(NRF24.BR_250KBPS)
		self.radio.setPALevel(NRF24.PA_MAX)

		self.radio.setAutoAck(1)
		self.radio.openReadingPipe(1, uuid)

		self.radio.startListening()
		self.radio.stopListening()
		self.radio.printDetails()

	def run(self):
		radio.startListening()
		while True:
			pipe = [0]
			while not radio.available(pipe):
				time.sleep(10000/1000000.0)
			recv_buffer = []
			radio.read(recv_buffer, radio.getDynamicPayloadSize())
			packet = unpack("<ffff", recv_buffer)
			DaloyGround.instance.registerEntry(packet)
			DaloyGround.instance.update();
			print recv_buffer

	def start(self):
		thread = Thread(target=self.run)
		thread.start()