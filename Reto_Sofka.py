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


class pista:
    def __init__(self):
        self.carriles = []

    def llenar_carriles(self, identificador, nombre, figura, distancia):
        for i in range(len(identificador)):
            self.carriles.append(carril(identificador[i], nombre[i], figura[i], distancia))

    def avanzar(self):
        for i in self.carriles:
            i.desplazamiento(i.distancia)
            i.comprobar()


class podio:
    def __init__(self):
        self.orden_llegada = []
        self.resultado = []

    def guardar_ganador(self, objeto_pista):
        while len(self.orden_llegada) < len(objeto_pista.carriles):
            objeto_pista.avanzar()

            for i in objeto_pista.carriles:
                if i.identificador not in self.orden_llegada:
                    if i.ganador is True:
                        self.orden_llegada.append(i.identificador)

    def ordenar_resultado(self):
        for i in range(len(self.orden_llegada)):
            self.resultado.append(self.orden_llegada.index(i) + 1)


identificador1 = [0, 1, 2, 3, 4]
nombre1 = ["Marcos", "Daniel", "Andres", "Valentina", "Juan"]
figura1 = ["]■>", "}■>", ")■>", "╠■>", "#■>"]
distancia1 = 4

pista1 = pista()
podio1 = podio()

pista1.llenar_carriles(identificador1, nombre1, figura1, distancia1)

podio1.guardar_ganador(pista1)
podio1.ordenar_resultado()

print(podio1.resultado)
