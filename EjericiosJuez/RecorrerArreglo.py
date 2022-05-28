#Función de multiplos, recibe un arreglo y retorna True si encuentra algún numero en la lista cuyo vecino derecho sea múltiplo de el.
import numpy as np
def multiplos(arreglo):
    for j in range(0, len(arreglo)):
        if j != len(arreglo)-1:
            if arreglo[j] % arreglo[j+1] == 0:
                return True
    return False
#Codigo para pruebas (incluir unicamente al enviar su solución)

n = int(input())
entrada = input().split(" ")
entrada = list(map(lambda x: int(x),entrada))
arreglo = np.array(entrada)
print(multiplos(arreglo))