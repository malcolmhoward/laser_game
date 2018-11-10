from smbus2 import SMBus
import RPi.GPIO as rpi
import time as time

bus = 0



class WiiController:

    def __init__(self, delay=0.05):
        self.delay = delay
        if rpi.RPI_REVISION == 1:
            i2c_bus = 0
        elif rpi.RPI_REVISION == 2:
            i2c_bus = 1
        elif rpi.RPI_REVISION == 3:
            i2c_bus = 1
        else:
            print("Unable to determine Raspberry Pi revision.")
            exit()
        self.bus = SMBus(i2c_bus)
        self.bus.write_byte_data(0x52, 0x40, 0x00)
        time.sleep(0.1)

    def read(self):
        self.bus.write_byte(0x52, 0x00)
        time.sleep(self.delay)
        temp = [(0x17 + (0x17 ^ self.bus.read_byte(0x52))) % 256 for i in range(6)]
        return temp
