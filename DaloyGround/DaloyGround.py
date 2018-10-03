from DataReader import Reader
from WebServer import WebServer
from DataIO import DataIO
from threading import Thread
import os

class Singleton:
	def __init__(self):
		self.reader = Reader()
		self.server = WebServer()
		self.io = DataIO()
		self.packets = []
		self.packetId = 0
		self.clear = False
		self.backupSize = 15 # once every 5 mins for 1Hz refresh rate
		self.refreshRate = 1 # 1 Hz

	def clearCache(self):
		self.packets[:] = []

	def registerEntry(self, packet):
		if self.clear:
			self.clearCache()
			self.clear = False
		entry = {"id": self.packetId, "temperature": packet[0], "humidity": packet[1], "pressure": packet[2], "altitude": packet[3]}
		self.packets.append(entry)
		# flush cache
		if len(self.packets) == self.backupSize and self.packetId > 0:
			thread = Thread(target=self.io.saveData, args=(self.packets[:],))
			thread.start()
			self.clear = True
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
		self.io.saveData(self.packets[:])
		csv = self.io.readData()
		return csv

instance = Singleton()
if __name__ == "__main__":
	instance.initServer()
	instance.startListening()