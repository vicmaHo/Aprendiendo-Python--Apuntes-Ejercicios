# Escriba un programa en Python que dada una lista de
# enteros y un valor x por parte del usuario, diga cuántas
# veces x aparece en la lista. El programa como salida
# debe mostrar la lista ingresada por el usuario e indicar
# cuántas veces aparece el valor x y en cuáles posiciones.

## Entradas
n = int(input("Cantidad de datos de la lista: "))
x = int(input("Cual sera el valor x?: "))

## Proceso
lista = [None] * n
cantidadX = 0
accValores = ""

for i in range(len(lista)):
    lista[i] = int(input(f"Ingrese valores y o ingrese el valor x en la posicion {i}: "))
    if lista[i] == x:
        cantidadX += 1
        accValores += f"{i},"
    
# salida 
print(f"La lista ingresada por el usuario es: {lista}")
print(f"El valor de x es: {x}")
print(f"El valor {x} aparece: {cantidadX} veces")
print(f"El valor {x} aparece en la posiciones:", accValores)