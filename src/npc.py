from typing import Generator, Tuple
from gpiozero import LED
from .turret import Turret


class NPC:

    def __init__(self, pwm, turret: Turret):
        self.pwm = pwm
        self.turret = turret
        self.x_pin = turret.x_pin
        self.y_pin = turret.y_pin
        self.laser = LED(turret.laser_pin)

    def set_servo(self, x: int, y: int):
        self.pwm.set_pwm(self.x_pin, 0, x + self.turret.x_cal)
        self.pwm.set_pwm(self.y_pin, 0, y + self.turret.y_cal)

    def follow_path(self, path_generator: Generator[Tuple[int, int], Tuple[bool, bool], None]):
        """
        Wraps a generator/coroutine and sets the servo to the x/y value received.

        :param path_generator:
        :return:
        """
        x, y = path_generator.__next__()
        gen_arg = yield x, y
        while True:
            # Send the arg (if any) to the generator
            x, y = path_generator.send(gen_arg)
            self.set_servo(x, y)
            gen_arg = yield x, y
