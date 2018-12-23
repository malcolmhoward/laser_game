from typing import Tuple
from math import atan2, sqrt


class PlayerController:

    def __init__(self, x_center, y_center, x_min, x_max, y_min, y_max):
        self.x_center = x_center
        self.y_center = y_center
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def joystick(self) -> Tuple[int, int]:
        ...

    def angle_and_radius(self) -> Tuple[float, float]:
        x, y = self.joystick()
        angle = atan2(y - self.y_center, x - self.x_center)
        radius = sqrt((y - self.y_center) ** 2 + (x - self.x_center) ** 2)
        return angle, radius

    def fire(self):
        ...
