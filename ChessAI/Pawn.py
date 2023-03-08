import Utils
from Position import Position
from Piece import Piece
from Action import Action
from Queen import Queen

# this class implements the getPossibleActions for each type of piece
# Clase para el peón

class Pawn(Piece): 
	
	utilidad = 10

	# Utilidades dependiendo de la posición
	ut_peon_pos = 	[[0, 0, 0, 0, 0, 0, 0, 0],
                    [5, 5, 5, 5, 5, 5, 5, 5],
                    [1, 1, 1, 3, 3, 2, 1, 1],
                    [0.5, 0.5, 0, 2.5, 2, 1, 0.5, 0.5],
                    [0, 0, 1, 2, 2, 0, 0, 0],
                    [0.5, -0.5, 1, 0, 0, -1, -0.5, 0.5],
                    [0.5, 1, 1, -2, -2, 1, 1, 0.5],
                    [0, 0, 0, 0, 0, 0, 0, 0]]

	# constructor
	def __init__(self, color):
		self.m_color = color
		
		if color==0: 
			self.m_type = Utils.wPawn
		else:
			self.m_type = Utils.bPawn

	
	# this method must be completed with all the possible pieces	
	def getPossibleActions(self, state):
		
		r = state.m_agentPos[0]
		c = state.m_agentPos[1]
		action = None
		
		l = []
		
		oponent_color = -1
		if self.m_color == 0: # white pawn
			oponent_color = 1
		elif self.m_color == 1: #black pawn
			oponent_color = 0
		
		if self.m_color == 0:					# Si el peón corona
			if r == state.m_boardSize - 1:
				self.m_type = 4
				self.m_piece = Queen(0)
				return self.m_piece.getPossibleActions(state)
		if self.m_color == 1:
			if r == 0:
				self.m_type = 10
				self.m_piece = Queen(1)
				return self.m_piece.getPossibleActions(state)

		if self.m_type == Utils.wPawn:
			if state.m_board[r+1][c] == Utils.empty: # standard pawn move
				l.append(Action(state.m_agentPos, Position(r+1,c)))
			if r==1 and (state.m_board[r+2][c] == Utils.empty): # starting pawn move
					l.append(Action(state.m_agentPos, Position(r+2,c)))
			if c>0 and (state.m_board[r+1][c-1] != Utils.empty) and (Utils.getColorPiece(state.m_board[r+1][c-1]) == oponent_color): # capture
				l.append(Action(state.m_agentPos, Position(r+1,c-1)))
			if c<(state.m_boardSize-1) and (state.m_board[r+1][c+1] != Utils.empty) and (Utils.getColorPiece(state.m_board[r+1][c+1]) == oponent_color): # capture
				l.append(Action(state.m_agentPos, Position(r+1,c+1)))
		else:
			if state.m_board[r-1][c] == Utils.empty: # standard pawn move
				l.append(Action(state.m_agentPos, Position(r-1,c)))
			if r==6 and (state.m_board[r-2][c] == Utils.empty): # starting pawn move
					l.append(Action(state.m_agentPos, Position(r-2,c)))
			if c>0 and (state.m_board[r-1][c-1] != Utils.empty) and (Utils.getColorPiece(state.m_board[r-1][c-1]) == oponent_color): # capture
				l.append(Action(state.m_agentPos, Position(r-1,c-1)))
			if c<(state.m_boardSize-1) and (state.m_board[r-1][c+1] != Utils.empty) and (Utils.getColorPiece(state.m_board[r-1][c+1]) == oponent_color): # capture
				l.append(Action(state.m_agentPos, Position(r-1,c+1)))

		return l

	def getUtility(self, pos):
		if self.m_color == 0:	# Para las blancas
			utilidad =  self.utilidad + self.ut_peon_pos[7 - pos[0]][pos[1]]		# Para las blancas, como es la simeétrica, se pone col / row
			return utilidad 
		else:					# Para las negras
			utilidad =  (-1 * self.utilidad) + (-1 * self.ut_peon_pos[pos[0]][pos[1]])
			return utilidad 