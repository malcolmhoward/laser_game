import Adafruit_PCA9685
from src.player import Player
from src import PlayerNunchuk, pro_controller_factory
from src.TURRETS import TURRET_1, TURRET_2, TURRET_3

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
# c = PlayerNunchuk(127, 127, 20, 200, 20, 200)
c, _ = pro_controller_factory()
player = Player(100, 100, pwm, TURRET_2, c)
player.laser.on()
while True:
    player.set_servo()
    if player.firing():
        x, y = player.get_position()
        print('x offset: ', x - 375)
        print('y offset: ', y - 375)
