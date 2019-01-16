import time
import random
from typing import Generator
from math import sqrt
from paths import Line
from src import Player, NPC
from .game import Game
from src.player_controller import PlayerController
from src.turret import Turret
# TODO: Add missiles remaining counter that counts up until win
# TODO: Corkscrew missiles!


class MissileDefense(Game):
    """
    The player must aim and shoot at missile raining down on a peaceful city.
    """

    '''
    GAME INFO
    '''
    curr_time = 0

    '''
    PLAYER INFO
    '''
    # Delay until the player can fire again
    player_attack_rate = 1
    # Size of player attack
    bomb_radius = 10
    player_fired = False
    fire_time = 0
    skip_frame = False
    laser_blink = False
    '''
    MISSILE INFO
    '''
    # How long to delay until the missile comes alive
    missile_delay = 1
    # How much to increase the missile speed per success
    rate_increase = 0.1
    '''
    LIVES INFO
    '''
    lives = 10
    life_pos = 0

    def __init__(self, center, bound, pwm,
                 controller: PlayerController,
                 player_turret: Turret,
                 missile_turret: Turret,
                 life_turret: Turret):
        super().__init__(center, bound, pwm)
        '''
        INIT PLAYER
        '''
        self.player = Player(bound, bound, pwm, player_turret, controller)
        if self.player.laser is not None:
            self.player.laser.on()
        '''
        INIT MISSILE
        '''
        self.missile = NPC(pwm, missile_turret)
        if self.missile.laser is not None:
            self.missile.laser.on()
        '''
        INIT LIFE COUNTER
        '''
        self.life_counter = NPC(pwm, life_turret)
        self.life_pos = int(center + bound/2)
        # Put life counter out of bounds
        self.life_counter.set_servo(int(center - bound/2) - 10, int(center + bound/2))
        self.life_counter.laser.on()
        self.life_distance = int(bound/self.lives)

    def play_on(self):
        self.playing = True
        hit = False
        lose = False
        prev_time = 0
        player_score = 0
        missile_rate = 1
        missile = self.make_missile()
        missile_respawn = False
        respawn_time = time.time()
        while self.playing:
            if hit:
                player_score += 1
                missile_rate += self.rate_increase
            if lose:
                self.lives -= 1
                self.life_pos -= self.life_distance
                self.life_counter.set_servo(int(self.center - self.bound/2) - 10,
                                            self.life_pos)
            if hit or lose:
                hit = False
                lose = False
                self.missile.laser.off()
            self.current_missile = self.make_missile(self.missile_rate)
            self.missile_respawn = True
            self.respawn_time = time.time()
        # Win/lose conditions
        if self.player_score == 10:
            pass
        elif self.lives == 0:
            pass
        self.curr_time = time.time()
        if self.curr_time - self.prev_time >= self.time_rate:
            prev_time = self.curr_time
            p_x, p_y = 0, 0 # TODO get p_x and p_y from something other than the servo
            if self.player.laser is not None:
                p_x, p_y = self.player.set_servo()
            if not self.missile_respawn:
                try:
                    m_x, m_y = self.current_missile.__next__()
                except StopIteration:
                    self.lose = True
                else:
                    if not self.player_fired and self.player.firing():
                        self.player_fired = True
                        self.fire_time = time.time()
                        dist_2_bomb = sqrt((m_y - p_y)**2 + (m_x - p_x)**2)
                        if dist_2_bomb <= self.bomb_radius:
                            self.hit = True
            else:
                if self.curr_time - self.respawn_time > self.missile_delay:
                    self.missile_respawn = False
                    if self.missile.laser is not None:
                        self.missile.laser.on()
            self.handle_player_firing()

    def handle_player_firing(self):
        """
        Handles all player info after firing, such as laser blinking
        :return:
        """
        if self.player_fired:
            if not self.skip_frame:
                self.skip_frame = True
                if self.laser_blink:
                    self.player.laser.on()
                else:
                    self.player.laser.off()
                self.laser_blink = not self.laser_blink
            else:
                self.skip_frame = False
            if self.curr_time - self.fire_time > self.player_attack_rate:
                self.player_fired = False
                self.player.laser.on()

    def make_missile(self, rate=1) -> Generator:
        """
        Creates a new random missile
        :param rate:
        :return:
        """
        y_low = int(self.center - self.bound / 2)
        y_high = int(self.center + self.bound / 2)
        x_start = random.randint(y_low, y_high)
        # Since the controllers can't reach the corners, restrict them
        x_end = random.randint(y_low + 20, y_high - 20)
        path = Line(x_start, y_high, x_end, y_low, rate)
        self.current_missile = self.missile.follow_path(path.data())
        # Let the servos get into position. Yield once for init, yield again to move servos
        self.current_missile.__next__()
        self.current_missile.__next__()
        return self.current_missile
