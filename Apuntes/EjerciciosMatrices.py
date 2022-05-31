# Ejercicios de matrices
# •Presente el conjunto de instrucciones en Python
# para crear una matriz de 50x4 números reales.
# •Adicione las instrucciones necesarias para solicitar al
# usuario cada uno de los números
# •Ahora, muestre en un mensaje, todos los números

matriz = [[ None for i in range(4)]for j in range(4)]
print(matriz)
for i in matriz:
    print (i)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = int(input("Ingrese el numero: "))

for i in matriz:
    print(i)