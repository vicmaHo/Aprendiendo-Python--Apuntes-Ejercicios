"""
Se realizo el apartado del juego con la matriz :D
Autores:
    Victor Manuel Hernandez Ortiz - 2259520
    Juan Pablo Escobar Viveros - 2259519
"""


'''
Se trata de un programa que genera un número aleatorio entero entre 1 y 100, lo oculte y le de 
al usuario 5 oportunidades para que adivine el número oculto.

Ahora usted debe hacer una matriz cuadrada de 10x10, seleccionar aleatoriamente una casilla sin
que el usuario sepa cual es, y el usuario debe adivinarlo en un máximo de 5 intentos. Para la 
ayuda, imagine que se trata del plano cartesiano y usted le indicará al usuario la distancia de
la casilla indicada por el usuario a la casilla seleccionada.
'''

from random import randint
from math import sqrt
# oculto = randint(1, 100)
# hayGanador = False
# oportunidades = 0
# while (not hayGanador) and (oportunidades < 5):
#     valor = int(input("Digite un valor: "))
#     oportunidades += 1
#     if(valor==oculto):
#         print("Usted ha ganado!!!")
#         hayGanador = True
#     else:
#         print(f"Aún no lo logras, sigue intentando, te quedan {5-oportunidades} oportunidades")
#         if(oculto<valor):
#             print("El número oculto es menor")
#         else:
#             print("El número oculto es mayor")
# if not hayGanador:
#     print(f"Eres un perdedor!!! El número era: {oculto}")
print("="*40)

# desarrollo de la actividad
# creacion del cuadrado 10x10
cuadrado = [[None for i in range(10)] for j in range(10)]
# for i in cuadrado:
#     print(i)
    
# seleccion de una casilla aleatoria

fila = randint(0, 9)
columna = randint(0, 9)
#print(f" *** esto no lo ve el usuario, es solo para las pruebas *** La casilla es {fila}, {columna}")
cuadrado[fila][columna] = "Aqui es!!!!"    
# loop para iniciar el juego
print("Bienvenido/a al juego!!!\nTu objetivo es encontrar la casilla que ha sido ELEGIDAAA!\nBuena Suerte!!!!!")
print("Ingrese las coordenadas como numeros enteros separado por un espacio (recuerde que las coordenadas van desde 0 hasta 9)")    
jugando = True
intentos = 5
while jugando:
    print("="*40)
    distancia = 0
    coordenadas = input("Ingrese aqui las coordenadas ---> ").split(" ")
    coordenadas = [int(x) for x in coordenadas] # convierto los valores en enteros
    if coordenadas[0] == fila and coordenadas[1] == columna:
        break
    else:
        intentos -= 1
        print(f"Sigue intentando :(\nTe quedan {intentos} intentos")
        distancia = round(sqrt(((coordenadas[0]-fila)**2) + ((coordenadas[1]-columna)**2)),2) 
        print(f"La distancia a la que estas del punto es: {distancia}")
    if intentos == 0:
        break
print("="*40)
if intentos == 0:
    print("Has perdido!!!")
    print(f"El punto era: ({fila}, {columna})")
else:
    print("Has Adivinado!!!!")