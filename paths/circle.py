from math import sin, cos, pi


class Circle:

    def __init__(self, x_start, y_start, radius, angle_to_radius, rate, clockwise=False):
        self.x_start = x_start
        self.y_start = y_start
        self.radius = radius
        self.angle_to_radius = angle_to_radius,
        self.rate = rate
        self.clockwise = clockwise
