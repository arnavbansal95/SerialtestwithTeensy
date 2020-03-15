from comm import CommModule
from ctypes import *


class floorPos_t(Structure):
    _pack_ = 1
    _fields_ = [('prev', c_uint8), ('curr', c_uint8), ('dest', c_uint8), ('dirc', c_uint8)]

    def __repr__(self):
        return 'PREV: {} \nCURR: {} \nDEST: {} \nDIRC: {}'.format(self.prev, self.curr, self.dest, self.dirc)

if __name__ == "__main__":
    CommObj = CommModule()
    CommObj.setUp()
    CommObj.write(b"Hello World!")
    readBuffer = CommObj.read()
    readData = floorPos_t.from_buffer(bytearray(readBuffer))
    print(readData)
    CommObj.tearDown()
