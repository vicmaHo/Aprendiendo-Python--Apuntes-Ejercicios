# Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0. El algoritmo debe imprimir
# el valor ingresado, y un mensaje que indique si el estudiante “Ganó el curso” o “Perdió el curso”. 
# Se gana el curso solo si la nota definitiva es mayor o igual a 3.0.

def mensaje(notaDefinitva):
    if notaDefinitva < 0 or notaDefinitva > 5:
        return f"{notaDefinitva} no se encuentra en el rango correcto"
    if notaDefinitva >= 3.0:
        anotacion = "Gano el curso"
    else:
        anotacion = "Perdio el curso"
    return f"La nota es de: {notaDefinitva}. {anotacion}"

nota = float(input("Ingrese la nota: "))
print(mensaje(nota))