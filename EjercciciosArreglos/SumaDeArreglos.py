# suma de dos arrays usando numpy

import numpy as np

numeros1 = np.array([1,2,3,4,5])
numeros2 = np.array([2,3,4,5,6])
tamanio = numeros1.size
numeros3 = np.array([None]*tamanio)

for j in range(tamanio):
    suma = 0
    suma = numeros1[j] + numeros2[j]
    numeros3[j] = suma
print(numeros3)


# version abreviada usando una funcion lambda
resultado = np.array(list(map(lambda x, y: x + y, numeros1, numeros2)))
print(resultado)