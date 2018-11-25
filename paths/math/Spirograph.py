from math import cos, sin, pi
from ..path import Path

"""
Assume all maximums will be around R + r + d
"""


class Spirograph(Path):

    def __init__(self, center, rate, big_r, little_r):
        super().__init__(rate)
        if little_r == 0:
            raise ValueError('Little r cannot be zero.')
        self.center = center
        self.big_r = big_r
        self.little_r = little_r


class Hypotrochoid(Spirograph):
    """

    Hypocycloid: b = little_r
    """

    def __init__(self, center, rate, big_r, little_r, d):
        super().__init__(center, rate, big_r, little_r)
        self.ratio = self.big_r - self.little_r
        self.d = d

    def data(self):
        angle = 0
        while True:
            x = self.ratio * cos(angle) + self.d * cos(self.ratio / self.little_r * angle)
            y = self.ratio * sin(angle) - self.d * sin(self.ratio / self.little_r * angle)
            yield int(x + self.center), int(y+ self.center)
            # iterate angle and normalize
            angle += self.rate
            # FIXME: Any way to bound this?
            # if angle >= 2 * pi:
            #     angle -= 2 * pi
            # elif angle <= -2 * pi:
            #     angle += 2 * pi


class Epitrochoid(Spirograph):
    """

    Epicycloid: b = little_r
    """

    def __init__(self, center, rate, big_r, little_r, d):
        super().__init__(center, rate, big_r, little_r,)
        self.ratio = self.big_r + self.little_r
        self.d = d

    def data(self):
        angle = 0
        while True:
            x = self.ratio * cos(angle) - self.d * cos(self.ratio / self.little_r * angle)
            y = self.ratio * sin(angle) - self.d * sin(self.ratio / self.little_r * angle)
            yield int(x + self.center), int(y+ self.center)
            # iterate angle and normalize
            angle += self.rate
            # if angle >= 2 * pi:
            #     angle -= 2 * pi
            # elif angle <= -2 * pi:
            #     angle += 2 * pi
