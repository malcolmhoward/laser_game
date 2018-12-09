import time
from src import Nunchuk, ProController

c = Nunchuk()
# c = ProController()
# c.joystick = c.left_joystick

x, y = c.joystick()
print("x, y: ", x, y)

left_x = True
right_x = False
down_y = False
up_y = False
print('Move X all the way left and press fire')
while True:
    if c.button_z() and left_x:
        x, _ = c.joystick()
        print(x)
        print('Move X all the way right and press fire')
        left_x = not left_x
        right_x = not right_x
        time.sleep(1)
    if c.button_z() and right_x:
        x, _ = c.joystick()
        print(x)
        print('Move Y all the way down and press fire')
        right_x = not right_x
        down_y = not down_y
        time.sleep(1)
    if c.button_z() and down_y:
        _, y = c.joystick()
        print(y)
        print('Move Y all the way up and press fire')
        down_y = not down_y
        up_y = not up_y
        time.sleep(1)
    if c.button_z() and up_y:
        _, y = c.joystick()
        print(y)
        print('Pat yourself on the back for a job well done.')
        break
