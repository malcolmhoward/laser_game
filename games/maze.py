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
        binding = {}
        lines =[Wall(355, 355, y_end=395), Wall(355, 395, x_end=395)]
        while self.playing:
            x, y = self.player.set_servo(**binding)
            binding = {}
            for line in lines:
                binding.update(line.has_collided(x, y))
                # if collide:
                #     if not restrict_x:
                #         restrict_x = line.is_vertical
                #     if not restrict_y:
                #         restrict_y = line.is_horizontal
