import game as santorino
import random

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

import time

def showGameState( gameState, playerTurn, gameStage, playedTurns, gameBoardGraphics = None):
	if not gameBoardGraphics:
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
	else:
		xpos = [ 0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4 ]
		ypos = [ 0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4 ]
		zpos = np.zeros( 25 )

		dx = np.ones( 25 ) * 0.8
		dy = np.ones( 25 ) * 0.8
		dz = np.zeros( 25 )

		playerXpos = np.zeros( 4 )
		playerYpos = np.zeros( 4 )
		playerZpos = np.zeros( 4 )

		playerD = np.ones( 4 ) * 0.5

		playerIndex = 0
		for i in range(25):
			height = gameState[0][xpos[i]][ypos[i]] * 0.5
			dz[i] = height
			if gameState[1][xpos[i]][ypos[i]] != 0:
				playerXpos[playerIndex] = xpos[i] + 0.15
				playerYpos[playerIndex] = ypos[i] + 0.15
				playerZpos[playerIndex] = height
				playerIndex += 1

		gameBoardGraphics.clear()
		gameBoardGraphics.bar3d( xpos, ypos, zpos, dx, dy, dz, color='#00ceaa' )
		gameBoardGraphics.bar3d( playerXpos, playerYpos, playerZpos, playerD, playerD, playerD*0.5, color='#aa0033' )
		plt.draw()


gameWindow = plt.figure()
gameBoardGraphics = gameWindow.add_subplot( 111, projection='3d' )
plt.show(block=False)

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
showGameState( game.get_current_state(), game.player, game.stage, game.playedturns, gameBoardGraphics )
print("Winner: " + ("White" if game.winner == 1 else "Black"))

print( "All moves count = " + str(len(game.allmoves)))
plt.show()

input("Press Return to end...")
