import time
from src import ClassicController

c = ClassicController()
while True:
    if c.button_a():
        print('a')
    if c.button_b():
        print('b')
    if c.button_x():
        print('x')
    if c.button_y():
        print('y')
    if c.button_up():
        print('up')
    if c.button_down():
        print('down')
    if c.button_left():
        print('left')
    if c.button_right():
        print('right')
    if c.button_minus():
        print('minus')
    if c.button_plus():
        print('plus')
    if c.button_home():
        print('home')
    if c.button_zl():
        print('zl')
    if c.button_zr():
        print('zr')
    if c.button_trigger_left():
        print('lt')
    if c.button_trigger_right():
        print('rt')
    print('Left joystick: ', c.left_joystick())
    print('Right joystick: ', c.right_joystick())
    print('Left Trigger Pressure: ', c.left_trigger_pressure())
    print('Right Trigger Pressure: ', c.right_trigger_pressure())
    time.sleep(0.1)
