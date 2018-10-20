from gpiozero import LED
import Adafruit_PCA9685
from src.player import Player

laser = LED(4)
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
player_1 = Player(100, 375, pwm, 0, 1)
while True:
    player_1.set_servo()
