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
    def __init__(self, identificador, nombre, color, posicion, distancia, ganador):
        carro.__init__(self, identificador, nombre, color, posicion)

        self.distancia = distancia
        self.ganador = ganador


pista = [carril(1, "marcos", "rojo", 0, 2, False), carril(2, "daniel", "verde", 0, 2, False)]
