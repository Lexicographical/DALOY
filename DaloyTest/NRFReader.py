from threading import Thread
from struct import *
import random
import time

class NRFReader:
	def run(self):
		while True:
			import DaloyGround
			packet = (random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10))
			DaloyGround.instance.registerEntry(packet)
			time.sleep(0.5)

	def start(self):
		thread = Thread(target=self.run)
		thread.start()