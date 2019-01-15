import json
import time
import Adafruit_PCA9685
from src.player import Player
from src import PlayerNunchuk
from src.TURRETS import TURRET_1, TURRET_2, TURRET_3, TURRET_4, TURRET_5

with open('src/calibration.json', 'r') as json_file:
    curr_cal = json.load(json_file)

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
c = PlayerNunchuk(127, 127, 20, 200, 20, 200)
# c, _ = pro_controller_factory()
turrets = {TURRET_1: '1',
           TURRET_2: '2',
           TURRET_3: '3',
           TURRET_4: '4',
           TURRET_5: '5',
}
for turret, num in turrets.items():
    player = Player(100, 100, pwm, turret, c)
    player.laser.on()
    while True:
        x, y = player.set_servo()
        if player.firing():
            x_offset = x - 375
            y_offset = y - 375
            time.sleep(2)
            break
    curr_cal['turret' + num]['x'] += x_offset
    curr_cal['turret' + num]['y'] += y_offset
with open('src/calibration.json', 'w') as json_file:
    json.dump(curr_cal, json_file)
