import Utils
from Position import Position
from Piece import Piece
from Action import Action

# Clase para le reina

class Queen(Piece):

    utilidad = 90

    # Utilidades dependiendo de la posición
    ut_queen_pos =  [[-2, -1, -1, -0.5, -0.5, -1, -1, -2],
                    [-1, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1],
                    [0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
                    [0, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
                    [-1, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1],
                    [-1, 0, 0.5, 0, 0, 0, 0, -1],
                    [-2, -1, -1, -0.5, -0.5, -1, -1, -2]]

    def __init__(self, color):
        self.m_color = color

        if (color == 0):
            self.m_type = Utils.wQueen
        else:
            self.m_type = Utils.bQueen

    def getPossibleActions(self, state):

        l = []

        # Movimientos diagonales del alfil
        l = self.getDiagonalUpRightMoves(state)
        l += self.getDiagonalUpLeftMoves(state)
        l += self.getDiagonalDownRightMoves(state)
        l += self.getDiagonalDownLeftMoves(state)

        # Movimientos lineales de la torre
        l += self.getVerticalUpMoves(state)
        l += self.getHorizontalRightMoves(state)
        l += self.getHorizontalLeftMoves(state)
        l += self.getVerticalDownMoves(state)

        
        if self.m_type == Utils.wQueen or l == []:
            return l
        else:
            l.reverse()
            return l
        
    def getUtility(self, pos):
        if self.m_color == 0:	# Para las blancas
            utilidad = self.utilidad + self.ut_queen_pos[pos[0]][pos[1]]
            return utilidad 
        else:					# Para las negras
            utilidad = (-1 * self.utilidad) + (-1 * self.ut_queen_pos[7 - pos[0]][pos[1]])
            return utilidad 
        