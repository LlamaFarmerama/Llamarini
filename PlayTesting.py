import game as santorino
from display import *

import random

import time

graphicsWindow = initializeDisplay()

game = santorino.Game()
game.set_up_randomly()
showGameState( game.get_current_state(), game.player, game.stage, game.playedturns )


while game.winner == 0:
	validMoves = game.get_allowed_moves()
	if len(validMoves) == 0:
		print( "No valid moves left." )
		assert game.winner != 0 # no valid moves, winner should be filled now
		continue

	chosenMove = random.choice( validMoves )
	game.move( chosenMove )

	showGameState( game.get_current_state(), game.player, game.stage, game.playedturns )

	# time.sleep(0.1)

showGameState( game.get_current_state(), game.player, game.stage, game.playedturns )
showGameState( game.get_current_state(), game.player, game.stage, game.playedturns, graphicsWindow )
print("Winner: " + ("White" if game.winner == 1 else "Black"))

print( "All moves count = " + str(len(game.allmoves)))

shutdownDisplay()
