from gpiozero import LED
import Adafruit_PCA9685
from src.player import Player
from src import PlayerNunchuk
from src.TURRETS import TURRET_1, TURRET_2, TURRET_3

nunchuk = PlayerNunchuk(127, 127, 20, 200, 20, 200)
laser = LED(4)
laser.on()
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
player_1 = Player(100, 100, pwm, TURRET_1, nunchuk)
while True:
    player_1.set_servo()
