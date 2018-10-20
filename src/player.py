from src.nunchuck import nunchuck


class Player:

    # Range of the Nunchuk's analog stick
    nun_min = 45
    nun_max = 255
    nun_center = 174

    def __init__(self, bound, servo_center, pwm, x_channel, y_channel, no_x=False, no_y=False):
        self.bound = bound
        self.servo_center = servo_center
        self.pwm = pwm
        self.x_channel = x_channel
        self.y_channel = y_channel
        self.no_x = no_x
        self.no_y = no_y
        # Calculate the values for y = mx + b
        # x needs to be swapped for our setup
        self.xm = self.bound / (self.nun_min - self.nun_max)
        self.ym = self.bound / (self.nun_max - self.nun_min)
        self.xb = self.servo_center - self.xm * self.nun_center
        self.yb = self.servo_center - self.ym * self.nun_center
        try:
            self.n = nunchuck()
        except OSError:
            raise OSError('Ensure the Nunchuk is plugged in') from None

    def set_servo(self):
        x, y = self.n.joystick()
        x_servo = self.xm * x + self.xb
        y_servo = self.ym * y + self.yb
        if not self.no_x:
            self.pwm.set_pwm(self.x_channel, 0, x_servo)
        if not self.no_y:
            self.pwm.set_pwm(self.y_channel, 0, y_servo)
