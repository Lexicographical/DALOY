import os
from datetime import datetime
from threading import Thread

class DataIO:
	def __init__(self):
		self.backupSize = 15

		hRP = "data/DaloyHangin_" + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".csv"
		tRP = "data/DaloyTubig_" + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".csv"
		self.fn = []
		self.fn[0] = os.path.abspath(os.path.join(os.path.join(os.path.abspath(__file__), os.pardir), hRP))
		self.fn[1] = os.path.abspath(os.path.join(os.path.join(os.path.abspath(__file__), os.pardir), tRP))
		dataFolder = os.path.abspath(os.path.join(os.path.abspath(self.fn[0]), os.pardir))
		if not os.path.exists(dataFolder):
			os.makedirs(dataFolder)

		hFile = open(self.fn[0], "w+")
		hFile.write("ID,Temperature,Humidity,Pressure,Altitude\n")
		hFile.flush()
		hFile.close()

		tFile = open(self.fn[1], "w+")
		tFile.write("ID,Temperature,AbsolutePressure,pH\n")
		tFile.flush()
		tFile.close()

	def saveData(self, type, packets):
		file = open(self.fn[type], "a+")
		for packet in packets[type]:
			# hanginPacket if type == 0 else tubigPacket
			info = (packet["id"], packet["temperature"], packet["humidity"], packet["pressure"], packet["altitude"]) if type == 0 else (packet["id"], packet["temperature"], packet["abs_temperature"], packet["rel_temperature"], packet["pH"])
			file.write(("{},{},{},{},{}\n" if type == 0 else "{},{},{},{}\n").format(*info))
		file.flush()
		file.close()

	def readData(self, type):
		file = open(self.fn[type], "r")
		s = file.read()
		return s
