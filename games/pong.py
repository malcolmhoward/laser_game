import time
from math import fabs
from .game import Game
from src import Player, NPC
from paths import Bounce


class Pong(Game):
    """
    Two players swat a ball back and forth.
    """

    '''
    PLAYER INFO
    '''
    paddle_length = 10
    x_hit = 2

    '''
    BALL INFO
    '''
    ball_rate = 2
    resetting = False
    skip_frame = False
    laser_blink = False
    reset_time = 0
    reset_rate = 1

    def __init__(self, center, bound, pwm, player_1_controller, player_2_controller,
                 player_1_turret, player_2_turret, npc_turret):
        super().__init__(center, bound, pwm)
        self.player_1 = Player(bound, bound, pwm,
                               player_1_turret, player_1_controller,
                               no_x=True, fixed_x=int(center + bound/2))
        self.player_2 = Player(bound, bound, pwm,
                               player_2_turret, player_2_controller,
                               no_x=True, fixed_x=int(center - bound/2))
        self.ball = NPC(pwm, npc_turret)

    def play_on(self):
        player_1_points = 0
        player_2_points = 0
        self.playing = True
        self.ball.laser.on()
        self.player_1.laser.on()
        self.player_2.laser.on()
        while self.playing:
            ball = self.make_ball(self.ball_rate)
            prev_time = 0
            xs, ys = ball.send((False, False))
            while self.playing:
                self.curr_time = time.time()
                if self.curr_time - prev_time >= self.time_rate:
                    prev_time = self.curr_time
                    xp_1, yp_1 = self.player_1.set_servo()
                    xp_2, yp_2 = self.player_2.set_servo()
                    xp_1_hit = fabs(xp_1 - xs) <= self.x_hit
                    xp_2_hit = fabs(xp_2 - xs) <= self.x_hit
                    yp_1_hit = fabs(yp_1 - ys) <= self.paddle_length
                    yp_2_hit = fabs(yp_2 - ys) <= self.paddle_length
                    # Player 1 or 2 lose
                    if not yp_1_hit and xp_1_hit:
                        print('Player 1 loses!')
                        player_2_points += 1
                        self.resetting = True
                        self.reset_time = time.time()
                        break
                    elif not yp_2_hit and xp_2_hit:
                        print('Player 2 loses!')
                        player_1_points += 1
                        self.resetting = True
                        self.reset_time = time.time()
                        break
                    else:
                        top_hit = ys >= (self.center + self.bound/2)
                        bottom_hit = ys <= (self.center - self.bound/2)
                        # Player 1 hit
                        if yp_1_hit and xp_1_hit:
                            print('Player 1 hit!')
                            vertical_hit = True
                            horizontal_hit = False
                        # Player 2 hit
                        elif yp_2_hit and xp_2_hit:
                            print('Player 2 hit!')
                            vertical_hit = True
                            horizontal_hit = False
                        # Top or bottom wall hit
                        elif top_hit or bottom_hit:
                            horizontal_hit = True
                            vertical_hit = False
                        else:
                            horizontal_hit = False
                            vertical_hit = False
                        if not self.resetting:
                            xs, ys = ball.send((horizontal_hit,
                                                vertical_hit))
                    self.handle_ball_resetting()

    def handle_ball_resetting(self):
        """
        Handles all player info after firing, such as laser blinking
        :return:
        """
        if self.resetting:
            if not self.skip_frame:
                self.skip_frame = True
                if self.laser_blink:
                    self.ball.laser.on()
                else:
                    self.ball.laser.off()
                self.laser_blink = not self.laser_blink
            else:
                self.skip_frame = False
            if self.curr_time - self.reset_time > self.reset_rate:
                self.resetting = False
                self.ball.laser.on()

    def make_ball(self, angle=2, rate=2):
        bounce = Bounce(self.center, self.center, angle, rate)
        ball_servo = self.ball.follow_path(bounce.data())
        # Let the servos get into position. Yes, yield twice
        ball_servo.__next__()
        ball_servo.send((False, False))
        return ball_servo
