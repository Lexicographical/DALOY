from NRFReader import NRFReader
from WebServer import WebServer
from datetime import datetime
from threading import Thread
import os

class Singleton:
	def __init__(self):
		self.reader = NRFReader()
		self.server = WebServer()
		self.packets = []
		self.packetId = 0

		self.backupSize = 15 # once every 5 mins for 1Hz refresh rate
		self.refreshRate = 1 # 1 Hz
		self.clearCache = False

		relPath = "data/Daloy " + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + ".csv"
		self.fn = os.path.abspath(os.path.join(os.path.join(os.path.abspath(__file__), os.pardir), relPath))
		dataFolder = os.path.abspath(os.path.join(os.path.abspath(self.fn), os.pardir))
		if not os.path.exists(dataFolder):
			os.makedirs(dataFolder)
		file = open(self.fn, "w+")
		file.write("Time (s),Temperature,Humidity,Pressure,Altitude\n")
		file.flush()
		file.close()

	def registerEntry(self, packet):
		if self.clearCache:
			self.packets[:] = []
			self.clearCache = False
		entry = {"id": self.packetId, "temperature": packet[0], "humidity": packet[1], "pressure": packet[2], "altitude": packet[3]}
		self.packets.append(entry)
		# flush cache
		if self.packetId % self.backupSize == 0 and self.packetId > 0:
			thread = Thread(target=self.backupData, args=(self.packets[:],))
			thread.start()
			self.clearCache = True
		self.packetId += 1

	def backupData(self, data):
		print("Backing up")
		file = open(self.fn, "a+")
		for packet in data:
			print(packet)
			info = (packet["id"] * self.refreshRate, packet["temperature"], packet["humidity"], packet["pressure"], packet["altitude"])
			print(info)
			file.write("{},{},{},{},{}\n".format(*info))
		file.flush()
		file.close()


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