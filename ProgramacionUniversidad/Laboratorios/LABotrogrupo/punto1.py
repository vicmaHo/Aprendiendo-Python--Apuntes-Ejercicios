#datos que piden en la hoja esa

#ingreso de datos
nombre_equipo = input("Ingrese el nombre del equipo: ")
partidos_ganados = int(input("Ingrese el numero de partidos ganados: "))
partidos_empatados = int(input("Ingrese el numero de partidos empatados: "))
partidos_perdidos = int(input("Ingrese el numero de partidos perdidos: "))
golesAfavor = int(input("Ingrese el numero de goles a favor: "))
golesEnContra = int(input("Ingrese el numero de goles en contra: "))

#procesamiento de datos
puntos_partidos_ganado = partidos_ganados * 3
puntos_partido_empatado = partidos_empatados * 1

partidos_jugados = partidos_ganados + partidos_empatados + partidos_perdidos

puntos_totales = puntos_partido_empatado + puntos_partidos_ganado

diferenciaGoles = golesAfavor - golesEnContra

diferenciaGoles = abs(diferenciaGoles) # en caso de que quede negativo, abs lo pasara a positivo

# salida de datos
print(f"Nombre: {}")