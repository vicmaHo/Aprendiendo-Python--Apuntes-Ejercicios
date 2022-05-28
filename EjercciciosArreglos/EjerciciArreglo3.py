# Ejercicio arreglo

cantidadProductos = 10
nombresProductos = [None] * cantidadProductos
precioProductos = [None] * cantidadProductos
cuestanMasde3000 = 0
for i in range(len(nombresProductos)):
    nombresProductos[i] = input(f"Ingrese el nombre del producto {i}: ")
    precioProductos[i] = int(input(f"Ingrese el precio de {nombresProductos[i]}: "))
    if precioProductos[i] > 3000:
        cuestanMasde3000 += 1
    
print(f"Son {cuestanMasde3000} los productos que cuestan mas de 3000 pesos")
for i in  range(len(nombresProductos)):
    if precioProductos[i] > 3000:
        print(f"{nombresProductos[i]} cuesta/n: {precioProductos[i]}")