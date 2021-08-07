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

Reto_Sofka_funciones.limpiar_consola()
concursante = Rs_funciones.concursante()
now = datetime.now()
cadena = "$ {:,}                                                      {}:{}"
print(cadena.format(concursante.dinero, now.hour, now.minute))
print("¯" * (len(cadena) + 2) + '\n')

cadena2 = " Bienvenido a apuestas deportivas ".upper()
print(cadena2.center(len(cadena) + 2, "="))
cadena2 = " La avaricia  ".lower()
print(cadena2.center(len(cadena) + 2, "=") + '\n' + '\n')
print("   (1) Empezar apuesta  ")
print("   (2) Salir del juego    ")
Rs_funciones.input_usuario("    ", 1, 2)
