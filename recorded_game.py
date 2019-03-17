from typing import List

import game as santorino

class Match:
	def __init__( self ):
		self.moves: List[santorino.Move] = []

	def add_move( self, move ):
		self.moves.append( move )

	def add_moves( self, moves ):
		self.moves.extend( moves )

	def serialize( self ):
		save_string = ""
		for move in self.moves:
			save_string += move.serialize() + ","
		return save_string
