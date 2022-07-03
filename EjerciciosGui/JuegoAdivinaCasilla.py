'''
Se traata de elaborar un programa que meustre una cuadrivula de botoes de 4x4 enumerados
al iniciar el programa debe marcarse internamente( ein que el usuario lo vea) uno 
de los botones como el objetivo que el usuario debe adivinar; solo contará con tres oportunidades
para lograrlo. Al final, cuando el usuario adivine o se completen los tres intentos debe mostrarse
un mensaje  Has Ganado o Has perdido y toddos los botones deben deshabilitarse
'''

from random import random, randint
from tkinter import *
from tkinter import ttk

# funcion para deshabilitar o habilitar el tablero, se usa cuando se reinicia, se gana o se pierde
def deshabilitarHabilitarTablero(mensaje, estado = DISABLED):
    for i in range(4):
        for j in range(4):
            tablero[i][j]["state"] = estado
    LMensaje["text"] = mensaje
    
# saber en que boton damos click, todos los botones acceden a la funcion
def clickButton(m): # m -> numero de boton
    Breiniciar["state"] = NORMAL
    global intentos # para poder acceder a la variable intentos
    intentos += 1
    if intentos <= 3:
        if m == BotonEscondido:
            # desabilito todos los botones
            deshabilitarHabilitarTablero("HAS GANADO!!!! era el %d"% BotonEscondido) 
        else: # deshabilito el boton en cuestion. Ya que no es el indicado
            # existen dos soluciones, enviar las coordenadas, o operar m para hallar fila y columna
            f = (m - 1) // 4 # hallo fila
            c = (m - 1) % 4  # hallo columna
            tablero[f][c]["state"] = DISABLED  # modifico la caracteristica estado = desabilitado, NORMAL cuando funciona
            LMensaje["text"] = f"Intenta de nuevo, no es el {m}, te quedan {4-intentos} intentos"
    else:
        deshabilitarHabilitarTablero("Perdiste..... :c, era el %d" % BotonEscondido) 
            
def reiniciar():
    global intentos
    global BotonEscondido
    intentos = 1
    BotonEscondido = randint(1, 16)
    #print(BotonEscondido)
    deshabilitarHabilitarTablero("HA JUGAR!!!", NORMAL)
    Breiniciar["state"] = DISABLED

# genero la ventana
ventana = Tk()
ventana.title("Adivina la casilla!!!")
ventana.resizable(False, False) # posibilidad de cambiar el tamaño de la ventana
# centro la ventana
# Tamaño de la ventana
window_width = 500
window_height = 300

# Tamaño de pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# encuentro el punto del centro
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# Cambio de tamaño y posición
ventana.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# genero los elementos de la interfaz
Breiniciar = ttk.Button(ventana, text="Reiniciar", command=reiniciar, state=DISABLED)
LMensaje = ttk.Label(ventana, text="")
tablero = [[ttk.Button(ventana, text="")for x in range(4)]for y in range(4)] # crecion de la matriz
                                                                        # de 4 x 4 con botones

# añado texto a los botones                              
num = 1
for i in range(4):
    for j in range(4):
        tablero[i][j]["text"] = str(num) # añado el texto a al boton i,j 
        tablero[i][j]["command"] = lambda m = num: clickButton(m) # con un lambda enviamos el numero del boton a la funcion clickButton para saber a que boton le estamos dando click
        #tablero[i][j].grid(row=i, column=j) # con grid en vez de pack, podemos ubicar todo en cuadricula, usando filas y columnas
        
        # pongo los botonees en la interfaz
        tablero[i][j].place(x = 60 + 100 * j , y = 25 + 55 * i) # con place podemos tener mayor control al separar los botones manualmente
        num += 1
    
reiniciar() # con reiniciar puedo iniciarlizar las variables necesarias, solo es necesario posicionarlo en este lugar
# agrego menseje a la interfaz
LMensaje.place(x = 100, y = 235)
Breiniciar.place(x = 215, y = 255)
ventana.mainloop()
