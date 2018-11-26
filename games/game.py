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
        self.game_screen_title = 'Game Title'
        self.laser_radius = 1
        self.wall_width = 5

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
                # Capture keyboard arrow input to update location of player-controlled game objects
                # We're using floats here instead of int to allow for more precise changes
                # Be sure to cast to int as needed when it's time to draw
                xchange, ychange = 0.0, 0.0
                movement_distance = .1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        xchange = -movement_distance
                    elif event.key == pygame.K_RIGHT:
                        xchange = movement_distance

                    if event.key == pygame.K_UP:
                        ychange = -movement_distance
                    elif event.key == pygame.K_DOWN:
                        ychange = movement_distance
                print('xchange', xchange)
                print('ychange', ychange)
                self.x += xchange
                self.y += ychange
                print ('self.x', self.x)
                print ('self.y', self.y)
                self.game_window.fill(self.color_palette.get('white'))
                self.run_gui_logic()
                pygame.display.update()
                # Go ahead and update the screen with what we've drawn.
                # This MUST happen after all the other drawing commands.
                pygame.display.flip()

    def run_game_logic(self):
        ...

    def run_gui_logic(self):
        self.draw_laser(self.x, self.y)

    def init_game(self, player=None):
        # This is an override for games that are multiplayer, where self.player does not exist, i.e. self.player_1
        if player:
            self.player = player
        self.use_gui = self.player.laser is None
        if self.use_gui:
            self.init_gui()

    def init_gui(self):
        pygame.init()
        game_screen_resolution = (self.bound, self.bound)
        self.game_window = pygame.display.set_mode(game_screen_resolution)
        pygame.display.set_caption(self.game_screen_title)
        self.color_palette = {
            'black': (0, 0, 0),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'white': (255, 255, 255)
        }

    def draw_laser(self, x=200, y=200):
        # pygame.draw.circle(), which requires int values, so cast x and y just in case those are float values
        pygame.draw.circle(self.game_window, self.color_palette.get('red'), [int(x), int(y)], self.laser_radius)

    def draw_lasers(self, x=200, y=200):
        # TODO: This should iterate through a list of x/y coordinates for all available lasers to call pygame.draw.circle
        pass

    def draw_wall(self, start_pos=(0, 0), end_pos=(200, 200), wall_thickness=0):
        if not wall_thickness:
            wall_thickness = self.wall_width
        pygame.draw.line(self.game_window, self.color_palette.get('red'), start_pos, end_pos, wall_thickness)