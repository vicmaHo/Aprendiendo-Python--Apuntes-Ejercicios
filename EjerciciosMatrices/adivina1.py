'''
Se trata de un programa que genera un número aleatorio entero entre 1 y 100, lo oculte y le de 
al usuario 5 oportunidades para que adivine el número oculto.

Ahora usted debe hacer una matriz cuadrada de 10x10, seleccionar aleatoriamente una casilla sin
que el usuario sepa cual es, y el usuario debe adivinarlo en un máximo de 5 intentos. Para la 
ayuda, imagine que se trata del plano cartesiano y usted le indicará al usuario la distancia de
la casilla indicada por el usuario a la casilla seleccionada.
'''
from random import randint
oculto = randint(1, 100)
hayGanador = False
oportunidades = 0
while (not hayGanador) and (oportunidades < 5):
    valor = int(input("Digite un valor: "))
    oportunidades += 1
    if(valor==oculto):
        print("Usted ha ganado!!!")
        hayGanador = True
    else:
        print(f"Aún no lo logras, sigue intentando, te quedan {5-oportunidades} oportunidades")
        if(oculto<valor):
            print("El número oculto es menor")
        else:
            print("El número oculto es mayor")
if not hayGanador:
    print(f"Eres un perdedor!!! El número era: {oculto}")
    