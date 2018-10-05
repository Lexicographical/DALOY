import serial
import time
from threading import Thread

class HanginReader:
    def __init__(self, debug=False):
        self.reader = serial.Serial("/dev/ttyUSB0", baudrate=9600)
        print("Initialized Hangin Reader. Debug:", debug)
        self.debug = debug

    def run(self):
        while True:
            data = self.reader.readline().decode()
            try:
                val = [float(i) for i in data.split(",")]
                if self.debug:
                    print(val)
                else:
                    import DaloyGround
                    DaloyGround.instance.registerEntry(tuple(val), type=0)
            except ValueError:
                print("Non-numeric text detected! Text: ", data)
            time.sleep(0.3)

    def start(self):
        thread = Thread(target=self.run)
        thread.start()

class TubigCommunicator:
    def __init__(self):
        self.reader = serial.Serial("/dev/ttyAMA0", baudrate = 9600)
        print("Initialized Tubig Reader.")

    def run(self):
        while True:
            data = self.reader.readline().decode()
            try:
                val = [float(i) for i in data.split(",")]
                import DaloyGround
                DaloyGround.instance.registerEntry(tuple(val), type=1)
            except ValueError:
                print("Non-numeric text detected! Text: ", data)
            time.sleep(0.3)

    def start(self):
        thread = Thread(target=self.run)
        thread.start()

if __name__ == "__main__":
    reader = HanginReader(debug=True)
    reader.start()
