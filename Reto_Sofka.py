class jugador:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre


class carro(jugador):
    def __init__(self, identificador, nombre, color, posicion):
        jugador.__init__(self, identificador, nombre)

        self.color = color
        self.posicion = posicion


class carril(carro):
    def __init__(self, identificador, nombre, color, posicion, distancia, ganador):
        carro.__init__(self, identificador, nombre, color, posicion)

        self.distancia = distancia
        self.ganador = ganador


pista = [carril(1, "marcos", "rojo", 0, 2, False), carril(2, "daniel", "verde", 0, 2, False)]
