import time
from .game import Game
from src import Player
from src.player_controller import PlayerController
from src.turret import Turret



class Wall:
    thickness = 4

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
        binding_values = {}
        if self.x_start <= x <= self.x_end and self.y_start <= y <= self.y_end:
            if self.is_vertical:
                if self.x_end - self.thickness/2 - x > 0:
                    binding_values['min_x'] = self.x_start
                else:
                    binding_values['max_x'] = self.x_end
            else:
                if self.y_end - self.thickness/2 - y > 0:
                    binding_values['min_y'] = self.y_start
                else:
                    binding_values['max_y'] = self.y_end
        return binding_values

class MazeWalls:
    def __init__(self, x_offset, y_offset):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.walls = []

    def add_wall(self, x_start, y_start, x_end=0, y_end=0):
        if x_end:
            x_end += self.x_offset
        if y_end:
            y_end += self.y_offset
        new_wall = Wall(x_start + self.x_offset, y_start + self.x_offset,
                        x_end, y_end)
        self.walls.append(new_wall)

    def check_collision(self, x, y):
        binding = {}
        for wall in self.walls:
            binding.update(wall.has_collided(x, y))
        return binding

LINES = [Wall(355, 355, y_end=395), Wall(355, 395, x_end=395)]
WALLS = MazeWalls(325, 325)
WALLS.add_wall(y_start=25, y_end=100, x_start=15)
WALLS.add_wall(y_start=0, y_end=75, x_start=45)
WALLS.add_wall(y_start=25, y_end=100, x_start=75)


class Maze(Game):

    def __init__(self, center, bound, pwm,
                 controller: PlayerController,
                 player_turret: Turret,
                 ):
        super().__init__(center, bound, pwm)
        self.player = Player(bound, bound, pwm, player_turret, controller,
                             initial_x=415, initial_y=415,
                             x_center=375, y_center=375)
        self.player.laser.on()

    def play_on(self):
        self.playing = True
        binding = {}
        prev_time = 0
        while self.playing:
            curr_time = time.time()
            if curr_time - prev_time >= self.time_rate:
                prev_time = curr_time
                x, y = self.player.manual_servo(**binding)
                binding = WALLS.check_collision(x, y)
