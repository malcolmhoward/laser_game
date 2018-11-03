from src import Player, NPC
from paths import Bounce


class Pong:

    def __init__(self, bound, pwm, player_1_controller, player_2_controller,
                 player_1_turret, player_2_turret, npc_turret):
        self.bound = bound
        self.player_1 = Player(bound, bound, pwm,
                               player_1_turret, player_1_controller, no_x=True)
        self.player_2 = Player(bound, bound, pwm,
                               player_2_turret, player_2_controller, no_x=True)
        self.ball = NPC(pwm, npc_turret)

    def play_on(self):
        bounce = Bounce(int(self.bound/2), int(self.bound/2), 0, 2)
        ball_servo = self.ball.follow_path(bounce)
        x, y = ball_servo.__next__()
