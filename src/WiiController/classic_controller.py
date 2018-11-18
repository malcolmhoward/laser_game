# links:
# data http://wiibrew.org/wiki/Wiimote/Extension_Controllers/Classic_Controller
# C++ code https://github.com/dmadison/WiiChuck/tree/master/src

"""
DATA
      Bit
Byte |    7    | 6   |	5  | 4  | 3  |	2  | 1   |	0  |
0    |    RX<4:3>    |             LX<5:0>             |
1    |    RX<2:1>    |             LY<5:0>             |
2    |  RX<0>  |  LT<4:3>  |          RY<4:0>          |
3    |       LT<2:0>       |          RT<4:0>          |
4    |   R     |  D  | LT  | -  | H  |  +  | RT  |     |
5    |   ZL    |  B  |  Y  |  A |  X |  ZR |  L  |  U  |
"""

from .wii_controller import WiiController


class ClassicController(WiiController):

    def __init__(self, delay=0.05):
        super().__init__(delay)

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
