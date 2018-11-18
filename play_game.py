from argparse import ArgumentParser

# from games.jezz_ball import JezzBall
from games.maze import Maze
from games.missile_defense import MissileDefense
from games.pong import Pong

parser = ArgumentParser()
parser.add_argument("-g", "--game", dest="game", help="start the game named GAME", metavar="GAME")

args = parser.parse_args()
game_name = args.game

if game_name is not None:
	print('play the {} game'.format(game_name))
	game = None
	if game_name in ['maze', 'Maze']:
		game = Maze(center=0, bound=400, pwm=None, controller=None, player_turret=None)
	elif game_name in ['missle_defense', 'MissileDefense']:
		game = MissileDefense(
			center=0,
			bound=400,
			pwm=None,
			controller=None,
			player_turret=None,
			missile_turret=None,
			life_turret=None
		)
	elif game_name in ['pong', 'Pong']:
		game = Pong(center=0, bound=400, pwm=None, controller=None, player_turret=None)
	if game is not None:
		game.play_on()
else:
	print('Please specify a game name.  Available options are: "Maze", "MissileDefense", "Pong"')
