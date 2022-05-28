"""
Presente el conjunto de instrucciones para crear un arreglo de tamaño 100


"""
n = 5


enteros = [None] * n

for i in range(0, n):
    numero = int(input(f"Ingrese el numero de la posicion{i + 1}: "))
    enteros[i] = numero # podemos poner de una vez el input aca unu

print("Conjunto completo digitado: ")
print(enteros)


#imprimir los elementos en una linea
linea = ""
for i in range(0, n, 2):
    linea += str(enteros[i]) + " - "
print(linea)


print("Valores almacenados en posiciones pares")
for i in range(0, n, 2):
    print (enteros[i])


print("Valores impares en el arreglo")

for i in range(0, n):
    if enteros[i] % 2 == 1:
        print(enteros[i])




n = 10
enteros = [None] * n


# esta es otra forma entendiendo que i representa los indices del conjunto "enteros"