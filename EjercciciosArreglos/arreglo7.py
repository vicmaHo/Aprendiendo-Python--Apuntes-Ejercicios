# Desarrolle un programa que recorra un arreglo de enteros,
# evalúe si sus datos son múltiplos de 7 y los muestre en
# pantalla.

## Entrada
lista = [27, 34, 7, 2, 5, 70, 35, 49]


## Proceso
for i in lista:
    if i % 7 == 0:
        ## Salida
        print(f"El {i} es multiplo de 7")