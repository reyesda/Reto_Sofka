import Reto_Sofka_funciones as Rs_funciones

datos = Rs_funciones.leer_archivo()
pista1 = Rs_funciones.pista()
podio1 = Rs_funciones.podio()

pista1.llenar_carriles(datos[0], datos[1], datos[2])

podio1.guardar_ganador(pista1)
podio1.ordenar_resultado()

Rs_funciones.estadisticas(datos)
Rs_funciones.actualizar_archivo(podio1)
