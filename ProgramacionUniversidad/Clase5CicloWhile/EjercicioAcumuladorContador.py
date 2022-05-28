"""
Para ingresar al curso de producin cinematografica se realizo una prueba clasificatoria. se tiene 
los resultados de dicho examen por aspirante (una nota comprendida entre 0 y 5) y se desea saber
cuantos aspirantes aprobaron el examen, cuantos lo perdieron (nota menor que 3) y cual fue el promedio 
de todo el grupo de aspirantes. No sabesmos cuantos aspirantes son, pero sabemos que cuando se quiera
indicar que se finalizo el ingreso de notas se digitara un valor negativo
"""


# funcion para comprobar que la nota esta en el rango correcto

def leeNota():
    while True:
        nota = float(input(f"Ingrese la calificacion del aspirante {aspiranteNumero}: "))
        if nota <= 5:
            break

        else:
            print("Ingrese una nota entre 0 y 5")
    return nota

aspiranteNumero = 1
aprobados = 0
reprobados = 0
totalNotas = 0

nota = leeNota()

while nota >= 0:
    if nota >= 3.0:
        aprobados += 1
    else: 
        reprobados += 1
# estas dos lineas hacen lo mismo, la comparacion retornan valores falsos o verdaderos (0, 1) 
#   reprobados += nota < 3
#   aprobados += nota >= 3
    totalNotas += nota
    aspiranteNumero += 1
    nota = leeNota()
    
if aprobados + reprobados > 0:
    print(f"Aspirantes que aprueban: {aprobados}")
    print(f"Aspirantes que reprueban: {reprobados}")
    promedio = totalNotas / (aprobados + reprobados)
    print(f"Promedio de aspirantes: {promedio}")
else:
    print("No se ingresaron datos validos")