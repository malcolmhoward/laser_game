from src import Player, NPC


class Pong:

    def __init__(self, bound, pwm, player_1_controller, player_2_controller,
                 player_1_turret, player_2_turret, npc_turret):
        self.player_1 = Player(bound, bound, pwm,
                               player_1_turret, player_1_controller, no_x=True)
        self.player_2 = Player(bound, bound, pwm,
                               player_2_turret, player_2_controller, no_x=True)
        self.ball = NPC(pwm, npc_turret)
