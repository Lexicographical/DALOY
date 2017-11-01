import NRFReader
import WebServer

class Singleton:
	def __init__(self):
		self.reader = NRFReader()
		self.server = WebServer()
		self.packets = []

	def registerEntry(self, packet):
		self.packets.append(packet)

	def initServer(self):
		self.server.initServer()

	def getLatestEntry():
		return self.packets[-1]

	def getAllEntries():
		return self.packets


instance = Singleton()
instance.initServer()