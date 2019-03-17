import game as santorino
from display import *
from recorded_game import Match

import random

game = santorino.Game()
print( "All moves count = " + str(len(game.allmoves)))
match = Match()
match.add_moves( game.set_up_randomly() )
showGameState( game.get_current_state(), game.active_player, game.stage, game.playedturns )



while game.winner is None:
	validMoves = game.get_allowed_moves()
	if len(validMoves) == 0:
		print( "No valid moves left." )
		assert game.winner is not None # no valid moves, winner should be filled now
		continue

	chosenMove = random.choice( validMoves )
	game.move( chosenMove )

	match.add_move( chosenMove )

	showGameState( game.get_current_state(), game.active_player, game.stage, game.playedturns )

print("Winner: " + ("White" if game.winner == 0 else "Black"))

print( "Save string: " + match.serialize() )
