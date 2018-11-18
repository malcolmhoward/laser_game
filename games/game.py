import pygame
from pygame.locals import QUIT


class Game:
    def __init__(self, center, bound, pwm,):
        self.bound = bound
        self.center = center
        self.pwm = pwm
        self.playing = False
        self.time_rate = 1/60
        self.curr_time = 0
        self.player = None

    def play_on(self):
        self.playing = True
        self.init_game()
        while self.playing:
            self.run_game_logic()
            if self.use_gui:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.playing = False
                        print('Game window closed.  Now exiting game...')
                self.game_window.fill(self.color_palette.get('white'))
                pygame.display.update()

    def run_game_logic(self):
        ...

    def init_game(self):
        self.use_gui = self.player.laser is None
        if self.use_gui:
            self.init_gui()

    def init_gui(self):
        pygame.init()
        game_screen_resolution = (self.bound, self.bound)
        self.game_window = pygame.display.set_mode(game_screen_resolution)
        game_screen_title = 'Maze Game'
        pygame.display.set_caption(game_screen_title)
        self.color_palette = {
            'white': (255, 255, 255)
        }
