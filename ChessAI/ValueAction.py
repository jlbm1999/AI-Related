
# Aquí guardamos las acciones junto con su valor
class ValueAction():
    valor = 0
    action = None

    def __init__(self, a, v):
        self.valor = v
        self.action = a