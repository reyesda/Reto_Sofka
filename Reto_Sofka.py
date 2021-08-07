import random
import time
import os

# Definición de funciones _____________________________________________________________


# función para limpiar consola
def limpiar_consola():
    # identifica el sistema operativo
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# función para validar entrada de usuario
def input_usuario(texto, valor_inferior=0, valor_superior=1000000):
    try:
        in_usu = float(input(texto))
        # se mira si esta dentro del rango permisible
        if in_usu in range(valor_inferior, valor_superior):
            return in_usu
    # se mira si entrega un valor diferente a un float
    except ValueError:
        pass
        # print("input no valido")


# función para escribir documento con las estadísticas
def reporte_estadistica(resultados_estadisticas):
    with open("result.txt", "w") as dt_r:
        cadena = "Reporte estadisticas".capitalize()
        dt_r.write(cadena.center(60, "=") + '\n' + '\n')
        dt_r.write("Numero de carreras totales realizadas: {}".format(resultados_estadisticas[3]) + '\n' + '\n')
        dt_r.write("Corredor     juegos ganados      porcentaje victorias " + '\n')

        for i in range(len(resultados_estadisticas[0])):
            dt_r.write("{}             {}                 {}%".format(data[1][i], resultados_estadisticas[0][i],
                                                                      resultados_estadisticas[1][i]) + '\n')

        dt_r.write('\n' + "Numero de veces en el podio" + '\n')
        for i in range(len(resultados_estadisticas[0])):
            dt_r.write("{}             {} ".format(data[1][i], resultados_estadisticas[2][i]) + '\n')

        dt_r.write('\n' + "Ganadores ultimas 3 carreras: ")
        for i in resultados_estadisticas[4]:
            dt_r.write("{}   ".format(data[1][i]))


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

    reporte_estadistica(resultados_estadisticas)
    # return resultados_estadisticas


# función para graficar la carrera
def dibujar_carros(nombres, figuras, porcentajes, llego):
    maximo_casillas = 70  # máximos caracteres en pantalla
    # se imprime el porcentaje de avance de cada corredor
    print(nombres + "  [" + "░" * round(maximo_casillas * porcentajes) + figuras +
          "-" * round(maximo_casillas * (1 - porcentajes)) + "] " + "$" * int(llego))


# escribir en la última línea del archivo
def actualizar_archivo():
    with open("data.txt", "a") as dt2:
        # transformar lista en string y agregar un salto de línea
        if podio1.resultado:
            dt2.write(",".join(map(str, podio1.resultado)) + '\n')


# leer archivo
def leer_archivo():
    global data
    with open("data.txt", "r") as dt:
        # extraer líneas, borrar salto de línea, separar por comas
        data = [linea.rstrip('\n').split(",") for linea in dt]
        # transformar primer elemento a int
        data[0] = [int(i) for i in data[0]]


# Definición de funciones _____________________________________________________________

# Definición de clases  _______________________________________________________________


# clase del jugador / corredor
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

        self.porcentaje_carrera = 0

    def comprobar(self):  # verifica si ya llegó a la meta
        if self.posicion == self.distancia * 1000:  # convierte distancia a metros
            self.ganador = True

        self.porcentaje_carrera = self.posicion / (self.distancia * 1000)


class pista:  # crea el objeto que almacena todos los carriles
    def __init__(self):
        self.carriles = []

    # llena “carriles” con todos los objetos carriles
    def llenar_carriles(self, identificador, nombre, figura, distancia):
        for i in range(len(identificador)):
            self.carriles.append(carril(identificador[i], nombre[i], figura[i], distancia))

    # llama el método de avanzar para los carros y verificar si ganaron
    def avanzar(self):
        # limpiar_consola()

        for i in self.carriles:
            i.desplazamiento(i.distancia)
            i.comprobar()

            #  dibujar_carros(i.nombre, i.figura, i.porcentaje_carrera, i.ganador)

        #  time.sleep(0.2)


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


class concursante:
    def __init__(self):
        self.dinero = 10000
        self.turnos = 0
        self.riesgo = 0

    def balance_dinero(self, diferencia):
        self.dinero += diferencia


# Definición de clases  _______________________________________________________________

# Main  _______________________________________________________________

data = []
leer_archivo()
distancia1 = 20  # en kilometros

pista1 = pista()
podio1 = podio()

pista1.llenar_carriles(data[0], data[1], data[2], distancia1)

podio1.guardar_ganador(pista1)
podio1.ordenar_resultado()

estadisticas()
actualizar_archivo()
