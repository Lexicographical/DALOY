import NRFReader
import WebServer

class Singleton:
	def __init__(self):
		self.reader = NRFReader.NRFReader()
		self.server = WebServer.WebServer()
		self.packets = []
		self.packetId = 0

	def registerEntry(self, packet):
		entry = {"id": self.packetId, "temperature": packet[0], "humidity": packet[1], "pressure": packet[2], "altitude": packet[3]}
		self.packets.append(entry)
		self.packetId += 1

	def initServer(self):
		self.server.initServer()

	def startListening(self):
		self.reader.start()

	def getLatestEntry(self):
		if len(self.packets) > 0:
			return self.packets[-1]
		else:
			return  {"id": -1, "temperature": 0, "humidity": 0, "pressure": 0, "altitude": 0}

	def getAllEntries(self):
		return self.packets

instance = Singleton()

if __name__ == "__main__":
	print("Start main")
	instance.initServer()
	print("Proceeded")
	instance.startListening()