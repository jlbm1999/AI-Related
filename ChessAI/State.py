# This class contains the information needed to represent a state 
# and some useful methods

import sys
import copy
import Utils
from Position import Position
from Action import Action
from Piece import Piece
from Rook import Rook
from Pawn import Pawn
from King import King
from Knight import Knight
from Queen import Queen
from Bishop import Bishop

class State:
	m_board = None
	m_agentPos = None
	m_agentPos_white = []
	m_agentPos_black = []
	m_agent = -1 # the type of piece
	m_color = 0  # 0 for white, 1 for black
	m_boardSize = -1 
	m_piece = Piece()
	blancas = []		# Lista con las piezas blancas
	negras = []			# Lista con las piezas negras
	applied_action = None
	profundidad = None
	rey_blancas = False
	rey_negras = False


	utilidad_total = []

	
	def __init__(self, board):
		self.m_board = board
		self.m_boardSize = len(board[0])


	# compares if the current state is final
	def isFinal(self):
		# Devuelve True si alguno de los 2 reyes no está
		if 11 not in self.negras:	
			self.rey_negras = True

		if 5 not in self.blancas:
			self.rey_blancas = True

		return self.rey_blancas or self.rey_negras

	
	# hard copy of an State
	def copy(self, memodict={}):
		# print '__deepcopy__(%s)' % str(memo)
		# newState = State(self.m_board, self.m_agentPos, self.m_agent)
		newState = State(self.m_board)
		newState.__dict__.update(self.__dict__)
		newState.m_agentPos = copy.deepcopy(self.m_agentPos, memodict)
		newState.m_agent = copy.deepcopy(self.m_agent, memodict)
    
		return newState
		
	# apply a given action over the current state -which remains unmodified. Return a new state
	def applyAction(self,action):
		newState = self.copy()
		pieza = newState.m_board[action.m_initPos[0]][action.m_initPos[1]]
		newState.m_board[action.m_initPos[0]][action.m_initPos[1]] = Utils.empty
		newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = pieza
		newState.m_agentPos = action.m_finalPos
		
		return newState
		
	# Calcular la utilidad de un estado por cada pieza que tenemos disponible en el tablero.
	# Puesto que vamos a copiar el estado muchas veces, el valor de la utilidad puede acumularse. Si lo inicializamos a 0 ahora,
	# nos aseguramos de que cada vez que se ejecuta esta función, la utilidad se calcula correctamente
	def calculaUtilidad(self, turno):
		self.utilidad_total = 0	
		utilidad_b = 0
		utilidad_n = 0
		piezas_b = []
		piezas_n = []

		piezas_b = self.calculaPiezasDisponibles(True)
		for i in range(len(piezas_b)):	# Calculamos la utilidad de las piezas blancas		

			if piezas_b[i].m_type == 0:				# Si es un peón blanco
				utilidad_b = utilidad_b + piezas_b[i].getUtility(self.m_agentPos_white[i])
			elif piezas_b[i].m_type == 1:			# Si es una torre blanca
				utilidad_b = utilidad_b + piezas_b[i].getUtility(self.m_agentPos_white[i])
			elif piezas_b[i].m_type == 2:			# Si es un alfil blanco
				utilidad_b = utilidad_b + piezas_b[i].getUtility(self.m_agentPos_white[i])
			elif piezas_b[i].m_type == 3:			# Si es un caballo blanco
				utilidad_b = utilidad_b + piezas_b[i].getUtility(self.m_agentPos_white[i])
			elif piezas_b[i].m_type == 4:			# Si es una reina blanca
				utilidad_b = utilidad_b + piezas_b[i].getUtility(self.m_agentPos_white[i])
			elif piezas_b[i].m_type == 5:			# Si es un rey blanco
				utilidad_b = utilidad_b + piezas_b[i].getUtility(self.m_agentPos_white[i])
    
		piezas_n = self.calculaPiezasDisponibles(False)
		for i in range(len(piezas_n)):	# Calculamos la utilidad de las piezas negras

			if piezas_n[i].m_type == 6:				# Si es un peón negro
				utilidad_n = utilidad_n + piezas_n[i].getUtility(self.m_agentPos_black[i])
			elif piezas_n[i].m_type == 7:			# Si es una torre negra
				utilidad_n = utilidad_n + piezas_n[i].getUtility(self.m_agentPos_black[i])
			elif piezas_n[i].m_type == 8:			# Si es un alfil negro
				utilidad_n = utilidad_n + piezas_n[i].getUtility(self.m_agentPos_black[i])
			elif piezas_n[i].m_type == 9:			# Si es un caballo negro
				utilidad_n = utilidad_n + piezas_n[i].getUtility(self.m_agentPos_black[i])
			elif piezas_n[i].m_type == 10:			# Si es una reina negra
				utilidad_n = utilidad_n + piezas_n[i].getUtility(self.m_agentPos_black[i])
			elif piezas_n[i].m_type == 11:			# Si es un rey negro
				utilidad_n = utilidad_n + piezas_n[i].getUtility(self.m_agentPos_black[i])


		return utilidad_b + utilidad_n

	# Devolverá la diferencia de piezas. Cuanto mayor sea el número, mejor para las blancas, y viceversa para las piezas negras
	def calculaHeuristica(self):
		return len(self.blancas) - len(self.negras)


	
	# Método que devolverá las posibles acciones que puede realizar un jugador
	def getPossibleActions(self, turno):
		acciones = []
		a_devolver = []
		piezas = self.calculaPiezasDisponibles(turno)			# En piezas almacenamos los agentes que se podrán mover
		for i in range(len(piezas)):
			if turno:
				self.m_agentPos = self.m_agentPos_white[i]		# Actualizamos el agente
			else:
				self.m_agentPos = self.m_agentPos_black[i]
			acciones.append(piezas[i].getPossibleActions(self))	# Introducimos la acción y las devolvemos
		for i in acciones:
			if i != []:
				for j in i:
					a_devolver.append(j)
		return a_devolver
	# Devolvemos a_devolver porque no eliminaba correctamente las listas vacías, así que pasamos lo que no es vacío a la lista a_devolver

	######################## MÉTODOS PARA CALCULAR QUÉ PIEZAS TIENE CADA JUGADOR ##########################

	# Devuelve una lista con las piezas que tiene disponible cada jugador
	def getPieces(self, turno):
		if turno:
			self.blancas = []
			self.m_agentPos_white = []
			for i in range(len(self.m_board)):
				for j in range(len(self.m_board[i])):				# Recorremos el tablero entero, y por cada pieza que nos sirve, nos la guardamos en blancas
					if self.m_board[i][j] < 6:						# y guardamos su posición en agentPos_w. Lo mismo para las negras.
						self.blancas.append(self.m_board[i][j])
						self.m_agentPos_white.append((i, j))
			return self.blancas
		else:		
			self.negras = []
			self.m_agentPos_black = []
			for i in range(len(self.m_board)):
				for j in range(len(self.m_board[i])):
					if self.m_board[i][j] >= 6 and self.m_board[i][j] < 12:	# Menor que 12 para no contar los espacion en blanco
						self.negras.append(self.m_board[i][j])
						self.m_agentPos_black.append((i, j))
			return self.negras
	
	# Inicializa todas las piezas del tablero. Es igual que getPieces(), pero inicializa todas, no solo las del jugador al que le toca jugar
	def inicializaPiezas(self):
		self.blancas = []
		self.m_agentPos_white = []
		for i in range(len(self.m_board)):
			for j in range(len(self.m_board[i])):				# Recorremos el tablero entero, y por cada pieza que nos sirve, nos la guardamos en blancas
				if self.m_board[i][j] < 6:						# y guardamos su posición en agentPos_w. Lo mismo para las negras.
					self.blancas.append(self.m_board[i][j])		# Guardamos la pieza en la lista
					self.m_agentPos_white.append((i, j))		# Nos guardamos su posición en la lista
		
		self.negras = []
		self.m_agentPos_black = []
		for i in range(len(self.m_board)):
			for j in range(len(self.m_board[i])):
				if self.m_board[i][j] >= 6 and self.m_board[i][j] < 12:	# Menor que 12 para no contar los espacion en blanco
					self.negras.append(self.m_board[i][j])
					self.m_agentPos_black.append((i, j))

    # Devuelve las piezas que tiene disponible un jugador en forma de lista de objetos
	def calculaPiezasDisponibles(self, turno):
		piezas_disponibles_obj = []						               # Almacenamos los objetos Piece en la lista
		copiaEstado = copy.deepcopy(self.copy())                       # Copiamos el estado
		piezas_disponibles = copiaEstado.getPieces(turno)              # Obtenemos las piezas que puede mover el jugador (la lista es numérica, es decir, no pasamos objetos pieza sino números)
		self.blancas = copy.deepcopy(copiaEstado.blancas)
		self.m_agentPos_white = copy.deepcopy(copiaEstado.m_agentPos_white)
		self.negras = copy.deepcopy(copiaEstado.negras)
		self.m_agentPos_black = copy.deepcopy(copiaEstado.m_agentPos_black)
		
		for i in range(len(piezas_disponibles)):                                 				# Por cada pieza que tenga el agente
			if turno:
				piezas_disponibles_obj.append(copiaEstado.definePieza(piezas_disponibles[i]))	# La declaramos
			else:
				piezas_disponibles_obj.append(copiaEstado.definePieza(piezas_disponibles[i]))

		# Devolvemos una lista de piezas
		return (piezas_disponibles_obj)		

	# Función para definir como objetos las diferentes piezas que tiene cada jugador
	def definePieza(self, pieza):

		if pieza == Utils.wPawn: 
			self.m_piece = Pawn(0)
			return self.m_piece
		elif pieza == Utils.bPawn:
			self.m_piece = Pawn(1)
			return self.m_piece
		elif pieza == Utils.wQueen:
			self.m_piece = Queen(0)
			return self.m_piece
		elif pieza == Utils.bQueen:
			self.m_piece = Queen(1)
			return self.m_piece
		elif pieza == Utils.wRook: 
			self.m_piece = Rook(0)
			return self.m_piece
		elif pieza == Utils.bRook:
			self.m_piece = Rook(1)
			return self.m_piece
		elif pieza == Utils.wKing:
			self.m_piece = King(0)
			return self.m_piece
		elif pieza == Utils.bKing:
			self.m_piece = King(1)
			return self.m_piece
		elif pieza == Utils.wKnight:
			self.m_piece = Knight(0)
			return self.m_piece
		elif pieza == Utils.bKnight:
			self.m_piece = Knight(1)
			return self.m_piece
		elif pieza == Utils.wBishop:
			self.m_piece = Bishop(0)
			return self.m_piece
		elif pieza == Utils.bBishop:
			self.m_piece = Bishop(1)
			return self.m_piece
		else:
			print("Chess piece not implemented")
			sys.exit()

