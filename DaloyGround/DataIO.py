import os
from datetime import datetime
from threading import Thread

class DataIO:
	def __init__(self):
		self.backupSize = 15 # once every 5 mins for 1Hz refresh rate
		self.refreshRate = 1 # 1 Hz

		relPath = "data/Daloy " + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + ".csv"
		self.fn = os.path.abspath(os.path.join(os.path.join(os.path.abspath(__file__), os.pardir), relPath))
		dataFolder = os.path.abspath(os.path.join(os.path.abspath(self.fn), os.pardir))
		if not os.path.exists(dataFolder):
			os.makedirs(dataFolder)
		file = open(self.fn, "w+")
		file.write("Time (s),Temperature,Humidity,Pressure,Altitude\n")
		file.flush()
		file.close()

	def saveData(self, packets):
		file = open(self.fn, "a+")
		for packet in packets:
			info = (packet["id"] * self.refreshRate, packet["temperature"], packet["humidity"], packet["pressure"], packet["altitude"])
			file.write("{},{},{},{},{}\n".format(*info))
		file.flush()
		file.close()

	def readData(self):
		file = open(self.fn, "r")
		s = file.read()
		return s
