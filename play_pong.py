import Adafruit_PCA9685
from games import Pong
from src.TURRETS import TURRET_1, TURRET_2, TURRET_3
from src import pro_controller_factory

controller_1, controller_2 = pro_controller_factory()
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
p = Pong(375, 100, pwm, controller_1, controller_2, TURRET_1, TURRET_3, TURRET_2)
p.play_on()
