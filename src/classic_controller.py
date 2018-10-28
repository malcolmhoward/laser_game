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

    def left_joystick(self):
        data = self.read()

    def right_joystick(self):
        data = self.read()

    def left_trigger_pressure(self):
        data = self.read()

    def right_trigger_pressure(self):
        data = self.read()

    def button_a(self):
        data = self.read()
        return data[5] & 0x00

    def button_b(self):
        data = self.read()
        return data[5] & 0x00

    def button_x(self):
        data = self.read()
        return data[5] & 0x00

    def button_y(self):
        data = self.read()
        return data[5] & 0x00

    def button_home(self):
        data = self.read()
        return data[5] & 0x00

    def button_minus(self):
        data = self.read()
        return data[5] & 0x00

    def button_plus(self):
        data = self.read()
        return data[5] & 0x00

    def button_zl(self):
        data = self.read()
        return data[5] & 0x07

    def button_zr(self):
        data = self.read()
        return data[5] & 0x00

    def button_trigger_left(self):
        data = self.read()
        return data[5] & 0x00

    def button_trigger_right(self):
        data = self.read()
        return data[5] & 0x00

    def button_up(self):
        data = self.read()
        return data[5] & 0x00

    def button_down(self):
        data = self.read()
        return data[5] & 0x00

    def button_left(self):
        data = self.read()
        return data[5] & 0x00

    def button_right(self):
        data = self.read()
        return data[5] & 0x00
