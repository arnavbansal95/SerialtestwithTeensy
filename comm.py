from sys import getsizeof
import serial

import serial.tools.list_ports as SerialPorts


class CommModule:
    def __init__(self):
        self.devDescription = "USB Serial Device"
        self.serialPort = self.get_comport(self.devDescription)
        self.serial = None
        self.bytes_recv = None

    def setUp(self):
        self.serial = serial.Serial(self.serialPort, 9600, timeout=10)
        if self.serial.isOpen():
            print("Connected to {} on Port: {}".format(self.devDescription, self.serialPort))

    def tearDown(self):
        if self.serial.isOpen():
            self.serial.close()
            if self.serial.isOpen() != True:
                print("Disconnected {} on Port: {}".format(self.devDescription, self.serialPort))

    def get_comport(self, devDesc):
        port = None
        for i in list(SerialPorts.comports()):
            if devDesc in i.description:
                port = str(i.description).split("(")
                port = port[1].rstrip(")")
        return port

    def write(self, payload):
        if self.serial.isOpen():
            self.serial.write(payload)
            print("Wrote {} bytes".format(getsizeof(payload)))
        else:
            print("Serial Port not Open!")

    def read(self):
        bytes_recv = None
        if self.serial.isOpen():
            while self.serial.in_waiting == 0:
                pass
            bytes_in = self.serial.in_waiting
            bytes_recv = self.serial.read(bytes_in)
        return bytes_recv
