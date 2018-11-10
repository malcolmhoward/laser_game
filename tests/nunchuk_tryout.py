import time
from src import Nunchuk

n = Nunchuk()

while True:
    if n.button_c():
        print('c')
    if n.button_z():
        print('z')
    print('Joystick: ', n.joystick())
    print('Accelerometer: ', n.accelerometer())
    time.sleep(0.1)
