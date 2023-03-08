import Utils
from Piece import Piece

# this class implements the getPossibleActions for each type of piece
# Clase para la torre

class Rook(Piece): 
	
	utilidad = 50

	# Utilidades dependiendo de la posición
	ut_rook_pos = 	[[0, 0, 0, 0, 0, 0, 0, 0],
                    [0.5, 1, 1, 1, 1, 1, 1, 0.5],
                    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                    [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                    [0, 0, 0, 0, 0, 0, 0, 0]]

	# constructor
	def __init__(self, color):
		self.m_color = color
		
		if color==0: 
			self.m_type = Utils.wRook
		else:
			self.m_type = Utils.bRook

	
	# this method must be completed with all the possible pieces	
	def getPossibleActions(self, state):
		l = []

		l = self.getVerticalUpMoves(state)
		l += self.getHorizontalRightMoves(state)
		l += self.getHorizontalLeftMoves(state)
		l += self.getVerticalDownMoves(state)
		
		if self.m_type == Utils.wRook or l == []:	# Depende del color, el orden de las acciones es distinto
			return l
		else:
			l.reverse()
			return l

	def getUtility(self, pos):
		if self.m_color == 0:	# Para las blancas
			utilidad = self.utilidad + self.ut_rook_pos[pos[0]][pos[1]]
			return utilidad 
		else:					# Para las negras
			utilidad = (-1 * self.utilidad) + (-1 * self.ut_rook_pos[7 - pos[0]][pos[1]])
			return utilidad 