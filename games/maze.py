from .game import Game
from src import Player
from src.player_controller import PlayerController
from src.turret import Turret



class Wall:
    thickness = 3

    def __init__(self, x_start, y_start, x_end=0, y_end=0):
        self.x_start = x_start
        self.y_start = y_start
        if not x_end:
            self.x_end = x_start + self.thickness
            self.is_vertical = True
        else:
            self.is_vertical = False
            self.x_end = x_end
        if not y_end:
            self.y_end = y_start + self.thickness
            self.is_horizontal = True
        else:
            self.is_horizontal = False
            self.y_end = y_end

    def has_collided(self, x, y):
        x_collision = self.x_start <= x <= self.x_end
        y_collision = self.y_start <= y <= self.y_end
        return x_collision and y_collision


class Maze(Game):

    def __init__(self, center, bound, pwm,
                 controller: PlayerController,
                 player_turret: Turret,
                 ):
        super().__init__(center, bound, pwm)
        self.player = Player(bound, bound, pwm, player_turret, controller)
        self.player.laser.on()

    def play_on(self):
        self.playing = True
        lines =[Wall(355, 355, y_end=395), Wall(355, 395, x_end=395)]
        while self.playing:
            restrict_x = False
            restrict_y = False
            x, y = self.player.set_servo(restrict_x, restrict_y)
            for line in lines:
                collide = line.has_collided(x, y)
                if collide:
                    if not restrict_x:
                        restrict_x = line.is_vertical
                    if not restrict_y:
                        restrict_y = line.is_horizontal
