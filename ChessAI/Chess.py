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
from time import time
from Modos_de_Juego import Modos_de_Juego




if __name__ == '__main__':

    metodo = None
    inicio = None
    profundidad = None
    color = None
    max_jugadas = None
    seed = None
    probabilidad = None

    if (len(sys.argv) < 8):
        print("\n**Sorry, correct usage require 5 params:")
        print("Método: string.")
        print("Inicio: boolean")
        print("Profundidad: int.")
        print("Color: white/black, todo, dummy. Cada una de estas opciones corresponde a una manera distinta de jugar")
        print("Max-jugadas: int. Número de jugadas que se realizarán.")
        print("Seed: int. To initialize the problem instance random number generator (for reproducibility)")
        print("Probabilidad: [0, 1]. Probabilidad de que aparezcan ciertas piezas aleatoriamente.")
        sys.exit()

    else:
        metodo = (sys.argv[1])
        inicio = (sys.argv[2])
        profundidad = int(sys.argv[3])
        color = (sys.argv[4])
        max_jugadas = int(sys.argv[5])
        seed = int(sys.argv[6])
        probabilidad = float(sys.argv[7])

        if metodo != "alfabeta" and metodo != "minimax":
            print("\nSorry: método incorrecto.")
            size = 4

        if color != "white/black" and color != "todo" and color != "dummy":
            print("\nSorry: modo de juego incorrecto.")
            density=0.25

        if inicio == "True":
            initState = Utils.getChessInstance(probabilidad, seed)  # Instancia inicial
        if inicio == "False":
            initState = Utils.getChessInstancePosition(probabilidad, seed)

    Utils.printBoard(initState)
    search = Modos_de_Juego(initState, metodo, profundidad, color, max_jugadas, True)   # True para que jueguen las blancas por defecto.
    search.doSearch()

