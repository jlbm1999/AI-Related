# Clase donde se modelarán los modos de juego
import sys
import random
import Utils
from Position import Position
from Action import Action
from State import State
from Piece import Piece
from Rook import Rook
from Pawn import Pawn
from King import King
from Knight import Knight
from Queen import Queen
from Bishop import Bishop
import copy
from ValueAction import ValueAction
from Algoritmos import Algoritmos


class Modos_de_Juego:

    state = None
    turno_blancas = True
    metodo = None
    inicio = None
    profundidad = None
    color = None
    max_jugadas = None
    m_piece = None
    algoritmo = None
    alpha = None
    beta = None
    
    def __init__(self, state, metodo, profundidad, color, max_jugadas, turno):
        self.state = state                  
        self.metodo = metodo                # Minimax o alfabeta
        self.profundidad = profundidad      # Profundidad que tendrán los árboles
        self.color = color                  # Máquina contra máquina / Máquina contra jugador / Máquina contra máquina parada
        if max_jugadas == -1:
            self.max_jugadas = 9999999
        else:
            self.max_jugadas = max_jugadas      # Máximo de jugadas que tendrá la partida

        self.turno_blancas = turno          # Si es True, es el turno de las blancas
        self.alpha = -999999999
        self.beta = 9999999999
        self.metodo = metodo
        
    # Método principal de la clase. Se encargará de llamar al algoritmo correspondiente
    def doSearch(self):
        
        # Modo de juego donde la máquina juega contra si misma
        if self.color == 'todo':
            self.jugarMaquina(self.state)

        # Modo de juego donde jugamos contra la máquina. Nosotros siempre somos las blancas
        elif self.color == 'white/black':
            self.jugarContraMaquina(self.state)

        # Modo de juego donde las blancas pueden moverse, pero las negras se quedan quietas
        else:
            self.dummy(self.state)

    # Este método contiene el modo de juego donde la máquina juega contra si mismo
    def jugarMaquina(self, state):
        self.algoritmo = Algoritmos(self.metodo)
        contador_turnos = 0
        while self.max_jugadas > 0:         # Mientras queden jugadas disponibles, sigue el juego
            contador_turnos += 1
            state.inicializaPiezas()        # Inicializamos todas las piezas del tablero

            # En v tendremos un objeto ValueAction, el cual contendrá una acción así como su valor de utilidad correspondiente
            if self.turno_blancas:
                if state.isFinal():
                    print("GANAN LAS NEGRAS")
                    sys.exit()
                v = self.algoritmo.MaxValor(state, self.profundidad, self.turno_blancas, self.alpha, self.beta)       # Como juegan las blancas, queremos maximizar la utilidad
                state.applyAction(v.action)                                     # Una vez obtenemos el mejor movimiento, lo aplicamos
                print()
                print('Juegan blancas - Turno ', contador_turnos, '\t')
                print('The agent ', self.getName(state.m_board[v.action.m_finalPos.row][v.action.m_finalPos.col]), ' moves from ', v.action.m_initPos, ' to ', (v.action.m_finalPos.row,v.action.m_finalPos.col))

            else:
                if state.isFinal():
                    print("GANAN LAS BLANCAS")
                    sys.exit() 
                v = self.algoritmo.MinValor(state, self.profundidad, self.turno_blancas, self.alpha, self.beta)
                state.applyAction(v.action)                                     # Una vez obtenemos el mejor movimiento, lo aplicamos      
                print()
                print('Juegan negras - Turno ', contador_turnos, '\t')
                print('The agent ', self.getName(state.m_board[v.action.m_finalPos.row][v.action.m_finalPos.col]), ' moves from ', v.action.m_initPos, ' to ', (v.action.m_finalPos.row,v.action.m_finalPos.col))

            Utils.printBoard(state)                             # Una vez aplicado el movimiento, mostramos como queda el tablero
            self.turno_blancas = not self.turno_blancas         # Cambiamos el turno para que juegue el jugador del otro color
            self.max_jugadas -= 1                               # Esta jugada termina, por lo que decrementa el contador
        

    # Este método contiene el modo de juego donde la máquina juega contra un jugador pasivo, es decir, que no mueve ninguna pieza, pero asumiendo que sus movimientos serían óptimos
    def dummy(self, state):
        self.algoritmo = Algoritmos(self.metodo)
        contador_turnos = 0
        while self.max_jugadas > 0:         # Mientras queden jugadas disponibles, sigue el juego
            contador_turnos += 1
            state.inicializaPiezas()        # Inicializamos todas las piezas del tablero
            if state.isFinal():
                    print("GANAN LAS BLANCAS")
                    sys.exit()
            v = self.algoritmo.MaxValor(state, self.profundidad, self.turno_blancas, self.alpha, self.beta)
            state.applyAction(v.action)                                     # Lo aplicamos
            print()
            print('Juegan blancas - Turno ', contador_turnos, '\t')
            print('The agent ', self.getName(state.m_board[v.action.m_finalPos.row][v.action.m_finalPos.col]), ' moves from ', v.action.m_initPos, ' to ', (v.action.m_finalPos.row,v.action.m_finalPos.col))

            # No cambiamos nunca de turno, aunque suponemos que el rival juega de manera óptima
            Utils.printBoard(state)                             # Mostramos como queda el tablero
            self.max_jugadas -= 1                               # Esta jugada termina, por lo que decrementa el contador
    
    # Este método contiene el modo de juego donde el jugador compite contra la máquina. El jugador siempre controla las fichas blancas.
    def jugarContraMaquina(self, state):
        self.algoritmo = Algoritmos(self.metodo)
        contador_turnos = 0
        while self.max_jugadas > 0:         # Mientras queden jugadas disponibles, sigue el juego

            contador_turnos += 1
            state.inicializaPiezas()            # Inicializamos todas las piezas del tablero
            if self.turno_blancas:              # Si es nuestro turno
                if state.isFinal():
                    print("GANAN LAS NEGREAS")
                    sys.exit()
                
                acciones = state.getPossibleActions(self.turno_blancas)
                print('Las acciones disponibles son:\t')
                for i in range(len(acciones)):
                    agente = state.m_board[acciones[i].m_initPos[0]][acciones[i].m_initPos[1]]
                    print(i, ': ', self.getName(agente), ' ', acciones[i].m_initPos, ' -> ', (acciones[i].m_finalPos.row, acciones[i].m_finalPos.col))
                siguiente_movimiento = int(input('\nEscriba el número del movimiento\n'))
                agente = state.m_board[acciones[siguiente_movimiento].m_initPos[0]][acciones[siguiente_movimiento].m_initPos[1]]          # Generamos al agente de la casilla inicial
                state.applyAction(acciones[siguiente_movimiento])         # Una vez tenemos el movimiento, lo aplicamos
                print()
                print('Juegan blancas - Turno ', contador_turnos, '\t')
                print('The agent ', agente, ' moves from ', acciones[siguiente_movimiento].m_initPos, ' to ', (acciones[siguiente_movimiento].m_finalPos.row, acciones[siguiente_movimiento].m_finalPos.col))
            else:
                if state.isFinal():
                    print("GANAN LAS BLANCAS")
                    sys.exit()
                v = self.algoritmo.MinValor(state, self.profundidad, self.turno_blancas, self.alpha, self.beta)
                state.applyAction(v.action)                                     # Una vez obtenemos el mejor movimiento, lo aplicamos 
                print()
                print('Juegan negras - Turno ', contador_turnos, '\t')
                print('The agent ', self.getName(state.m_board[v.action.m_finalPos.row][v.action.m_finalPos.col]), ' moves from ', v.action.m_initPos, ' to ', (v.action.m_finalPos.row,v.action.m_finalPos.col))

            Utils.printBoard(state)                             # Una vez aplicado el movimiento, mostramos como queda el tablero
            self.turno_blancas = not self.turno_blancas         # Cambiamos el turno para que juegue el jugador del otro color
            self.max_jugadas -= 1                               # Esta jugada termina, por lo que decrementa el contador

    # Este método sirve para representar que pieza se ha movido. Su propósito es mejorar la legibilidad del juego.
    def getName(self, boardPosition):
        if boardPosition == 0:
            return 'P'
        elif boardPosition == 1:
            return 'R'
        elif boardPosition == 2:
            return 'B'
        elif boardPosition == 3:
            return 'N'
        elif boardPosition == 4:
            return 'Q'
        elif boardPosition == 5:
            return 'K'
        elif boardPosition == 6:
            return 'p'
        elif boardPosition == 7:
            return 'r'
        elif boardPosition == 8:
            return 'b'
        elif boardPosition == 9:
            return 'n'
        elif boardPosition == 10:
            return 'q'
        elif boardPosition == 11:
            return 'k'
        