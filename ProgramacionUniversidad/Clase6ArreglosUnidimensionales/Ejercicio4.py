"""
Desarrolle un programa en python que permita leer el nomre de 10 productos de una
tienda y su correspondiente precio. la palicacion debe deccir cuantos de ellos 
cuestan mas de 3000 pesos y mostrar su nombre, precio y posiion en pantalla.

utilice arreglos para almacenar los precios y nombres de productos

"""


###### leer el nombre de 10 productos - Precio corrspondiente del producto

# leer numero de datos
n = int(input("Ingrese el numero de productos: "))

#leer datos

nombreProducto = [None] * n
precioProducto = [None] * n

for i in range(0, n):
    nombreProducto[i] = input(f"Nombre del producto {i + 1}: ")
    precioProducto[i] = int(input(f"Ingrese el precio de {nombreProducto[i]}: "))

print("Listado de productos mayores a 3000: ")
mayor3000 = 0
for i in range(0, n):
    if precioProducto[i] > 3000:
        mayor3000 += 1
        print(f"{i + 1}. {nombreProducto[i]} -- {precioProducto[i]}")    

print(f"La cantidad de productos con un precio mayor a 3000: {mayor3000}")


###### mostrar cuantos cuestan mas de 300 pesos y mostrar los precios y nombres de l productos



