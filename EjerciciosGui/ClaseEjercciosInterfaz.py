'''
Se traata de elaborar un programa que meustre una cuadrivula de botoes de 4x4 enumerados
al iniciar el programa debe marcarse internamente( ein que el usuario lo vea) uno 
de los botones como el objetivo que el usuario debe adivinar; solo contará con tres oportunidades
para lograrlo. Al final, cuando el usuario adivine o se completen los tres intentos debe mostrarse
un mensaje  Has Ganado o Has perdido y toddos los botones deben deshabilitarse
'''

from random import random, randint
from tkinter import *
# saber en que boton damos click, todos los botones acceden a la funcion
def clickButton(m): # m -> numero de boton
    Breiniciar["state"] = NORMAL
    global intentos # para poder acceder a la variable intentos
    intentos += 1
    if intentos <= 3:
        if m == BotonEscondido:
            # desabilito todos los botones
            for i in range(4):
                for j in range(4):
                    tablero[i][j]["state"] = DISABLED
            # imprimo el mensake de ganar
            LMensaje["text"] = "Has ganado"
        else:
            # existen dos soluciones, enviar las coordenadas, o operar m para hallar fila y columna
            f = (m - 1) // 4 # hallo fila
            c = (m - 1) % 4  # hallo columna
            tablero[f][c]["state"] = DISABLED  # modifico la caracteristica estado = desabilitado, NORMAL cuando funciona
            LMensaje["text"] = f"Intenta de nuevo, no es el {m}, te quedan {4-intentos} intentos"
    else:
        for i in range(4):
            for j in range(4):
                tablero[i][j]["state"] = DISABLED
            LMensaje["text"] = "Perdiste :C"    
            
def reiniciar():
    global intentos
    global BotonEscondido
    intentos = 1
    BotonEscondido = randint(1, 16)
    print(BotonEscondido)
    print(intentos)
    for i in range(4):
            for j in range(4):
                tablero[i][j]["state"] = NORMAL
        # imprimo el mensake de ganar
            LMensaje["text"] = "Juego reiniciado"


intentos = 1
# genero el boton aleatorio
# randint(1, 16) # con un randint es mucho mas facil lo de abajo
BotonEscondido = round(random()*15) + 1 # con round obtengo un numero del 0 al 15, + 1, 16, y con round 
print(BotonEscondido)

# genero la ventana
ventana = Tk()
ventana.title("Adivina la casilla")
ventana.geometry("400x300")


Breiniciar = Button(ventana, text="Reiniciar", command=reiniciar, state=DISABLED)
LMensaje = Label(ventana, text="")
tablero = [[Button(ventana, text="")for x in range(4)]for y in range(4)] # crecion de la matriz
                                                                        # de 4 x 4

# añado texto a los botones                              
num = 1
for i in range(4):
    for j in range(4):
        tablero[i][j]["text"] = str(num) # añado el texto a al boton i,j 
        tablero[i][j]["command"] = lambda m = num: clickButton(m) # con un lambda enviamos el numero del boton a la funcion clickButton para saber a que boton le estamos dando click
        #tablero[i][j].grid(row=i, column=j) # con grid en vez de pack, podemos ubicar todo en cuadricula, usando filas y columnas
        
        # pongo los botonees en la interfaz
        tablero[i][j].place(x = 20 + 50 * j , y = 20 + 50 * i) # con place podemos tener mayor control al separar los botones manualmente
        num += 1
        
# agrego menseje a la interfaz
LMensaje.place(x = 10, y = 220)
Breiniciar.place(x = 20, y = 245)
ventana.mainloop()


# reducir las lineas haciendo uso de funciones, principalmente las funciones que traten de 
# deshabilitar o habilitar el tablero dejuego 
# hacer que lfuncion reiniciar inice el juego y no sea necesario 