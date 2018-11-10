##########################################
## Python module to read a Wii nunchuck ##
##                                      ##
## Written by Jason - @Boeeerb          ##
##  jase@boeeerb.co.uk                  ##
##########################################
##
## v0.1 03/05/14 - Initital release
## v0.2 21/06/14 - Retrieve one byte at a time [Simon Walters - @cymplecy]
## v0.3 22/06/14 - Minor Refactoring [Jack Wearden - @JackWeirdy]
## v0.32 25/6/14 - XOR each data byte with 0x17 and then add 0x17 to produce corrent values - Simon Walters @cymplecy
## v0.4 26/6/14 - Change method of XOR and add delay parameter - Simon Walters @cymplecy
## v0.41 30/3/15 - Adding support for RPI_REVISION 3 - John Lumley @Jelby-John

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
