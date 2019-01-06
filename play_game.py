from argparse import ArgumentParser

# from games.jezz_ball import JezzBall
from games.maze import Maze
from games.missile_defense import MissileDefense
from games.pong import Pong

parser = ArgumentParser()
parser.add_argument("-g", "--game", dest="game", help="start the game named GAME", metavar="GAME")

args = parser.parse_args()
game_name = args.game
valid_game_names = ['maze', 'Maze', 'missle_defense', 'MissileDefense', 'pong', 'Pong']

if game_name is not None and game_name in valid_game_names:
	print('play the {} game'.format(game_name))
	game = None
	if game_name in ['maze', 'Maze']:
		game = Maze(
			center=0,
			bound=400,
			pwm=None,
			controller=None,
			player_turret=None,
			gui_enabled=True
		)
	elif game_name in ['missle_defense', 'MissileDefense']:
		game = MissileDefense(
			center=0,
			bound=400,
			pwm=None,
			controller=None,
			player_turret=None,
			missile_turret=None,
			life_turret=None,
			gui_enabled=True
		)
	elif game_name in ['pong', 'Pong']:
		game = Pong(
			center=0,
			bound=400,
			pwm=None,
			player_1_controller=None,
			player_2_controller=None,
			player_1_turret=None,
			player_2_turret=None,
			npc_turret=None,
			gui_enabled=True
		)
	if game is not None:
		game.play_on()
else:
	print('Please specify a valid game name.  Available options are: "Maze", "MissileDefense", "Pong"')
