import random


class jugador:
    def __init__(self, identificador, nombre):
        self.identificador = identificador  # para asignar su lugar las listas
        self.nombre = nombre


class carro(jugador):  # hereda de jugador
    def __init__(self, identificador, nombre, figura):
        jugador.__init__(self, identificador, nombre)

        self.figura = figura  # para graficar los carros
        self.posicion = 0  # esta en metros

    def desplazamiento(self, limite):  # para mover los carros aleatoriamente por el carril
        self.posicion += random.randint(1, 6) * 100  # regla de desplazamiento, en metros

        # se limita el desplazamiento máximo al tamaño del carril
        self.posicion = self.posicion if self.posicion <= (limite * 1000) else limite * 1000


class carril(carro):  # hereda de carro
    def __init__(self, identificador, nombre, figura, distancia):
        carro.__init__(self, identificador, nombre, figura)

        self.distancia = distancia  # está en kilometros
        self.ganador = False  # indica si ya llegó a la meta

    def comprobar(self):  # verifica si ya llegó a la meta
        if self.posicion == self.distancia * 1000:  # convierte distancia a metros
            self.ganador = True


class pista:  # crea el objeto que almacena todos los carriles
    def __init__(self):
        self.carriles = []

    # llena “carriles” con todos los objetos carriles
    def llenar_carriles(self, identificador, nombre, figura, distancia):
        for i in range(len(identificador)):
            self.carriles.append(carril(identificador[i], nombre[i], figura[i], distancia))

    # llama el método de avanzar para los carros y verificar si ganaron
    def avanzar(self):
        for i in self.carriles:
            i.desplazamiento(i.distancia)
            i.comprobar()


class podio:  # clase para guardar la posición de llegada
    def __init__(self):
        # almacena en orden los identificadores de quienes terminan la carrera
        # orden_llegada [0] = 2, quiere decir que el conductor con indicador “2” quedó en primer puesto
        self.orden_llegada = []
        # almacena la posición en la que quedo cada corredor (cada índice según identificador)
        # resultado [0] = 1, quiere decir que el conductor con indicador “0” quedó en primer puesto
        self.resultado = []

    # llena orden_llegada con el indicador de los corredores en orden de llegada
    def guardar_ganador(self, objeto_pista):
        while len(self.orden_llegada) < len(objeto_pista.carriles):
            # avanzan todos los carros hasta que todos hayan terminado
            objeto_pista.avanzar()

            # se detecta quien ganó y se guarda en la lista
            for i in objeto_pista.carriles:
                if i.identificador not in self.orden_llegada:
                    if i.ganador is True:
                        self.orden_llegada.append(i.identificador)

    # cambia el formato de orden_llegada al de resultado
    def ordenar_resultado(self):
        for i in range(len(self.orden_llegada)):
            # busca el indicador del jugador y lo guarda en su index
            self.resultado.append(self.orden_llegada.index(i) + 1)


# leer archivo
with open("data.txt", "r") as dt:
    # extraer líneas, borrar salto de línea, separar por comas
    data = [linea.rstrip('\n').split(",") for linea in dt]
    # transformar primer elemento a int
    data[0] = [int(i) for i in data[0]]


distancia1 = 4  # en kilometros

pista1 = pista()
podio1 = podio()

pista1.llenar_carriles(data[0], data[1], data[2], distancia1)

podio1.guardar_ganador(pista1)
podio1.ordenar_resultado()

# escribir en la última línea del archivo
with open("data.txt", "a") as dt:
    # transformar lista en string y agregar un salto de línea
    if podio1.resultado:
        dt.write(",".join(map(str, podio1.resultado)) + '\n')

# print(podio1.resultado)


# función para calcular las estadísticas de los corredores
def estadisticas():
    total_primero = [0, 0, 0, 0, 0]  # indica el numero de veces que el corredor a quedado de primero
    veces_podio = [0, 0, 0, 0, 0]  # indica el numero de veces que el corredor queda en los 3 primeros
    total_partidas = len(data) - 3  # indica el numero de veces que se han guardado partidas
    ultimos_ganadores = []  # guarda los 3 últimos ganadores

    for i in range(3, len(data)):
        # transformar todos los elementos a int
        data[i] = [int(j) for j in data[i]]

        # recorre cada lista de resultado
        for t in range(len(data[i])):
            # busca que corredor quedó de primero
            if data[i][t] == 1:
                # sumas las victorias del corredor
                total_primero[t] += data[i][t]

                # encuentra los últimos 3 ganadores
                if i >= len(data) - 3:
                    ultimos_ganadores.append(t)

            # identifica si el corredor estuvo dentro de los 3 primeros
            if data[i][t] <= 3:
                veces_podio[t] += 1

    # calcula el porcentaje de victorias de los corredores
    procentaje_primero = [round((i / sum(total_primero)) * 100) for i in total_primero if i != 0]

    # guarda todas las variables es “resultados_estadisticas”
    resultados_estadisticas = [total_primero, procentaje_primero, veces_podio, total_partidas, ultimos_ganadores]

    return resultados_estadisticas


# print(estadisticas())

# función para graficar la carrera
def dibujar_carros(nombres, figuras, porcentajes):
    maximo_casillas = 70  # máximos caracteres en pantalla
    for i in range(len(nombres)):
        # se imprime el porcentaje de avance de cada corredor
        print(nombres[i] + "  [" + ("░" * round(maximo_casillas * porcentajes[i])) + figuras[i] +\
              ("-" * round(maximo_casillas * (1 - porcentajes[i]))) + "] ")


por = [0.9, 1, 0.8, 1, 0.95]
dibujar_carros(data[1], data[2], por)
