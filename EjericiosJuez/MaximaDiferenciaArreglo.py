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


 