from math import fabs
from gpiozero import LED
from .turret import Turret
from .player_controller import PlayerController


class Player:

    def __init__(self,
                 x_bound: int, y_bound: int,
                 pwm, turret: Turret,
                 controller: PlayerController,
                 x_offset: int=0, y_offset: int=0,
                 no_x: bool=False, no_y: bool=False,
                 fixed_x: int=0, fixed_y: int=0,
                 initial_x: int=None, initial_y: int=None,
                 x_center: int=None, y_center: int=None):
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.controller = controller
        self.turret = turret
        self.laser = LED(turret.laser_pin)
        self.pwm = pwm
        self.x_pin = turret.x_pin
        self.y_pin = turret.y_pin
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.no_x = no_x
        self.no_y = no_y
        self.fixed_x = fixed_x
        if fixed_x:
            self.servo_x = fixed_x
            pwm.set_pwm(self.x_pin, 0, fixed_x + turret.x_cal)
        else:
            if initial_x is not None:
                self.servo_x = initial_x
            else:
                self.servo_x = -1
        self.fixed_y = fixed_y
        if fixed_y:
            self.servo_y = fixed_y
            pwm.set_pwm(self.x_pin, 0, fixed_y + turret.y_cal)
        else:
            if initial_y is not None:
                self.servo_y = initial_y
            else:
                self.servo_y = -1
        self.x_center = x_center
        self.y_center = y_center
        """
        SNAP
        """
        # Calculate the values for y = mx + b
        # x needs to be swapped for our setup
        self.xm = self.x_bound / (controller.x_min - controller.x_max)
        self.ym = self.y_bound / (controller.y_max - controller.y_min)
        self.xb = turret.x_center - self.xm * controller.x_center
        self.yb = turret.y_center - self.ym * controller.y_center
        """
        MANUAL
        """
        self.x_range = controller.x_max - controller.x_center
        self.y_range = controller.y_max - controller.y_center
        self.manual_rate = 2

    def set_servo(self, min_x=None, max_x=None, min_y=None, max_y=None):
        x, y = self.controller.joystick()
        if not self.no_x:
            self.servo_x = int(self.xm * x + self.xb)
            if min_x is not None:
                self.servo_x = min(min_x, self.servo_x)
            if max_x is not None:
                self.servo_x = max(max_x, self.servo_x)
            self.pwm.set_pwm(self.x_pin, 0, self.servo_x
                                            + self.turret.x_cal
                                            + self.x_offset)
        if not self.no_y:
            self.servo_y = int(self.ym * y + self.yb)
            if min_y is not None:
                self.servo_y = min(min_y, self.servo_y)
            if max_y is not None:
                self.servo_y = max(max_y, self.servo_y)
            self.pwm.set_pwm(self.y_pin, 0, self.servo_y
                                            + self.turret.y_cal
                                            + self.y_offset)
        return self.servo_x + self.x_offset, self.servo_y + self.y_offset

    def manual_servo(self, min_x=None, max_x=None, min_y=None, max_y=None):
        x, y = self.controller.joystick()
        x_delta = self.controller.x_center - x
        y_delta = self.controller.y_center - y
        if not self.no_x:
            if fabs(x_delta) > 0.1 * self.x_range:
                self.servo_x += int(x_delta / self.x_range * self.manual_rate)
                if min_x is not None:
                    min_x_vals = [min_x, self.servo_x, int(self.x_center + self.x_bound/2)]
                else:
                    min_x_vals = [self.servo_x, int(self.x_center + self.x_bound / 2)]
                self.servo_x = min(*min_x_vals)
                if max_x is not None:
                    max_x_vals = [max_x, self.servo_x, int(self.x_center + self.x_bound/2)]
                else:
                    max_x_vals = [self.servo_x, int(self.x_center + self.x_bound / 2)]
                self.servo_x = max(*max_x_vals)
                self.pwm.set_pwm(self.x_pin, 0, self.servo_x
                                                + self.turret.x_cal
                                                + self.x_offset)
        if not self.no_y:
            if fabs(y_delta) > 0.1 * self.y_range:
                # Y inverted
                self.servo_y -= int(y_delta / self.y_range * self.manual_rate)
                if min_y is not None:
                    min_y_vals = [min_y, self.servo_y, int(self.y_center + self.y_bound/2)]
                else:
                    min_y_vals = [self.servo_y, int(self.y_center + self.y_bound / 2)]
                self.servo_y = min(*min_y_vals)
                if max_y is not None:
                    max_y_vals = [max_y, self.servo_y, int(self.y_center - self.y_bound/2)]
                else:
                    max_y_vals = [self.servo_y, int(self.y_center - self.y_bound / 2)]
                self.servo_y = max(*max_y_vals)
                self.pwm.set_pwm(self.y_pin, 0, self.servo_y
                                                + self.turret.y_cal
                                                + self.y_offset)
        return self.servo_x + self.x_offset, self.servo_y + self.y_offset

    def get_position(self):
        return self.servo_x + self.x_offset, self.servo_y + self.y_offset

    def firing(self):
        return self.controller.fire()
