from .nunchuck import nunchuck
from .turret import Turret
from .player_nunchuk import PlayerNunchuk


class Player:

    def __init__(self, x_bound: int, y_bound: int, pwm, turret: Turret,
                 player_nunchuk: PlayerNunchuk,
                 no_x: bool=False, no_y: bool=False):
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.player_nunchuk = player_nunchuk
        self.nun_x_center = player_nunchuk.x_center
        self.nun_y_center = player_nunchuk.y_center
        self.nun_x_min = player_nunchuk.x_min
        self.nun_x_max = player_nunchuk.x_max
        self.nun_y_min = player_nunchuk.y_min
        self.nun_y_max = player_nunchuk.y_max
        self.servo_x_center = turret.x_center
        self.servo_y_center = turret.y_center
        self.turret = turret
        self.pwm = pwm
        self.x_pin = turret.x_pin
        self.y_pin = turret.y_pin
        self.no_x = no_x
        self.no_y = no_y
        # Calculate the values for y = mx + b
        # x needs to be swapped for our setup
        self.xm = self.x_bound / (self.nun_x_min - self.nun_x_max)
        self.ym = self.y_bound / (self.nun_y_max - self.nun_y_min)
        self.xb = self.servo_x_center - self.xm * self.nun_x_center
        self.yb = self.servo_y_center - self.ym * self.nun_y_center
        try:
            self.n = nunchuck()
        except OSError:
            raise OSError('Ensure the Nunchuk is plugged in') from None
        self.servo_x = -1
        self.servo_y = -1

    def set_servo(self):
        x, y = self.n.joystick()
        self.servo_x = int(self.xm * x + self.xb)
        self.servo_y = int(self.ym * y + self.yb)
        if not self.no_x:
            self.pwm.set_pwm(self.x_pin, 0, self.servo_x + self.turret.x_offset)
        if not self.no_y:
            self.pwm.set_pwm(self.y_pin, 0, self.servo_y + self.turret.y_offset)

    def get_position(self):
        # TODO: With offset?
        return self.servo_x, self.servo_y

    def firing(self):
        return self.n.button_z()
