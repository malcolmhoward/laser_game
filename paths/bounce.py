from math import sin, cos
from typing import Generator, Tuple
from .path import Path


class Bounce(Path):
    def __init__(self, x_start: int, y_start: int, angle_rad: float, rate: float):
        super().__init__(rate)
        self.x_start = x_start
        self.y_start = y_start
        self._angle = angle_rad
        self.x_rate = rate * cos(self._angle)
        self.y_rate = rate * sin(self._angle)

    def data(self) -> Generator[Tuple[int, int], Tuple[bool, bool], None]:
        """
        Coroutine to advance an object at a certain rate until colliding with a wall.

        Call __next__() to initialize and get back the starting position
        Call send((horizontal_hit, vertical_hit)) to keep getting data
        There is no closing condition, so .close() exits
        :return:
        """
        x = self.x_start
        y = self.y_start
        h_already_hit = False
        v_already_hit = False
        yield x, y
        while True:
            x += self.x_rate
            y += self.y_rate
            # Get whether the object has collided with a wall
            horizontal_hit, vertical_hit = yield int(x), int(y)
            # Simply reverse the x/y rate depending on the wall type
            # TODO: could add a little variance in the angle with every bounce
            if horizontal_hit:
                if not h_already_hit:
                    self.y_rate *= -1
                    h_already_hit = True
                else:
                    h_already_hit = False
            if vertical_hit:
                if not v_already_hit:
                    self.x_rate *= -1
                    v_already_hit = True
                else:
                    v_already_hit = False

    @Path.rate.setter
    def rate(self, rate):
        self._rate = rate
        self.x_rate = rate * cos(self._angle)
        self.y_rate = rate * sin(self._angle)

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self._angle = angle
        self.x_rate = self._rate * cos(self._angle)
        self.y_rate = self._rate * sin(self._angle)
