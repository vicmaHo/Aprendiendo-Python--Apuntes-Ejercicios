# Vamos a practicar cómo recorrer los elementos de un arreglo de una dimensióna. Queremos hacer una 
# función para darnos cuenta si en un arreglo de números enteros alguno de los números tiene un vecino 
# derecho que sea múltiplo de él.
# En el ejemplo de la gráfica el número 7 tiene un vecino a la derecha que es el número 3.
# 3 no es múltiplo de 7, por lo que hasta ahora no has encontrado la condición.
# El siguiente número de la lista es el número 3, y su vecino derecho es el número 8.
# 8 no es múltiplo de 3, por lo que hasta ahora no has encontrado la condición.
# Finalmente el siguiente número de la lista es el número 8, y su vecino derecho es el número 4. 
# 4 en este caso si es múltiplo de 8, por lo que el programa termina y retorna verdadero, es decir si 
# existe un número cuyo vecino derecho es múltiplo de él

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