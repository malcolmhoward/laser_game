from gpiozero import LED
import Adafruit_PCA9685
from src.player import Player
from src.NUNCHUKS import NUNCHUK_1
from src.TURRETS import TURRET_1

laser = LED(4)
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
player_1 = Player(100, 100, pwm, TURRET_1, NUNCHUK_1)
while True:
    player_1.set_servo()
