from math import sin, cos, atan2, fabs
from typing import Generator, Tuple
from .path import Path


class Line(Path):
    def __init__(self,
                 x_start: int, y_start: int,
                 x_end: int, y_end: int,
                 rate: float):
        super().__init__(rate)
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.angle = atan2(y_end - y_start, x_end - x_start)
        self.x_rate = rate * cos(self.angle)
        self.y_rate = rate * sin(self.angle)

    def data(self) -> Generator[Tuple[int, int], None, None]:
        x = self.x_start
        y = self.y_start
        keep_going = True
        yield x, y
        # For horizontal or vertical lines, don't iterate the flat axis
        while keep_going:
            keep_going = False
            if fabs(x - self.x_end) > fabs(self.x_rate):
                x += self.x_rate
                keep_going = True
            if fabs(y - self.y_end) > fabs(self.y_rate):
                y += self.y_rate
                keep_going = True
            yield int(x), int(y)
        yield self.x_end, self.y_end
