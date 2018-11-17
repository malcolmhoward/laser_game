from math import cos, sin, pi, fabs
from ..path import Path


class Spirograph(Path):

    def __init__(self, rate, big_r, little_r):
        super().__init__(rate)
        self.big_r = big_r
        self.little_r = little_r


class Hypo(Spirograph):
    def __init__(self, rate, big_r, little_r):
        super(Spirograph).__init__(rate, big_r, little_r)
        self.ratio = self.big_r - self.little_r


class Epi(Spirograph):
    def __init__(self, rate, big_r, little_r):
        super().__init__(rate, big_r, little_r)
        self.ratio = self.big_r + self.little_r


class Hypotrochoid(Hypo):

    def __init__(self, rate, big_r, little_r, d):
        super(Hypo).__init__(rate, big_r, little_r)
        self.d = d

    def data(self):
        angle = 0
        while True:
            x = self.ratio * cos(angle) + self.d * cos(self.ratio / self.little_r * angle)
            y = self.ratio * sin(angle) - self.d * sin(self.ratio / self.little_r * angle)
            yield x, y
            # iterate angle and normalize
            angle += self.rate
            if angle >= 2 * pi:
                angle -= 2 * pi
            elif angle <= -2 * pi:
                angle += 2 * pi


class Hypocycloid(Hypo):

    def __init__(self, rate, big_r, little_r):
        super(Hypo).__init__(rate, big_r, little_r)

    def data(self):
        pass


class Epicycloid(Epi):

    def __init__(self, rate, big_r, little_r):
        super().__init__(rate, big_r, little_r)


class Epitrochoid(Epi):

    def __init__(self, rate, big_r, little_r):
        super().__init__(rate, big_r, little_r)
