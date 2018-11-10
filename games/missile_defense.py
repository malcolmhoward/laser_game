import time
import random
from typing import Generator
from paths import Line
from src import Player, NPC
from src.player_controller import PlayerController
from src.turret import Turret


class MissileDefense:

    time_rate = 1/60
    bomb_radius = 10

    def __init__(self, pwm,
                 controller: PlayerController,
                 player_turret: Turret,
                 missile_turret: Turret,
                 bound, center):
        self.bound = bound
        self.center = center
        self.player = Player(bound, bound, pwm, player_turret, controller)
        self.player.laser.on()
        self.missile = NPC(pwm, missile_turret)
        self.missile.laser.on()
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
                p_x, p_y = self.player.set_servo()
                try:
                    m_x, m_y = missile.__next__()
                except StopIteration:
                    lose = True
                else:
                    if self.player.firing():
                        dist_2_bomb = (m_y - p_y)/(m_x - p_x)
                        if dist_2_bomb <= self.bomb_radius:
                            hit = True

    def make_missile(self) -> Generator:
        y_low = int(self.center + self.bound / 2)
        y_high = int(self.center - self.bound/2)
        x_start = random.randint(y_high, y_low)
        x_end = random.randint(y_high, y_low)
        missile = Line(x_start, y_low, x_end, y_high, 1)
        return missile.data()
