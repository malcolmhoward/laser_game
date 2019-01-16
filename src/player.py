from math import fabs
try:
    from gpiozero import LED
except Exception as e:
    if e.__class__.__name__ == "BadPinFactory":
        print("gpiozero.exc.BadPinFactory: Unable to load any default pin factory!")
        print("Setting LED to None..")
        LED = None
    else:
        raise(e)
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
                 x_center: int=375, y_center: int=375):
        self.x_bound = x_bound
        self.y_bound = y_bound
        if controller is None:
            print('controller was none, so use PlayerController instead')
            controller = PlayerController(x_center=400, y_center=300, x_min=0, x_max=800, y_min=0, y_max=600)
        self.controller = controller
        self.turret = turret
        self.laser = None
        if LED is not None:
            self.laser = LED(turret.laser_pin)
        self.pwm = pwm
        if turret is not None:
            self.x_pin = turret.x_pin
            self.y_pin = turret.y_pin
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.no_x = no_x
        self.no_y = no_y
        self.fixed_x = fixed_x
        if fixed_x:
            self.servo_x = fixed_x
            if turret is not None:
                pwm.set_pwm(self.x_pin, 0, fixed_x + turret.x_cal)
        else:
            if initial_x is not None and self.pwm is not None:
                self.servo_x = initial_x
                self.pwm.set_pwm(self.x_pin, 0, self.servo_x + self.turret.x_cal + self.x_offset)
            else:
                self.servo_x = -1
        self.fixed_y = fixed_y
        if fixed_y:
            self.servo_y = fixed_y
            if turret is not None:
                pwm.set_pwm(self.x_pin, 0, fixed_y + turret.y_cal)
        else:
            if initial_y is not None and self.pwm is not None:
                self.servo_y = initial_y
                self.pwm.set_pwm(self.y_pin, 0, self.servo_y + self.turret.y_cal + self.y_offset)
            else:
                self.servo_y = -1
        self.x_center = x_center
        self.x_min = int(x_center + x_bound / 2)
        self.x_max = int(x_center - x_bound / 2)
        self.y_center = y_center
        self.y_min = int(y_center + y_bound / 2)
        self.y_max = int(y_center - y_bound / 2)
        """
        SNAP
        """
        # Calculate the values for y = mx + b
        # x needs to be swapped for our setup
        self.xm = self.x_bound / (self.controller.x_min - self.controller.x_max)
        self.ym = self.y_bound / (self.controller.y_max - self.controller.y_min)
        self.xb = self.xm * self.controller.x_center
        self.yb = self.ym * self.controller.y_center
        if turret is not None:
            self.xb = turret.x_center - self.xm * self.controller.x_center
            self.yb = turret.y_center - self.ym * self.controller.y_center
        """
        MANUAL
        """
        self.x_range = controller.x_max - controller.x_center
        self.y_range = controller.y_max - controller.y_center
        self.manual_rate = 3

    def set_servo(self, min_x=999, max_x=-999, min_y=999, max_y=-999):
        """
        Servos follow exactly where the player sets the joystick.

        Min/max values are purposely set far out to allow them to be passed in.
        :param min_x:
        :param max_x:
        :param min_y:
        :param max_y:
        :return:
        """
        x, y = self.controller.joystick()
        if not self.no_x:
            self.servo_x = int(self.xm * x + self.xb)
            self.servo_x = min(min_x, self.servo_x)
            self.servo_x = max(max_x, self.servo_x)
            if self.pwm is not None:
                self.pwm.set_pwm(self.x_pin, 0, self.servo_x + self.turret.x_cal + self.x_offset)
        if not self.no_y:
            self.servo_y = int(self.ym * y + self.yb)
            self.servo_y = min(min_y, self.servo_y)
            self.servo_y = max(max_y, self.servo_y)
            if self.pwm is not None:
                self.pwm.set_pwm(self.y_pin, 0, self.servo_y + self.turret.y_cal + self.y_offset)
        return self.servo_x + self.x_offset, self.servo_y + self.y_offset

    def manual_servo(self, min_x=999, max_x=-999, min_y=999, max_y=-999):
        """
        Servos stay where they are when the joysticks are not touched.

        Min/max values are purposely set far out to allow them to be passed in.
        :param min_x:
        :param max_x:
        :param min_y:
        :param max_y:
        :return:
        """
        # FIXME: Since xy/values are higher at the cardinal directions,
        #   scrolling doesn't feel as snappy in the joystick corners
        x, y, x_delta, y_delta = 0, 0, 0, 0
        if self.controller is not None:
            x, y = self.controller.joystick()
            x_delta = self.controller.x_center - x
            y_delta = self.controller.y_center - y
        if not self.no_x:
            if fabs(x_delta) > 0.1 * self.x_range:
                self.servo_x += int(x_delta / self.x_range * self.manual_rate)
                self.servo_x = min(min_x, self.servo_x, self.x_min)
                self.servo_x = max(max_x, self.servo_x, self.x_max)
                if self.pwm is not None:
                    self.pwm.set_pwm(self.x_pin, 0, self.servo_x + self.turret.x_cal + self.x_offset)
        if not self.no_y:
            if fabs(y_delta) > 0.1 * self.y_range:
                # Y inverted
                self.servo_y -= int(y_delta / self.y_range * self.manual_rate)
                self.servo_y = min(min_y, self.servo_y, self.y_min)
                self.servo_y = max(max_y, self.servo_y, self.y_max)
                if self.pwm is not None:
                    self.pwm.set_pwm(self.y_pin, 0, self.servo_y + self.turret.y_cal + self.y_offset)
        return self.servo_x + self.x_offset, self.servo_y + self.y_offset

    def get_position(self):
        return self.servo_x + self.x_offset, self.servo_y + self.y_offset

    def firing(self):
        return self.controller.fire()
