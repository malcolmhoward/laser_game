from gpiozero import LED
import Adafruit_PCA9685
from nunchuck import nunchuck

try:
    n = nunchuck()
except OSError:
    raise OSError('Are you sure the Nunchuk is plugged in, idiot?')
laser = LED(4)
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
# How big you want your "box" to be
bound = 100
servo_center = 375
# Range of the Nunchuk's analog stick
nun_min = 45
nun_max = 255
nun_center = 127
# Calculate the values for y = mx + b
xm = bound/(nun_min - nun_max)
ym = bound/(nun_max - nun_min)
xb = servo_center - xm * nun_center
yb = servo_center - ym * nun_center
while True:
    x, y = n.joystick()
    # set_pwm requires ints
    x_servo = int(xm*x + xb)
    y_servo = int(ym*y + yb)
    pwm.set_pwm(0, 0, x_servo)
    pwm.set_pwm(1, 0, y_servo)
    if n.button_c():
        laser.on()
    else:
        laser.off()
