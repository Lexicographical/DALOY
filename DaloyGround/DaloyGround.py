from DataReader import HanginReader, TubigCommunicator
from WebServer import WebServer
from DataIO import DataIO
from threading import Thread
import os

HANGIN = 0
TUBIG = 1

class Singleton:
	def __init__(self):
		self.hangin = HanginReader()
		self.tubig = TubigCommunicator()
		self.server = WebServer()
		self.io = DataIO()

		self.backupSize = 15 # once every 5 mins for 1Hz refresh rate
		self.refreshRate = 1 # 1 Hz
		self.clear = [False, False]
		self.packetId = [0, 0]
		self.packets = [[], []]


	def clearCache(self, type):
		self.packets[type][:] = []

	def registerEntry(self, packet, type):
		if self.clear[type]:
				self.clearCache(type)
				self.clear[type] = False
		if type == HANGIN:
			entry = {"id": self.packetId[type], "temperature": packet[0], "humidity": packet[1], "pressure": packet[2], "altitude": packet[3]}
			self.packets[type].append(entry)
			# flush cache
		elif type == TUBIG:
			entry = {"id": self.packetId[type], "temperature": packet[0], "abs_pressure": packet[1], "pH": packet[2]}
			self.packets[type].append(entry)
		for i in range(2):
			if len(self.packets[i]) == self.backupSize and self.packetId > 0:
					thread = Thread(target=self.io.saveData, args=(tyself.packets))
					thread.start()
					self.clear[type] = True
		self.packetId[type] += 1

	def initServer(self):
		self.server.initServer()

	def startListening(self):
		self.hangin.start()
		self.tubig.start()

	def getLatestEntry(self, type):
		if len(self.packets[type]) > 0:
			return self.packets[type][-1]
		else:
			if type == HANGIN:
				return  {"id": -1, "temperature": 0, "humidity": 0, "pressure": 0, "altitude": 0}
			elif type == TUBIG:
				return {"id": -1, "temperature": 0, "abs_pressure": 0, "pH": 0}

	def getAllEntries(self, type):
		self.io.saveData(type, self.packets[:])
		csv = self.io.readData(type)
		return csv

instance = Singleton()
if __name__ == "__main__":
	instance.initServer()
	instance.startListening()
