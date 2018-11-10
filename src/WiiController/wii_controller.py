from cachetools import TTLCache, cached
from smbus2 import SMBus
import RPi.GPIO as rpi
import time as time


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
            raise OSError("Unable to determine Raspberry Pi revision.")
        self.bus = SMBus(i2c_bus)
        self.bus.write_byte_data(0x52, 0x40, 0x00)
        time.sleep(0.1)

    @cached(TTLCache(maxsize=1, ttl=0.0166))
    def read(self):
        self.bus.write_byte(0x52, 0x00)
        time.sleep(self.delay)
        return [(0x17 + (0x17 ^ self.bus.read_byte(0x52))) % 256 for _ in range(6)]
