import Adafruit_PCA9685
from games import Maze
from src.TURRETS import TURRET_1
from src.WiiController import pro_controller_factory

left, right = pro_controller_factory()

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

maze = Maze(375, 100, pwm, left, TURRET_1)
maze.play_on()
