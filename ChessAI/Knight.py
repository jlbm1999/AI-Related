import Utils
from Position import Position
from Piece import Piece
from Action import Action

# Clase para el caballo

class Knight(Piece):

    utilidad = 30

    ut_knight_pos = [[-5, -4, -3, -3, -3, -3, -4, -5],
                    [-4, -2, 0, 0, 0, 0, -2, -4],
                    [-3, 0, 1, 1.5, 1.5, 1, 0, -3],
                    [-3, 0.5, 1, 2, 2, 1.5, 0.5, -3],
                    [-3, 0, 1, 2, 2, 1.5, 0, -3],
                    [-3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3],
                    [-4, -2, 0, 0.5, 0.5, 0, -2, -4],
                    [-5, -4, -3, -3, -3, -3, -4, -5]]

    def __init__(self, color):
        self.m_color = color

        if (color == 0):
            self.m_type = Utils.wKnight
        else:
            self.m_type = Utils.bKnight
    
    def getPossibleActions(self, state):

        r = state.m_agentPos[0]
        c = state.m_agentPos[1]
        oponent_color = -1
        l = []

        if (self.m_color == 0):  # White Knight
            oponent_color = 1
        else:                   # Black Knight
            oponent_color = 0

        
        if((r > 1 and c < state.m_boardSize-1 and state.m_board[r-2][c+1] == Utils.empty) 
			or (r > 1 and c < state.m_boardSize-1 and state.m_board[r-2][c+1] != Utils.empty and Utils.getColorPiece(state.m_board[r-2][c+1]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r-2,c+1)))
        
        if((r > 1 and c > 0 and state.m_board[r-2][c-1] == Utils.empty) 
			or (r > 1 and c > 0 and state.m_board[r-2][c-1] != Utils.empty and Utils.getColorPiece(state.m_board[r-2][c-1]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r-2,c-1)))

        if((r > 0 and c > 1 and state.m_board[r-1][c-2] == Utils.empty) 
			or (r > 0 and c > 1 and state.m_board[r-1][c-2] != Utils.empty and Utils.getColorPiece(state.m_board[r-1][c-2]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r-1,c-2)))
        
        if((r > 0 and c < state.m_boardSize-2 and state.m_board[r-1][c+2] == Utils.empty) 
			or (r > 0 and c < state.m_boardSize-2 and state.m_board[r-1][c+2] != Utils.empty and Utils.getColorPiece(state.m_board[r-1][c+2]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r-1,c+2)))
        
        if((r < state.m_boardSize-1 and c > 1 and state.m_board[r+1][c-2] == Utils.empty) 
			or (r < state.m_boardSize-1 and c > 1 and state.m_board[r+1][c-2] != Utils.empty and Utils.getColorPiece(state.m_board[r+1][c-2]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r+1,c-2)))
        
        if((r > state.m_boardSize-1 and c < state.m_boardSize-2 and state.m_board[r+1][c+2] == Utils.empty) 
			or (r > state.m_boardSize-1 and c < state.m_boardSize-2 and state.m_board[r+1][c+2] != Utils.empty and Utils.getColorPiece(state.m_board[r+1][c+2]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r+1,c+2)))
        
        if((r < state.m_boardSize-2 and c < state.m_boardSize-1 and state.m_board[r+2][c+1] == Utils.empty) 
			or (r < state.m_boardSize-2 and c < state.m_boardSize-1 and state.m_board[r+2][c+1] != Utils.empty and Utils.getColorPiece(state.m_board[r+2][c+1]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r+2,c+1)))

        if((r < state.m_boardSize-2 and c > 0 and state.m_board[r+2][c-1] == Utils.empty) 
			or (r < state.m_boardSize-2 and c > 0 and state.m_board[r+2][c-1] != Utils.empty and Utils.getColorPiece(state.m_board[r+2][c-1]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r+2,c-1)))
        

        if self.m_type == Utils.wKnight or l == []:
            return l
        else:
            l.reverse()
            return l           

    def getUtility(self, pos):
        if self.m_color == 0:	# Para las blancas
            utilidad = self.utilidad + self.ut_knight_pos[pos[0]][pos[1]]
            return utilidad
        else:					# Para las negras
            utilidad = (-1 * self.utilidad) + (-1 * self.ut_knight_pos[7 - pos[0]][pos[1]])
            return utilidad