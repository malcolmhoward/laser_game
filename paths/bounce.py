from math import sin, cos
from typing import Generator


class Bounce:
    def __init__(self, x_start: int, y_start: int, angle_rad: float, rate: float):
        self.x_start = x_start
        self.y_start = y_start
        self.rate = rate
        self.angle_rad = angle_rad
        self.x_rate = rate * cos(self.angle_rad)
        self.y_rate = rate * sin(self.angle_rad)

    def data(self) -> Generator[int, int, None]:
        """
        Coroutine to advance an object at a certain rate until colliding with a wall.

        Call __next__() to initialize and get back the starting position
        Call send((horizontal_hit, vertical_hit)) to keep getting data
        There is no closing condition, so .close() exits
        :return:
        """
        x = self.x_start
        y = self.y_start
        yield x, y
        while True:
            x += self.x_rate
            y += self.y_rate
            # Get whether the object has collided with a wall
            horizontal_hit, vertical_hit = yield int(x), int(y)
            # Simply reverse the x/y rate depending on the wall type
            # TODO: could add a little variance in the angle with every bounce
            if horizontal_hit:
                self.y_rate *= -1
            if vertical_hit:
                self.x_rate *= -1
