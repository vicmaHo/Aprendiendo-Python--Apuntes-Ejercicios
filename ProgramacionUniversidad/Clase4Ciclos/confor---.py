
def notaDefinitiva(p1, p2, lab, trabajoFinal):
    final = (p1 *  0.3) + (p2 * 0.35) + (lab * 0.25) + (trabajoFinal * 0.1)
    return final 


# condiciones iniciales para el numero de estudiantes a procesar

n = int(input("Digite el numero de estudiantes"))
numEstudiantes = 0

for i in range(numEstudiantes, n):
    nombre = input("Nombre del estudiante: ")

    parcial1 = float(input("Ingrese la nota del parcial 1: "))

    parcial2 = float(input("Ingrese la nota del parcial 2: "))

    laboratorio = float(input("Ingrese la nota del laboratorio: "))

    trabajoFinal = float(input("Ingrese la nota del trabajo final: "))


    notafinal = notaDefinitiva(parcial1, parcial2, laboratorio, trabajoFinal)


    print(f"El estudiante {nombre} tiene una nota de: {notafinal}")