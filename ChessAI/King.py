import Utils
from Position import Position
from Piece import Piece
from Action import Action

# Clase para el rey

class King(Piece):
    
    utilidad = 9000

    # Utilidades dependiendo de la posición
    # Utilidad para el principio y mitad del juego, donde se escuda en los peones
    ut_king_pos =   [[-3, -4, -4, -5, -5, -4, -4, -3],
                    [-3, -4, -4, -5, -5, -4, -4, -3],
                    [-3, -3, -3, -5, -5, -6, -7, -7],
                    [-3, -4, -4, -5, -5, -4, -5, -3],
                    [-2, -3, -3, -4, -4, -3, -3, -2],
                    [-1, -2, -2, -2, -2, -2, -2, -1],
                    [2, 2, 0, 0, 0, 0, 2, 2],
                    [2, 3, 1, 0, 0, 1, 3, 2]]


    def __init__(self, color):
        self.m_color = color

        if (color == 0):
            self.m_type = Utils.wKing
        else:
            self.m_type = Utils.bKing
    
    
    def getPossibleActions(self, state):

        r = state.m_agentPos[0]
        c = state.m_agentPos[1]
        oponent_color = -1
        l = []

        if (self.m_color == 0):  # White King
            oponent_color = 1
        else:                   # Black King
            oponent_color = 0

        # Para cada movimiento, lo primero que comprobamos es que esa casilla esté dentro del tablero. Después, nos aseguramos de que está vacía.
        # En la segunda parte de la OR, comprobamos que estamos en los límites, y que la ficha que ocupa la casilla es del color del oponente para poder comérnosla
        
        if ((r > 0 and state.m_board[r-1][c] == Utils.empty) 
            or (r > 0 and  state.m_board[r-1][c] != Utils.empty and Utils.getColorPiece(state.m_board[r-1][c]) == oponent_color)): 
            l.append(Action(state.m_agentPos, Position(r-1,c)))                 # Movimiento hacia arriba
        
        if ((c < state.m_boardSize-1 and state.m_board[r][c+1] == Utils.empty) 
            or (c < state.m_boardSize-1 and state.m_board[r][c+1] != Utils.empty and Utils.getColorPiece(state.m_board[r][c+1]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r,c+1)))                 # Movimiento hacia drcha
        
        if ((c > 0 and state.m_board[r][c-1] == Utils.empty) 
            or (c > 0 and state.m_board[r][c-1] != Utils.empty and Utils.getColorPiece(state.m_board[r][c-1]) == oponent_color)):      
            l.append(Action(state.m_agentPos, Position(r,c-1)))                 # Movimiento hacia izqda
        
        if ((r < state.m_boardSize-1 and state.m_board[r+1][c] == Utils.empty) 
            or (r < state.m_boardSize-1 and state.m_board[r+1][c] != Utils.empty and Utils.getColorPiece(state.m_board[r+1][c]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r+1,c)))                 # Movimiento hacia abajo


			
        if ((r > 0 and c > 0 and state.m_board[r-1][c-1] == Utils.empty) 
            or (r > 0 and c > 0 and state.m_board[r-1][c-1] != Utils.empty and Utils.getColorPiece(state.m_board[r-1][c-1]) == oponent_color)):     
            l.append(Action(state.m_agentPos, Position(r-1,c-1)))               # Diagonal arriba izqda
			
        if ((r > 0 and c < state.m_boardSize-1 and state.m_board[r-1][c+1] == Utils.empty) 
            or (r > 0 and c < state.m_boardSize-1 and state.m_board[r-1][c+1] != Utils.empty and Utils.getColorPiece(state.m_board[r-1][c+1]) == oponent_color)): 
            l.append(Action(state.m_agentPos, Position(r-1,c+1)))               # Diagonal arriba derecha
        
        if ((r < state.m_boardSize-1 and c < state.m_boardSize-1 and state.m_board[r+1][c+1] == Utils.empty) 
            or (r < state.m_boardSize-1 and c < state.m_boardSize-1 and state.m_board[r+1][c+1] != Utils.empty and Utils.getColorPiece(state.m_board[r+1][c+1]) == oponent_color)): 
            l.append(Action(state.m_agentPos, Position(r+1,c+1)))               # Diagonal abajo derecha
        
        if ((r < state.m_boardSize-1 and c > 0 and state.m_board[r+1][c-1] == Utils.empty) 
            or (r < state.m_boardSize-1 and c > 0 and state.m_board[r+1][c-1] != Utils.empty and Utils.getColorPiece(state.m_board[r+1][c-1]) == oponent_color)):    
            l.append(Action(state.m_agentPos, Position(r+1,c-1)))               # Diagonal abajo izqda

			
        if self.m_type == Utils.wKing or l == []:
            return l
        else:
            l.reverse()
            return l
        
    def getUtility(self, pos):
        if self.m_color == 0:	# Para las blancas
            utilidad = self.utilidad + self.ut_king_pos[pos[0]][pos[1]]
            return utilidad 
        else:					# Para las negras
            utilidad = (-1 * self.utilidad) + (-1 * self.ut_king_pos[7 - pos[0]][pos[1]])
            return utilidad 
