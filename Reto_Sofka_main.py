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


def barra_estado(str_in):
    now = datetime.now()
    Reto_Sofka_funciones.limpiar_consola()
    print(str_in.format(concursante.dinero, now.hour, now.minute))
    print("¯" * (len(str_in) + 2) + '\n')


def centro_caracter(str_escrito, str_guia):
    return str_escrito.upper().center(len(str_guia) + 2, "=")


final_cadena = [centro_caracter(" Bienvenido a apuestas deportivas ", cadena),
                centro_caracter(" La avaricia  ", cadena) + '\n' + '\n',
                "   (0) Empezar apuesta  ", "   (1) Salir del juego    "]


def resultado_usuario_bool(str_ejemplo_largo, iterable_str):
    usuario_input = "error"
    while usuario_input == "error":
        barra_estado(str_ejemplo_largo)

        for i in iterable_str:
            print(i)

        usuario_input = Reto_Sofka_funciones.input_usuario("    ", 0, 1)


resultado_usuario_bool(cadena, final_cadena)

