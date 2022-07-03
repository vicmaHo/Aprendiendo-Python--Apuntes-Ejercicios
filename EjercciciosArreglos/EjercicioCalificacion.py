# entradas: calificacion de un numero indefinido de estudiantes (se ingresa 0 para determinar que se termino la calificacaion)

# salidas: Estudiantes encuestados
# frecuencia de calificaciones con. calificacion - num.estudiantes - histograma

frecuencia = [0 for i in range(10)]
numEstudiantes = 0
while True:
    calificacion = int(input("Ingrese la calificacion que otorga: "))
    if calificacion == 0:
        break
    calificacion -= 1
    frecuencia[calificacion] += 1
    numEstudiantes += 1

print("Estudiantes encuestados: %d" % numEstudiantes)
print("Frecuencia de las calificaciones: ")

print("Calificaciones\tnum.Estudiantes\t\tHistograma")
for i, n in enumerate(frecuencia):
    print(f"{i+1}\t\t{n}\t\t\t"+"*"*frecuencia[i])