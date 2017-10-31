import NRFReader
import WebServer


class Singleton:
	def __init__(self):
		self.reader = NRFReader()
		self.server = WebServer()

	def initServer(self):
		self.server.initServer()

instance = Singleton()
instance.initServer()