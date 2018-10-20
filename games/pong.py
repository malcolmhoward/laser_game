from src import Player, NPC


class Pong:

    def __init__(self, bound, servo_center, pwm):
        self.player_1 = Player(bound, servo_center - bound/2, pwm, 0, 1, no_x=True)
        self.player_2 = Player(bound, servo_center + bound/2, pwm, 4, 5, no_x=True)
        self.ball = NPC(pwm, 2, 3)
