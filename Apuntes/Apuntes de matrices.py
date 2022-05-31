# Apuntes de matrices
"""
Las matrices tambien llamadas arreglos bidemensionales, son conjuntos de datos de dos dimensines
se puede interpretar como una lista de listas
Las matrices cuentan con filas y cuentan con columnas
Podemos acceder a las ubicaciones mediante indices ----> matriz[fila][columna]
"""
# declaracion de una matriz usando list comprehension
# matrizA = [[valor_dentro_de_celda for x in range(n)]for y in range(m)]            n = numero de columnas, m = numero de filas
matrizA = [[0 for x in range(3)]for y in range(3)]
print(matrizA)
for i in matrizA:
    print(i)
print("\n" + ("="*30))
# Cómo definir una matriz de enteros, con 4 filas y
# 3 columnas, llamada numeros

numeros = [[None for i in range(3)] for j in range(4)]
for i in numeros:
    print(i)

"""
Como insertar datos?
se debe insertar la posicion --> [fila][columna] donde se almacenara el dato
nombreMatriz[fila][columa] = valor
"""
print("\n" + ("="*30))
nombresMatriz = [
    [None, None],
    [None, None],
    [None, None]
]
for i in nombresMatriz:
    print(i)
print("\n" + ("="*30))

# insertar nuevos nombres
nombresMatriz[0][0] = "Victor"
nombresMatriz[0][1] = "Cesar"
for i in nombresMatriz:
    print(i)
print("\n" + ("="*30))
for i in range(len(nombresMatriz)):   # len matriz para saber la longitud de filas
    for j in range(len(nombresMatriz[0])):  # con len(matriz[0]) podemos saber la longitud de las columas
        nombresMatriz[i][j] = input("Ingrese un nombre: ")
print("\n" + ("="*30))
for i in nombresMatriz:
    print(i)
    
"""
Recuperar datos de arreglos bidimensionales:
nombreMatriz[fila][columna]         añadiendo un print para mostrarlo en pantalla
"""
print(nombresMatriz[0][1])