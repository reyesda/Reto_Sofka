import random


class jugador:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre


class carro(jugador):
    def __init__(self, identificador, nombre, figura):
        jugador.__init__(self, identificador, nombre)

        self.figura = figura
        self.posicion = 0  # esta en metros

    def desplazamiento(self, limite):
        self.posicion += random.randint(1, 6) * 100
        self.posicion = self.posicion if self.posicion <= (limite * 1000) else limite * 1000


class carril(carro):
    def __init__(self, identificador, nombre, figura, distancia):
        carro.__init__(self, identificador, nombre, figura)

        self.distancia = distancia  # esta en kilometros
        self.ganador = False

    def comprobar(self):
        if self.posicion == self.distancia * 1000:
            self.ganador = True


