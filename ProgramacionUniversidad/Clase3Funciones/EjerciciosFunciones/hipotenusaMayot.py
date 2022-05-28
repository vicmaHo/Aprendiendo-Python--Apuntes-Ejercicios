"""
Programa que lea dos catetos, muestre cual es el mayor y muestre la hipotenusa 
"""

import math as mt
"""
funciones
"""
def mayor(a, b):
    if a > b:
        return a
    else:
        return b

def calcularHipotenusa(a, b):
    h = mt.sqrt((a * a) + (b * b))
    return h

"""
principal
"""
# entrada
print("""
Calcular el mayor de dos catetos y la hipotenusa.\n
""")
a = int(input("Ingrese el valor del cateto a: "))
b = int(input("Ingrese el valor del cateto b: "))

# proceso
catetoMayor = mayor(a, b)
hipotenusa = calcularHipotenusa(a, b)
# salida
print(f"El cateto mayor tiene un valor de: {catetoMayor}\nLa hipotenusa tiene un valor de: {hipotenusa}")



