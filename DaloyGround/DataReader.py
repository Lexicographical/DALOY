import serial
import time
from threading import Thread

class Reader:
    def __init__(self, debug):
        self.reader = serial.Serial("/dev/ttyUSB0", baudrate=9600)
        print("Initialized XBee Reader")
        self.debug = debug

    def run(self):
        while True:
            data = self.reader.readline().decode()
            try:
            	val = [float(i) for i in data.split(",")]
		if self.debug:
                	print(val)
            	else:
                	import Constants
                	Constants.instance.registerEntry(tuple(val))
            except ValueError:
                print("Non-numeric text detected! Text: ", data)
            
            time.sleep(0.3)

    def start(self):
        thread = Thread(target=self.run)
        thread.start()

if __name__ == "__main__":
    reader = Reader(debug=True)
    reader.start()