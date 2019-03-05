import game as santorino
import random

def showGameState(gameState, playerTurn, gameStage, playedTurns):
	print()
	print( "After Turn " + str(playedTurns) )
	print( "Next: " + ("White" if playerTurn == 0 else "Black") )
	line = "---------------"
	print( line )


	for y in range( 5 ):
		row = ""
		for x in range( 5 ):
			playerChar = "," if gameState[ 1 ][ x ][ y ] > 0 else "'" if gameState[ 1 ][ x ][ y ] < 0 else " "
			row += playerChar
			row += str( (gameState[0][x][y]) or "." )
			row += playerChar
		print( row )

	print( line )

game = santorino.Game()
game.set_up_randomly()
showGameState(game.get_current_state(), game.player, game.stage, game.playedturns)

while game.winner == 0:
	validMoves = game.get_allowed_moves()
	if validMoves.__len__() == 0:
		print( "No valid moves left." )
		assert game.winner != 0 # no valid moves, winner should be filled now
		continue

	chosenMove = random.choice( validMoves )
	game.move( chosenMove )

	if game.playedturns % 10 == 0 and game.player == 0:
		showGameState(game.get_current_state(), game.player, game.stage, game.playedturns)

showGameState(game.get_current_state(), game.player, game.stage, game.playedturns)
print ("Winner: " + ("White" if game.winner == 1 else "Black"))
