# En una competencia de natación se desea implementar una
# aplicación para almacenar el tiempo por cada competidor y
# además determinar con base en todos los tiempos de los
# competidores cual es el ganador. El usuario debe especificar
# cuantos tiempos (competidores) desea ingresar.

## Entrada
numeroCompetidores = int(input("Ingrese el numero de competidores: "))
listaTiempos = [None] * numeroCompetidores

for i in range(len(listaTiempos)):
    listaTiempos[i] = int(input(f"Ingrese el tiempo del competidor #{i + 1}: "))


## Proceso
minimo = min(listaTiempos)
for i in range(len(listaTiempos)):
    if listaTiempos[i] == minimo:
        competidor = i + 1


## Salida
print(f"El competidor ganador fue {competidor} que obtuvo un tiempo de {minimo} segundos.")