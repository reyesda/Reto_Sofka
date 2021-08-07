import Reto_Sofka_funciones as Rs_funciones

# datos = Rs_funciones.leer_archivo()
# pista = Rs_funciones.pista()
# podio = Rs_funciones.podio()
#
# pista.llenar_carriles(datos[0], datos[1], datos[2])
#
# podio.guardar_ganador(pista)
# podio.ordenar_resultado()
#
# Rs_funciones.estadisticas(datos)
# Rs_funciones.actualizar_archivo(podio)

cadena = " Tu cuenta bancaria: $ {:,}                                                   {}:{}"
game_over = False

while game_over is False:
    # lectura archivos e inicializacion de variables
    datos = Rs_funciones.leer_archivo()
    pista = Rs_funciones.pista()
    podio = Rs_funciones.podio()

    concursante = Rs_funciones.concursante()
    concursante.dinero = 500

    pista.llenar_carriles(datos[0], datos[1], datos[2])

    final_cadena = [Rs_funciones.centro_caracter(" Bienvenido a apuestas deportivas ", cadena),
                    Rs_funciones.centro_caracter(" La avaricia  ", cadena) + '\n' + '\n',
                    "   (1) Empezar apuesta  (-$500)", "   (0) Salir del juego    "]

    if Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante):
        if concursante.dinero > 1500:
            pass
        else:
            game_over = True

            final_cadena = [Rs_funciones.centro_caracter(" Bienvenido a apuestas deportivas ", cadena),
                            Rs_funciones.centro_caracter(" La avaricia  ", cadena) + '\n' + '\n',
                            "   No tienes suficiente dinero ", "   (0) Salir del juego    "]

            Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante)

    else:
        game_over = True
