from .game import Game
from src import Player
from src.player_controller import PlayerController
from src.turret import Turret


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
        restrict_x = False
        restrict_y = False
        line =((375, 355), (375, 395))
        while self.playing:
            x, y = self.player.set_servo(restrict_x, restrict_y)
            x_collision = x == line[0][0]
            y_collision = line[0][1] <= y <= line[1][1]
            if x_collision and y_collision:
                restrict_x = True
            else:
                restrict_x = False