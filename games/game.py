import pygame
from pygame.locals import QUIT


class Game:
    def __init__(self, center, bound, pwm, gui_enabled=False):
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
        self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0
        self.gui_enabled = gui_enabled

    def play_on(self):
        self.playing = True
        self.init_game()
        while self.playing:
            self.run_game_logic()
            if self.gui_enabled:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.playing = False
                        print('Game window closed.  Now exiting game...')
                # Capture keyboard arrow input to update location of player-controlled game objects
                # We're using floats here instead of int to allow for more precise changes
                # Be sure to cast to int as needed when it's time to draw
                x1change, y1change, x2change, y2change = 0.0, 0.0, 0.0, 0.0
                movement_distance = .1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1change = -movement_distance
                    elif event.key == pygame.K_RIGHT:
                        x1change = movement_distance
                    if event.key == pygame.K_a:
                        x2change = -movement_distance
                    elif event.key == pygame.K_d:
                        x2change = movement_distance

                    if event.key == pygame.K_UP:
                        y1change = -movement_distance
                    elif event.key == pygame.K_DOWN:
                        y1change = movement_distance
                    if event.key == pygame.K_w:
                        y2change = -movement_distance
                    elif event.key == pygame.K_s:
                        y2change = movement_distance
                print('x1change', x1change)
                print('y1change', y1change)
                print('x2change', x2change)
                print('y2change', y2change)
                self.x1 += x1change
                self.y1 += y1change
                self.x2 += x2change
                self.y2 += y2change
                print ('self.x1', self.x1)
                print ('self.y1', self.y1)
                print('self.x2', self.x2)
                print('self.y2', self.y2)
                self.game_window.fill(self.color_palette.get('white'))
                self.run_gui_logic()
                pygame.display.update()
                # Go ahead and update the screen with what we've drawn.
                # This MUST happen after all the other drawing commands.
                pygame.display.flip()

    def run_game_logic(self):
        ...

    def run_gui_logic(self):
        self.draw_laser(self.x1, self.y1)
        self.draw_laser(self.x2, self.y2)

    def init_game(self, player=None):
        # This is an override for games that are multiplayer, where self.player does not exist, i.e. self.player_1
        if player:
            self.player = player
        if self.gui_enabled:
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