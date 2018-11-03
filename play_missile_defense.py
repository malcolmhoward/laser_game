import Adafruit_PCA9685
from games import MissileDefense
from src import pro_controller_factory
from src.TURRETS import TURRET_1, TURRET_2

left_pro, _ = pro_controller_factory()
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
m = MissileDefense(pwm, left_pro, TURRET_1, TURRET_2, 100, 375)
m.play_on()
