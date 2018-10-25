from .turret import Turret


class NPC:

    def __init__(self, pwm, turret: Turret):
        self.pwm = pwm
        self.turret = turret
        self.x_pin = turret.x_pin
        self.y_pin = turret.y_pin

    def set_servo(self, x: int, y: int):
        self.pwm.set_pwm(self.x_pin, 0, x + self.turret.x_offset)
        self.pwm.set_pwm(self.y_pin, 0, y + self.turret.y_offset)

    def follow_path(self, path_generator):
        for x, y in path_generator:
            self.set_servo(x + self.turret.x_offset, y + self.turret.y_offset)
            yield x, y
        return
