import serial

ser = serial.Serial("/dev/ttyUSB0", baudrate=9600)

while True:
    data = ser.readline().decode()
    val = [float(i) for i in data.split(",")]
    temp, hum, heatIndex, pressure = val 
    