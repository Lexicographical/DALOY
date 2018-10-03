import serial
import DaloyGround
import time
from threading import Thread

class Reader:
    def __init__(self):
        self.reader = serial.Serial("/dev/ttyUSB0", baudrate=9600)
        print("Initialized XBee Reader")

    def run(self):
        while True:
            if self.reader.available():
                data = self.reader.readline().decode()
                val = [float(i) for i in data.split(",")]
                DaloyGround.instance.registerEntry(tuple(val))
                time.sleep(0.3)

    def start(self):
        thread = Thread(target=self.run)
        thread.start()
