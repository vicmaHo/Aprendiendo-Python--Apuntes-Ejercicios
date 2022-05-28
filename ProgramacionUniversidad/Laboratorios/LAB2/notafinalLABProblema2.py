#funcion para la nota final
def notaFinal(nombreMateria):
    print(f"Ingreso de notas para: {nombreMateria}")
    notaExamen = float(input("Ingrese la nota del parcial: "))
    nota1 = float(input("Ingrese la nota de la tarea 1: "))
    nota2 = float(input("Ingrese la nota de la tarea 2: "))
    nota3 = float(input("Ingrese la nota de la tarea 3: "))

    if nombreMateria == "matematica":
        notaDefinitiva = (notaExamen * 0.9) + (((nota1 + nota2 + nota3) / 3) * 0.1)
    elif nombreMateria == "fisica":
        notaDefinitiva = (notaExamen * 0.8) + (((nota1 + nota2 + nota3) / 3) * 0.2)
    else:
        notaDefinitiva = (notaExamen * 0.85) + (((nota1 + nota2 + nota3) / 3) * 0.15)
    
    print(f"La nota definitiva en {nombreMateria} es de: {notaDefinitiva}")
    if notaDefinitiva >= 3.0:
        print("Gano la materia")
    else:
        print("Perdio la materia")
    print("==================================================\n")

#programaPrincipal

#entradas - se realizan 3 veces

nombreMateria = input("Ingrese el nombre de la materia (matematica - fisica - quimica): ")
print("==================================================")
#proceso

notaFinal(nombreMateria)

nombreMateria = input("Ingrese el nombre de la materia: ")
print("==================================================")
#proceso

notaFinal(nombreMateria)

nombreMateria = input("Ingrese el nombre de la materia: ")
print("==================================================")
#proceso

notaFinal(nombreMateria)