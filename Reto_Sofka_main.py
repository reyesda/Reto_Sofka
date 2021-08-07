import Reto_Sofka_funciones as Rs_funciones
import time

cadena = " Tu cuenta bancaria: $ {:,}                                                   {}:{}"
game_over = False

concursante = Rs_funciones.concursante()

while game_over is False:
    Rs_funciones.limpiar_consola()

    # lectura archivos e inicializacion de variables
    datos = Rs_funciones.leer_archivo()
    pista = Rs_funciones.pista()
    podio = Rs_funciones.podio()

    # concursante.dinero = 1600

    pista.llenar_carriles(datos[0], datos[1], datos[2])

    # variables para GUI
    estadisticas = False
    seleccionar_corredor = False

    final_cadena = [Rs_funciones.centro_caracter(" Bienvenido a apuestas deportivas ", cadena, "="),
                    Rs_funciones.centro_caracter(" La avaricia  ", cadena, "=") + '\n' + '\n',
                    "   (1) Empezar apuesta  (-$500)", "   (0) Salir del juego    "]

    if Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante):

        if concursante.dinero > 1500:
            concursante. dinero -= 500

            # concursante.dinero = 400
            final_cadena = [Rs_funciones.centro_caracter(" ¿Desea ver las estadísticas de los corredores?   ",
                                                         cadena, " ") + '\n' + '\n',
                            "   (1) Ver las estadísticas  (-$500)", "   (0) No    "]

            if Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante):
                concursante.dinero -= 500

                if concursante.dinero > 1000:
                    estadisticas = True
                else:
                    final_cadena = [Rs_funciones.centro_caracter(" ¿Desea ver las estadísticas de los corredores?   ",
                                                                 cadena, " ") + '\n' + '\n',
                                    "   No tienes suficiente dinero", "   (0) Continuar    "]

                    Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante)

                    seleccionar_corredor = True
            else:
                seleccionar_corredor = True
        else:
            game_over = True

            final_cadena = [Rs_funciones.centro_caracter(" Bienvenido a apuestas deportivas ", cadena, "="),
                            Rs_funciones.centro_caracter(" La avaricia  ", cadena, "=") + '\n' + '\n',
                            "   No tienes suficiente dinero ", "   (0) Salir del juego    "]

            Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante)

    else:
        game_over = True

    if not game_over and estadisticas:
        Rs_funciones.limpiar_consola()
        Rs_funciones.barra_estado(cadena, concursante)

        with open("result.txt", "r") as dt:
            # extraer líneas, borrar salto de línea, separar por comas
            data = [linea.rstrip('\n').split(",") for linea in dt]

        for i in data:
            print(i[0])

        time.sleep(13)

    if game_over is False:
        # ventana seleccionar corredor
        final_cadena = [Rs_funciones.centro_caracter(" Seleccione su corredor   ", cadena, " ") + '\n',
                        "   (0) Marcos", "   (1) Daneil    ", "   (2) Andres", "   (3) Camilo", "   (4) Wilson"]

        usuario_input = "error"
        while usuario_input == "error":
            Rs_funciones.barra_estado(cadena, concursante)

            for i in final_cadena:
                print(i)

            usuario_input = Rs_funciones.input_usuario("    ", 0, 4)

        concursante.elegido = usuario_input

        # ventana de la apuesta
        final_cadena = [Rs_funciones.centro_caracter(" ¿Cuánto va a apostar? ", cadena, " ") + '\n',
                        "   puede apostar desde $1,000 hasta ${:,}".format(concursante.dinero)]

        usuario_input = "error"
        while usuario_input == "error":
            Rs_funciones.barra_estado(cadena, concursante)

            for i in final_cadena:
                print(i)

            usuario_input = Rs_funciones.input_usuario("    ", 1000, concursante.dinero)

        concursante.apuesta = usuario_input
        concursante.dinero -= concursante.apuesta

        podio.guardar_ganador(pista)
        podio.ordenar_resultado()

        Rs_funciones.estadisticas(datos)
        Rs_funciones.actualizar_archivo(podio)

        # Ventana de resultados
        if podio.orden_llegada[0] == concursante.elegido:
            concursante.dinero += concursante.apuesta * 2.2

            final_cadena = [Rs_funciones.centro_caracter(" ¡Ganaste!  ", cadena, " ") + '\n',
                            "   Apostaste ${:,} y ganas ${:,}".format(concursante.apuesta, concursante.apuesta * 2.2),
                            "   (0) Continuar"]

            Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante)

        else:

            final_cadena = [Rs_funciones.centro_caracter(" ¡Sigue intentando!  ", cadena, " ") + '\n',
                            "   (0) Continuar"]

            Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante)

        # pantalla continuar jugando
        final_cadena = [Rs_funciones.centro_caracter(" ¿Desea seguir jugando?   ",
                                                     cadena, " ") + '\n' + '\n',
                        "   (1) Sí", "   (0) No    "]

        if Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante):
            pass
        else:
            game_over = True
    else:
        final_cadena = [Rs_funciones.centro_caracter(" ¡Gracias por jugar con nosotros! ", cadena, "*"),
                        Rs_funciones.centro_caracter(" Vuelva pronto  ", cadena, " ") + '\n',
                        "   (0) Para salir"]

        Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante)
