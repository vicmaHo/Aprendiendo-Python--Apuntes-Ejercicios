# APUNTES NUMPY
# importat numpy, nos brinda facilidades
import numpy as np

# arreglos --
a = np.array([10, 20, 30]) # coge una lista y la convierte en un array
print([10,20,30]) # lista normal
print(a)
print(type(a)) # ahora es tipo np array

# consultar tamañ
print(a.shape) # solo tiene una dimension y tiene 3 elementos

# extraer informacion del array
print(a[0], a[1], a[2], sep="\n")

# modificar posiciones del array
a[0] = 5   # indico la posicion del array y le asigno el valor 5

# MATRICES
# arreglos de dos dimensiones
b = np.array([[10, 20, 30], [40, 50, 60]])
print(b)
#podemos observala como filas y columnas

# Extraer informacion de la matriz
print(b[0], b[1], sep="\n")
# imprime toda la fila
print(b[0][0], b[1][1], sep="\n")
# imprimimos las casillas indicads

# modificar posiciones de la matriz
b[0][0] = 9
b[1][1] = 7

# Creacion de matrices -- numpy permite crear matrices facilmente
matriz = np.zeros((4, 3)) # dentro indicamos las piosiciones, crea una matriz de zeros
# con ones creamos solo 1
# con full ((2, 1), 5) indicamos que todos sean 5s

# Matriz identidaa


# acceder a la matricesd 
## INdexacion entera
a = np.array([[1,2,3], [5,6,7], [9,10,11]])
print(a)
print()
print(np.fliplr(a)) # con esto cambiamos los datos de la matriz de izquierda a derecha

# usar rebanadas para sacar el esubconjunto que conssite en 2 primeras filas y las columnas

b = a[:2, 1:3] # rebano la matriz para sacar una mas pequeñña
print(b)
b[0, 0] = 77

## Indexaciones..... porcompletar 


