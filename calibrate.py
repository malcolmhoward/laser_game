import json
import Adafruit_PCA9685
from src.player import Player
from src import PlayerNunchuk, pro_controller_factory
from src.TURRETS import TURRET_1, TURRET_2, TURRET_3

with open('src/calibration.json', 'r') as json_file:
    curr_cal = json.load(json_file)

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
# c = PlayerNunchuk(127, 127, 20, 200, 20, 200)
c, _ = pro_controller_factory()
player = Player(100, 100, pwm, TURRET_1, c)
player.laser.on()
while True:
    player.set_servo()
    if player.firing():
        x, y = player.get_position()
        x_offset = x - 375
        y_offset = y - 375
        break
curr_cal['turret1']['x'] = x_offset
curr_cal['turret1']['y'] = y_offset
with open('src/calibration.json', 'w') as json_file:
    json.dump(curr_cal, json_file)
