"""
El curso de algoritmia se califica con dos parciales (el primero tiene un peso de 30% y el segundo 35%) 
una nota de laboratorios (25%) y una nota del trabajo final del curso (10%)

para n estudiantes

"""




def notaDefinitiva(p1, p2, lab, trabajoFinal):
    final = (p1 *  0.3) + (p2 * 0.35) + (lab * 0.25) + (trabajoFinal * 0.1)
    return final 


# condiciones iniciales para el numero de estudiantes a procesar

n = int(input("Digite el numero de estudiantes"))
numEstudiantes = 0


# for i in range(numEstudiantes, n):
#
#

while numEstudiantes < n:  # condicion que se debe cumplir para entrar en el ciclo while
    
    nombre = input("Nombre del estudiante: ")

    parcial1 = float(input("Ingrese la nota del parcial 1: "))

    parcial2 = float(input("Ingrese la nota del parcial 2: "))

    laboratorio = float(input("Ingrese la nota del laboratorio: "))

    trabajoFinal = float(input("Ingrese la nota del trabajo final: "))


    notafinal = notaDefinitiva(parcial1, parcial2, laboratorio, trabajoFinal)


    print(f"El estudiante {nombre} tiene una nota de: {notafinal}")
    

    numEstudiantes += 1  # aumento del contador de numero de estudiantes para que el ciclo progrese en cada iteracion

