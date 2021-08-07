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

cadena = "$ {:,}                                                      {}:{}"
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
                "   (0) Empezar apuesta  ", "   (1) Salir del juego    "]

print(Rs_funciones.resultado_usuario_bool(cadena, final_cadena, concursante))
