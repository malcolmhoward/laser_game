import time
import random
from paths import Line
from src import Player
from src import NPC


class MissileDefense:

    time_rate = 1/60
    bomb_radius = 10

    def __init__(self, pwm, bound, center):
        self.bound = bound
        self.center = center
        self.player = Player(bound, center, pwm, 0, 1)
        self.missile = NPC(pwm, 2, 3)
        self.playing = False

    def play_on(self):
        self.playing = True
        hit = False
        lose = False
        prev_time = 0
        player_score = 0
        homes_destroyed = 0
        missile = self.missile.follow_path(self.make_missile())
        while self.playing:
            if hit:
                player_score += 1
            if lose:
                homes_destroyed += 1
            if hit or lose:
                hit = False
                lose = False
                missile = self.missile.follow_path(self.make_missile())
            curr_time = time.time()
            if curr_time - prev_time >= self.time_rate:
                prev_time = curr_time
                self.player.set_servo()
                try:
                    m_x, m_y = missile.__next__()
                except StopIteration:
                    lose = True
                else:
                    player_x, player_y = self.player.get_position()
                    if self.player.firing():
                        dist_2_bomb = (m_y - player_y)/(m_x - player_x)
                        if dist_2_bomb <= self.bomb_radius:
                            hit = True

    def make_missile(self):
        x_low = int(self.center - self.bound / 2)
        x_high = int(self.center + self.bound/2)
        x_start = random.randint(x_low, x_high)
        x_end = random.randint(x_low, x_high)
        missile = Line(x_start, x_low, x_end, x_high, 1)
        return missile.data()
