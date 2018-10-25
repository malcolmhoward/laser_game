from .nunchuck import nunchuck
from .turret import Turret


class Player:

    # Range of the Nunchuk's analog stick
    nun_min = 45
    nun_max = 255
    nun_center = 174

    def __init__(self, bound: int, pwm, turret: Turret,
                 no_x: bool=False, no_y: bool=False):
        self.bound = bound
        self.x_servo_center = turret.x_center
        self.y_servo_center = turret.y_center
        self.turret = turret
        self.pwm = pwm
        self.x_pin = turret.x_pin
        self.y_pin = turret.y_pin
        self.no_x = no_x
        self.no_y = no_y
        # Calculate the values for y = mx + b
        # x needs to be swapped for our setup
        self.xm = self.bound / (self.nun_min - self.nun_max)
        self.ym = self.bound / (self.nun_max - self.nun_min)
        self.xb = self.x_servo_center - self.xm * self.nun_center
        self.yb = self.y_servo_center - self.ym * self.nun_center
        try:
            self.n = nunchuck()
        except OSError:
            raise OSError('Ensure the Nunchuk is plugged in') from None
        self.x_servo = -1
        self.y_servo = -1

    def set_servo(self):
        x, y = self.n.joystick()
        self.x_servo = int(self.xm * x + self.xb)
        self.y_servo = int(self.ym * y + self.yb)
        if not self.no_x:
            self.pwm.set_pwm(self.x_pin, 0, self.x_servo + self.turret.x_offset)
        if not self.no_y:
            self.pwm.set_pwm(self.y_pin, 0, self.y_servo + self.turret.y_offset)

    def get_position(self):
        # TODO: With offset?
        return self.x_servo, self.y_servo

    def firing(self):
        return self.n.button_z()
