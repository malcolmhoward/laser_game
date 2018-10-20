from Adafruit_Python_PCA9685.Adafruit_PCA9685 import PCA9685


class NPC:

    def __init__(self, pwm: PCA9685, x_channel: int, y_channel: int):
        self.pwm = pwm
        self.x_channel = x_channel
        self.y_channel = y_channel

    def set_servo(self, x: int, y: int):
        self.pwm.set_pwm(self.x_channel, 0, x)
        self.pwm.set_pwm(self.y_channel, 0, y)

    def follow_path(self, path_generator):
        for x, y in path_generator:
            self.set_servo(x, y)
            yield x, y
        return
