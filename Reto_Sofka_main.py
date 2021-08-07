import Reto_Sofka_funciones
import Reto_Sofka_funciones as Rs_funciones
from datetime import datetime
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


concursante = Rs_funciones.concursante()
cadena = "$ {:,}                                                      {}:{}"


def barra_estado():
    now = datetime.now()
    Reto_Sofka_funciones.limpiar_consola()
    print(cadena.format(concursante.dinero, now.hour, now.minute))
    print("¯" * (len(cadena) + 2) + '\n')


usuario_input = "error"
while usuario_input == "error":
    barra_estado()

    cadena2 = " Bienvenido a apuestas deportivas ".upper()
    print(cadena2.center(len(cadena) + 2, "="))
    cadena2 = " La avaricia  ".lower()
    print(cadena2.center(len(cadena) + 2, "=") + '\n' + '\n')
    print("   (0) Empezar apuesta  ")
    print("   (1) Salir del juego    ")

    usuario_input = Reto_Sofka_funciones.input_usuario("    ", 0, 1)
