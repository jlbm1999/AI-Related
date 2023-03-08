
# Clase donde se modelarán los algoritmos de búsqueda en juegos
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



class Algoritmos:

    def __init__(self, metodo):
        self.metodo = metodo

        ############### MÉTODOS MIN Y MAX PARA AMBOS ALGORITMOS #################

        # Este método define el comportamiento del jugador MAX para alfabeta
    def MaxValor(self, state, profundidad, turno, alpha, beta):
        # v representa una acción junto con su utilidad asociada
        v = ValueAction(None, 0)

        # Si algún jugador pierde la partida 
        if state.isFinal():
            v.valor = state.calculaUtilidad(not turno)                          # Calculamos la utilidad del estado
            return v

        # Si nos encontramos en el nodo hoja del árbol
        if profundidad == 0:
            v.valor = state.calculaHeuristica()                                 # Calculamos la heurística del estado
            return v

        v.valor = -999999999999999
        sucesores = []                                                  
        sucesores = state.getPossibleActions(turno)                         # Almacenamos en sucesores una lista con los posibles movimientos que tiene disponible el jugador
        while sucesores:                                                    # Mientras queden movimientos
            action = sucesores.pop(0)                                       # Nos quedamos con su acción
            nuevoEstado = copy.deepcopy(state.copy())                       # Generamos un estado hijo
            nuevoEstado = nuevoEstado.applyAction(action)                   # Le aplicamos la acción
            new_v = self.MinValor(nuevoEstado, profundidad - 1, not turno, alpha, beta)       # Almacenamos el valor del Min
            if new_v.valor > v.valor:                                       # Si maximizamos el valor, actualizamos 
                v.valor = new_v.valor
                v.action = action
            if self.metodo == 'alfabeta':
                if v.valor >= beta:
                    return v
                alpha = max(alpha, v.valor)
        return v                                                            # Devolvemos el objeto v, con su valor y su acción asociada

    # Este método define el comportamiento del jugador MIN para alfabeta
    def MinValor(self, state, profundidad, turno, alpha, beta):
        # v representa una acción junto con su utilidad asociada
        v = ValueAction(None, 0)

        # Si algún jugador pierde la partida 
        if state.isFinal():
            v.valor = state.calculaUtilidad(not turno)                          # Calculamos la utilidad del estado
            return v

        # Si nos encontramos en el nodo hoja del árbol
        if profundidad == 0:
            v.valor = state.calculaHeuristica()                                 # Calculamos la heurística del estado
            return v
        
        v.valor = 999999999999999
        sucesores = []                                                  
        sucesores = state.getPossibleActions(turno)                         # Almacenamos en sucesores una lista con los posibles movimientos que tiene disponible el jugador
        while sucesores:                                                    # Mientras queden movimientos
            action = sucesores.pop(0)                                       # Nos quedamos con su acción
            nuevoEstado = copy.deepcopy(state.copy())                       # Generamos un estado hijo
            nuevoEstado = nuevoEstado.applyAction(action)                   # Lo aplicamos
            new_v = self.MaxValor(nuevoEstado, profundidad - 1, not turno, alpha, beta)       # Almacenamos el valor del Max
            if new_v.valor < v.valor:                                       # Si minimizamos el valor, actualizamos 
                v.valor = new_v.valor
                v.action = action

            if self.metodo == 'alfabeta':
                if v.valor <= alpha:
                    return v
                beta = min(beta, v.valor)
        return v                                                            # Devolvemos el objeto v, con su valor y su acción asociada


    
