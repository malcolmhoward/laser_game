import time
from math import fabs
from src import Player, NPC
from paths import Bounce


class Pong:

    time_rate = 1 / 60
    paddle_length = 10
    x_hit = 2

    def __init__(self, center, bound, pwm, player_1_controller, player_2_controller,
                 player_1_turret, player_2_turret, npc_turret):
        self.center = center
        self.bound = bound
        self.player_1 = Player(bound, bound, pwm,
                               player_1_turret, player_1_controller, no_x=True)
        self.player_2 = Player(bound, bound, pwm,
                               player_2_turret, player_2_controller, no_x=True)
        self.ball = NPC(pwm, npc_turret)
        self.playing = True

    def play_on(self):
        self.playing = True
        bounce = Bounce(int(self.bound/2), int(self.bound/2), 0, 2)
        ball_servo = self.ball.follow_path(bounce)
        prev_time = 0
        xs, ys = ball_servo.__next__()
        while self.playing:
            curr_time = time.time()
            if curr_time - prev_time >= self.time_rate:
                prev_time = curr_time
                xp_1, yp_1 = self.player_1.get_position()
                xp_2, yp_2 = self.player_2.get_position()
                xp_1_hit = fabs(xp_1 - xs) <= self.x_hit
                xp_2_hit = fabs(xp_2 - xs) <= self.x_hit
                yp_1_hit = fabs(yp_1 - ys) <= self.paddle_length
                yp_2_hit = fabs(yp_2 - ys) <= self.paddle_length
                # Player 1 or 2 lose
                if not yp_1_hit and xp_1_hit:
                    pass
                elif not yp_1_hit and xp_2_hit:
                    pass
                else:
                    # Player 1 or 2 hit
                    if (yp_1_hit and xp_1_hit) or (yp_2_hit and xp_2_hit):
                        vertical_hit = True
                        horizontal_hit = False
                    # Top or bottom wall hit
                    elif ys >= (self.center + self.bound/2) or ys <= (self.center - self.bound/2):
                        horizontal_hit = True
                        vertical_hit = False
                    else:
                        horizontal_hit = False
                        vertical_hit = False
                    xs, ys = ball_servo.send((horizontal_hit, vertical_hit))
