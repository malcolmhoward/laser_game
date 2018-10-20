from math import sin, cos, atan2, fabs
import matplotlib.pyplot as plt


class Line:
    def __init__(self, x_start, y_start, x_end, y_end, rate):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.rate = rate
        self.angle = atan2(y_end - y_start, x_end - x_start)
        self.x_rate = rate * cos(self.angle)
        self.y_rate = rate * sin(self.angle)

    def data(self):
        x = self.x_start
        y = self.y_start
        yield x, y
        while fabs(x - self.x_end) > fabs(self.x_rate) and fabs(y - self.y_end) > fabs(self.y_rate):
            x += self.x_rate
            y += self.y_rate
            yield x, y


if __name__ == '__main__':
    l = Line(20, 100, 0, 0, 12)
    data = l.data()
    x = []
    y = []
    for d in data:
        x.append(d[0])
        y.append(d[1])
    plt.plot(x, y)
    plt.xticks([0, 100])
    plt.yticks([0, 100])
    plt.show()
