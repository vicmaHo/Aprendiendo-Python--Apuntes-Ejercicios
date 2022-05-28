"""
Un comerciante se dedica a la venta de sillas. Vende tres tipos de sillas:
Tipo    Precio
1       $5.000
2       $7.000
3       $10.000
Por cada cinco sillas compradas se obtiene un descuento, de acuerdo a la tabla
Tipo    Descuento
1       3%
2       5%
3       10%
El resto de sillas se cobran a precio normal. Diseñe un programa que lea el tipo de
silla y la cantidad a comprar e imprima la cantidad, el precio unitario, el descuento
y el precio total, de lo que debe cancelar el cliente por la compra.
"""


#funciones

import math 


def sillasTipo1(cantidad):
    sillasSinDescuento = cantidad % 5
    precioReal = cantidad * 5000
    descuento = ((cantidad - sillasSinDescuento) * 5000) * 0.03
    precioTotal = precioReal - descuento
    print(f"La cantidad de sillas es de: {math.trunc(cantidad)}")
    print(f"EL precio unitario es de: 5000")
    print(f"El precio real es de: {math.trunc(precioReal)}")
    print(f"El descuento es de: {math.trunc(descuento)}")
    print(f"El precio total es de: {math.trunc(precioTotal)}")

def sillasTipo2(cantidad):
    sillasSinDescuento = cantidad % 5
    precioReal = cantidad * 7000
    descuento = ((cantidad - sillasSinDescuento) * 7000) * 0.05
    precioTotal = precioReal - descuento
    print(f"La cantidad de sillas es de: {math.trunc(cantidad)}")
    print(f"EL precio unitario es de: 7000")
    print(f"El precio real es de: {math.trunc(precioReal)}")
    print(f"El descuento es de: {math.trunc(descuento)}")
    print(f"El precio total es de: {math.trunc(precioTotal)}")

def sillasTipo3(cantidad):
    sillasSinDescuento = cantidad % 5
    precioReal = cantidad * 10000
    descuento = ((cantidad - sillasSinDescuento) * 10000) * 0.1
    precioTotal = precioReal - descuento
    print(f"La cantidad de sillas es de: {math.trunc(cantidad)}")
    print(f"EL precio unitario es de: 10000")
    print(f"El precio real es de: {math.trunc(precioReal)}")
    print(f"El descuento es de: {math.trunc(descuento)}")
    print(f"El precio total es de: {math.trunc(precioTotal)}")

#programa

#programa

#programa
#entradas
opcion = int(input("¿Que tipo de silla quiere?: "))


#proceso
if opcion == 1:
    cantidad = int(input("¿Cuantas sillas necesita?: "))
    resultado = sillasTipo1(cantidad)
elif opcion == 2:
    cantidad = int(input("¿Cuantas sillas necesita?: "))
    resultado = sillasTipo2(cantidad)
elif opcion == 3:
    cantidad = int(input("¿Cuantas sillas necesita?: "))
    sillasTipo3(cantidad)
else:
    print("La opcion ingresada no es correcta")
#salida
