from nunchuck import nunchuck
import Adafruit_PCA9685

n = nunchuck()
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
# How big you want your "box" to be
bound = 500
servo_center = 1500
# Range of the Nunchuk's analog stick
nun_min = 45
nun_max = 255
nun_center = 127
# Calculate the values for y = mx + b
m = bound/(nun_max - nun_min)
b = servo_center - m * nun_center
while True:
    x, y = n.joystick()
    # set_pwm requires ints
    x_servo = int(m*x + b)
    y_servo = int(m*y + b)
    pwm.set_pwm(0, 0, x_servo)
    pwm.set_pwm(1, 0, y_servo)
