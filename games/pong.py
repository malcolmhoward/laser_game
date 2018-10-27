from src import Player, NPC
from src.TURRETS import TURRET_1, TURRET_2, TURRET_3
from src.NUNCHUKS import NUNCHUK_1, NUNCHUK_2


class Pong:

    def __init__(self, bound, pwm):
        self.player_1 = Player(bound, bound, pwm, TURRET_1, NUNCHUK_1, no_x=True)
        self.player_2 = Player(bound, bound, pwm, TURRET_3, NUNCHUK_2, no_x=True)
        self.ball = NPC(pwm, TURRET_2)
