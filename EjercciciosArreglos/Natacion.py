"""
En una competencia de natación se desea implementar una
aplicación para almacenar el tiempo por cada competidor y
además determinar con base en todos los tiempos de los
competidores cual es el ganador. El usuario debe especificar
cuantos tiempos (competidores) desea ingresar.
"""

n = int(input("Cuantos tiempos desea ingresar: "))
tiempos = []

for i in range(n):
    tiempos.append(int(input("Ingrese el tiempo del competidor numero %d: " % (i+1))))
ganadorTiempo = min(tiempos)
ganadorCompetidor = tiempos.index(ganadorTiempo)
print("Estos son los tiempos: ")
for i in tiempos:
    print(f"{i}", end=", ")
    
print(f"\nEl ganador es el competidor {ganadorCompetidor+1} con un tiempo de: {ganadorTiempo}")