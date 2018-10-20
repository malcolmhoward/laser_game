class NPC:

    def __init__(self, pwm, x_channel, y_channel):
        self.pwm = pwm
        self.x_channel = x_channel
        self.y_channel = y_channel

    def set_servo(self, x, y):
        self.pwm.set_pwm(self.x_channel, 0, x)
        self.pwm.set_pwm(self.y_channel, 0, y)
