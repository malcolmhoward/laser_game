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
                 fixed_x: int=0, fixed_y: int=0):
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
            pwm.set_pwm(self.x_pin, 0, fixed_x)
        self.fixed_y = fixed_y
        if fixed_y:
            pwm.set_pwm(self.x_pin, 0, fixed_y)
        # Calculate the values for y = mx + b
        # x needs to be swapped for our setup
        self.xm = x_bound / (controller.x_min - controller.x_max)
        self.ym = y_bound / (controller.y_max - controller.y_min)
        self.xb = turret.x_center - self.xm * controller.x_center
        self.yb = turret.y_center - self.ym * controller.y_center
        self.servo_x = -1
        self.servo_y = -1

    def set_servo(self):
        x, y = self.controller.joystick()
        self.servo_x = int(self.xm * x + self.xb)
        self.servo_y = int(self.ym * y + self.yb)
        if not self.no_x:
            self.pwm.set_pwm(self.x_pin, 0, self.servo_x
                                            + self.turret.x_cal
                                            + self.x_offset)
        if not self.no_y:
            self.pwm.set_pwm(self.y_pin, 0, self.servo_y
                                            + self.turret.y_cal
                                            + self.y_offset)

    def get_position(self):
        return self.servo_x + self.x_offset, self.servo_y + self.y_offset

    def firing(self):
        return self.controller.fire()
