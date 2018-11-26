import time
import Adafruit_PCA9685
from src import NPC
from src.TURRETS import TURRET_1
from paths.math import Hypotrochoid

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

h = Hypotrochoid(375, 1/60, 50, 20, 10)
d = h.data()

npc = NPC(pwm, TURRET_1)
npc.laser.on()
graph = npc.follow_path(d)
curr_time = time.time()
while time.time() - curr_time > 1/60:
    graph.__next__()
