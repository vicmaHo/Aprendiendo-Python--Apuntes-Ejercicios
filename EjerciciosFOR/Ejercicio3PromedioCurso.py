# Suponga que se desea saber la nota promedio del curso de
# algoritmia, diseñe un algoritmo que solicite la cantidad de
# estudiantes del curso y el promedio de cada estudiante.

def promedioCurso(numeroEstudiantes):
    notaTotal = 0
    for i in range(1, numeroEstudiantes+1):
        notaTotal += float(input(f"Ingrese la nota del estudiante {i}: "))
    promedio = notaTotal / numeroEstudiantes
    return promedio

# Entrada
numeroEstudiantes = int(input("Ingrese el numero de estudiantes: "))

# Proceso
promedio = promedioCurso(numeroEstudiantes)

# Salida
print(f"El promedio del curso es de: {promedio}")
