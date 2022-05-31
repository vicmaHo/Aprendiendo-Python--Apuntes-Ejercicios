# Suma de los elementos de la diagonal
# basicamente en la diagonal principal se encuentran
def sumaDiagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                suma += matriz[i][j]
    return suma
matriz = [
    [3,2,4],
    [2,1,1],
    [6,7,2]
]
print(sumaDiagonal(matriz))


# suma de los elementos de cada columna
matriz = [
    [2,5,2],
    [3,5,12],
    [6,12,43],
    [21,32,31]
]

def sumaColumnas(matriz):
    columnaSumada = 0
    for 