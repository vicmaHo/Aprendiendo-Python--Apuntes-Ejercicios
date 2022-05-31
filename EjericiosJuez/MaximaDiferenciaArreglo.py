# Dado un arreglo [2,4,6,-1,4,6] deseamos encontrar la mayor diferencia entre dos elementos del mismo, 
# en este caso la diferencia se define como el valor absoluto de la resta de un número, por lo que siempre 
# es positiva.

# Para buscar la mayor diferencia, evaluamos el arreglo de esta manera.

# El primer elemento 2 y el segundo es 4, por lo que la diferencia es 2, almacenamos este resultado.
# El primer elemento 2 y el tercero es 6, por lo que la diferencia es 4, como la diferencia es mayor a la que llevamos, almacenamos este resultado
# El primer elemento 2 y el cuarto elemento es -1, por lo que la diferencia es 3, como no es mayor, no la almacenamos
# El primer elemento 2 y el quinto elemento es 4, por lo que la diferencia es 2, como no es mayor, no la almacenamos
# El primer elemento 2 y el sexto elemento es 6, por lo que la diferencia es 4, como no es mayor, no la almacenamos.
# El segundo elemento es 4 y el tercer elemento es 6, por lo que la diferencia es 2, como no es mayor, no la almacenamos.
# Repetimos este proceso hasta comparar todos los elementos, obtenemos al final que la diferencia máxima es 7 (entre -1 y 6).

import numpy as np
def maxima_diferencia(arreglo):
    maxDiff = 0
    for elemento in arreglo:
        for elementos2 in arreglo:
            diff = abs(elemento - elementos2)
            if diff > maxDiff:
                maxDiff = diff
    return maxDiff
    
# [2,4,6,-1,4,6]

    
    # maxDiff = 0
    # for elemento in arreglo:
    #     for indice in range(len(arreglo)):
    #         diff = 0
    #         diff = abs(elemento - arreglo[indice])
    #         if diff >= maxDiff:
    #             maxDiff = diff
    # return maxDiff

n = int(input())
entrada = input().split(" ")
entrada = list(map(lambda x: int(x),entrada))
arreglo = np.array(entrada)
print(maxima_diferencia(arreglo))


 