#funciones

"""
Desarrolle un programa que lea los datos de 2 (a, b)
y determine cual de los 2 es mayor y muestre la hipotenusa

"""

"""
Las funciones son como los empledos a los que el jefe(programa principal) usa para realizar algo de lo cual no sabe
la importancia del jefe consisten en poder integrar a todas estas funciones
"""

import math # importamos la libreria math para poder sacar la raiz cuadrada(sqrt) en la funcion hipotenusa

# defino las funciones

        # funcion que calcula la hipotenusa
def calcularHipotenusa(a, b):
    hipotenusa = math.sqrt( (a*a) + (b * b))
    return hipotenusa # las funciones siempre deben retornar un valor

        # funcion para calcular el numero mayor

def calculaMayor(a, b):
    if a > b:
        mayor = a
    else:
        mayor = b
    return mayor

#Programa principal

a = int (input("Digite el valor del cateto a: "))
b = int (input("Digite el valor del cateto b: "))

# llamdo a las funciones

hipotenusa = calcularHipotenusa(a, b)

mayor = calculaMayor(a, b)

# salida
print (f"La hipotenusa es: {hipotenusa} \nEl cateto mayor tiene: {mayor} unidades")
