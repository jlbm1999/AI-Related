import Utils
from Position import Position
from Piece import Piece
from Action import Action

# Clase para el Alfil

class Bishop(Piece):

    utilidad = 30
    ut_bishop_pos = [[-2, -1, -1, -1, -1, -1, -1, 0],
                    [-1, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0.5, 1, 1, 0.5, 0, -1],
                    [-1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1],
                    [-1, 0, 1, 1, 1, 1, 0, -1],
                    [-1, 1, 1, 1, 1, 1, 1, -1],
                    [-1, 0.5, 0, 0, 0, 0, 0.5, -1],
                    [-2, -1, -1, -1, -1, -1, -1, -2]]

    def __init__(self, color):
        self.m_color = color

        if (color == 0):
            self.m_type = Utils.wBishop
        else:
            self.m_type = Utils.bBishop

    def getPossibleActions(self, state):

        l = []
        # print('ACCEDO A LOS MOVIMIENTOS DIAGONALES')

        l = self.getDiagonalUpRightMoves(state)
        l += self.getDiagonalUpLeftMoves(state)
        l += self.getDiagonalDownRightMoves(state)
        l += self.getDiagonalDownLeftMoves(state)


        if self.m_type == Utils.wBishop:
            return l
        else:
            l.reverse()
            return l

    def getUtility(self, pos):
        if self.m_color == 0:	# Para las blancas
            utilidad = self.utilidad + self.ut_bishop_pos[pos[0]][pos[1]]
            return utilidad 
        else:					# Para las negras
            utilidad = (-1 * self.utilidad) + (-1 * self.ut_bishop_pos[7 - pos[0]][pos[1]])
            return utilidad 