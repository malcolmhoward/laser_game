##########################################
## Python module to read a Wii nunchuck ##
##                                      ##
## Written by Jason - @Boeeerb          ##
##  jase@boeeerb.co.uk                  ##
##########################################
"""
DATA
      Bit
Byte |  7 |  6 |  5 |  4 |  3 |	 2 | 1  | 0  |
0    |                SX<7:0>                |
1    |                SY<7:0>                |
2    |                AZ<9:2>                |
3    |                AY<9:2>                |
4    |                AZ<9:2>                |
5    | AZ<1:0> | AY<1:0> | AX<1:0> | BC | BZ |
"""

from .wii_controller import WiiController

class Nunchuk(WiiController):

    def __init__(self, delay=0.05):
        super().__init__(delay)

    def raw(self):
        data = self.read()
        return data

    def joystick(self):
        data = self.read()
        return data[0], data[1]

    def accelerometer(self):
        data = self.read()
        return data[2], data[3], data[4]

    def button_c(self):
        data = self.read()
        butc = (data[5] & 0x02)

        return butc == 0

    def button_z(self):
        data = self.read()
        butc = (data[5] & 0x01)

        return butc == 0

    def joystick_x(self):
        data = self.read()
        return data[0]

    def joystick_y(self):
        data = self.read()
        return data[1]

    def accelerometer_x(self):
        data = self.read()
        return data[2]

    def accelerometer_y(self):
        data = self.read()
        return data[3]

    def accelerometer_z(self):
        data = self.read()
        return data[4]

    def set_delay(self, delay):
        self.delay = delay

    @staticmethod
    def scale(value, _min, _max, _omin, _omax):
        return (value - _min) * (_omax - _omin) // (_max - _min) + _omin
