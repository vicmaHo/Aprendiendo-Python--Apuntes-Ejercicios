# se trata de un program que genera un numero aleatorio enero entre 1 y 100, lo oculte y le da al usuario 5 oportunidades para 
# que adivine el numero oculto.

# Ahora usted debe hacer una matriz cuadrada de 10X10, seleccionar aleatoriamente una casilla sin que el
# usuario sepa cual es, y el usuario debe adivinarlo en maximo de 5 intentos. Para la ayuda imagine
# que se trata del plano cartesiano y usted le indicará al  usuario la distanci de la casilla indicada por 
# el usuario

from math import sqrt


import random
oculto = random.randint(1, 100)
hayGanador = False
oportunidades = 0

while not hayGanador and oportunidades < 5:
    numero = int(input("Ingrese el numero que va a adivinar: "))
    oportunidades += 1
    if numero == oculto:
        print("Usted ha ganado!!")
        hayGanador = True
    else: 
        print(f"Aun no lo logras, siguen intentanto. Te quedan {5-oportunidades} intentos")
        if oculto < numero:
            print("el numero oculto es menor")
        else:
            print("El numero oculto es mayor")
    
if not hayGanador:
    print("Eres un perdedor!!")
    print(oculto)
    
    
columnaAleatorio = random.randint(0,100)
filaAleatoria = random.randint(0,100)
matriz = [[for ]]