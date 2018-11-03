from math import sin, cos, atan2, fabs
from typing import Tuple


class Line:
    def __init__(self, x_start: int, y_start: int, x_end: int, y_end: int, rate: float):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.rate = rate
        self.angle = atan2(y_end - y_start, x_end - x_start)
        self.x_rate = rate * cos(self.angle)
        self.y_rate = rate * sin(self.angle)

    def data(self) -> Tuple[int, int]:
        x = self.x_start
        y = self.y_start
        yield x, y
        while fabs(x - self.x_end) > fabs(self.x_rate) and fabs(y - self.y_end) > fabs(self.y_rate):
            x += self.x_rate
            y += self.y_rate
            yield int(x), int(y)
