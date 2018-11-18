from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-g", "--game", dest="game", help="start the game named GAME", metavar="GAME")

args = parser.parse_args()
print(args)
print(args.game)
game_name = args.game
if game_name in ['maze', 'Maze']:
	print('play the maze game')
	from games.maze import Maze
	maze_game = Maze(center=0, bound=400, pwm=None, controller=None, player_turret=None)
	maze_game.play_on()
elif game_name is None:
	print('Please specify a game name.  Available options are: "Maze"')