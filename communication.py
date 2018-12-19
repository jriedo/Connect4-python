import serial
import time
import numpy as np


class ArduinoCommunication:
    def __init__(self):
        self.ser = serial.Serial('com5', 9600)
        time.sleep(3)
        self.drop(0)

    def drop(self, pos):
        pos = str(pos)
        self.ser.write(pos.encode())
        return self.ser.read(1).decode("utf-8")

    def open(self):
        self.ser.write(b'8')
        return self.ser.read(1).decode("utf-8")

    def close(self):
        self.ser.write(b'9')
        return self.ser.read(1).decode("utf-8")


if __name__ == '__main__':
    ac = ArduinoCommunication()



    for i in np.arange(1, 8):
        print(ac.drop(i))


