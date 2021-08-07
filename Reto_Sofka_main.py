import Reto_Sofka_funciones as Rs_funciones

datos = Rs_funciones.leer_archivo()
pista = Rs_funciones.pista()
podio = Rs_funciones.podio()

pista.llenar_carriles(datos[0], datos[1], datos[2])

podio.guardar_ganador(pista)
podio.ordenar_resultado()

Rs_funciones.estadisticas(datos)
Rs_funciones.actualizar_archivo(podio)
