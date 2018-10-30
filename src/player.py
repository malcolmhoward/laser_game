from .turret import Turret
from .player_controller import PlayerController


class Player:

    def __init__(self, x_bound: int, y_bound: int, pwm, turret: Turret,
                 controller: PlayerController,
                 no_x: bool=False, no_y: bool=False):
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.controller = controller
        self.nun_x_center = controller.x_center
        self.nun_y_center = controller.y_center
        self.nun_x_min = controller.x_min
        self.nun_x_max = controller.x_max
        self.nun_y_min = controller.y_min
        self.nun_y_max = controller.y_max
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
        self.servo_x = -1
        self.servo_y = -1

    def set_servo(self):
        x, y = self.controller.joystick()
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
        return self.controller.fire()
