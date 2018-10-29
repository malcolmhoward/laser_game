# links:
# data http://wiibrew.org/wiki/Wiimote/Extension_Controllers/Classic_Controller
# C++ code https://github.com/dmadison/WiiChuck/tree/master/src

try:
    from smbus import SMBus
except ImportError:
    from smbus2 import SMBus
import RPi.GPIO as rpi
import time as time


class ClassicController:

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
        temp = [(0x17 + (0x17 ^ self.bus.read_byte(0x52))) for _ in range(6)]
        return temp

    """
    ANALOGS
    """
    def left_joystick(self):
        data = self.read()
        return data[0] & 0x3F, data[1] & 0x3F

    def right_joystick(self):
        data = self.read()
        bit_0 = (data[2] & 0x80) >> 7
        bit_12 = (data[1] & 0xC0) >> 5
        bit_34 = (data[0] & 0xC0) >> 3
        return bit_0 + bit_12 + bit_34, data[2] & 0x1F

    def left_trigger_pressure(self):
        data = self.read()
        bit_02 = (data[3] & 0xE0) >> 5
        bit_34 = (data[3] & 0x60) >> 2
        return bit_02 + bit_34

    def right_trigger_pressure(self):
        data = self.read()
        return data[3] & 0x1F

    """
    BYTE 5
    """
    def button_zl(self):
        data = self.read()
        return data[5] & 0x80 == 0

    def button_b(self):
        data = self.read()
        return data[5] & 0x40 == 0

    def button_y(self):
        data = self.read()
        return data[5] & 0x20 == 0

    def button_a(self):
        data = self.read()
        return data[5] & 0x10 == 0

    def button_x(self):
        data = self.read()
        return data[5] & 0x08 == 0

    def button_zr(self):
        data = self.read()
        return data[5] & 0x04 == 0

    def button_left(self):
        data = self.read()
        return data[5] & 0x02 == 0

    def button_up(self):
        data = self.read()
        return data[5] & 0x01 == 0

    """
    BYTE 4
    """
    def button_right(self):
        data = self.read()
        return data[4] & 0x80 == 0

    def button_down(self):
        data = self.read()
        return data[4] & 0x40 == 0

    def button_trigger_left(self):
        data = self.read()
        return data[4] & 0x20 == 0

    def button_minus(self):
        data = self.read()
        return data[4] & 0x10 == 0

    def button_home(self):
        data = self.read()
        return data[4] & 0x08 == 0

    def button_plus(self):
        data = self.read()
        return data[4] & 0x04 == 0

    def button_trigger_right(self):
        data = self.read()
        return data[4] & 0x02 == 0
