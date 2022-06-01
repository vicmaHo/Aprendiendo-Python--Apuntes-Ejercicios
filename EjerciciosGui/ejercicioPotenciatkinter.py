from statistics import geometric_mean
import tkinter
# from tkinter import * ---> importamos todo lo de tkinter

def cacular():
    a = int(EvalorA.get())
    potencia = a * a
    EResultado.delete(0, tkinter.END)
    EResultado.insert(0, potencia)

# crear la ventana
gui = tkinter.Tk()
gui.geometry("140x130")

# crear elementos de la ventana
LvalorA = tkinter.Label(gui, text="Valor a")
LResultado = tkinter.Label(gui, text="resuktado")
EvalorA = tkinter.Entry(gui, width=10)
EResultado = tkinter.Entry(gui, width=10)
Bpotencia = tkinter.Button(gui, text="calcular a2", command=cacular) # command: vinculamos la funcion para que el boton realice la operacion

# introducir los elementos en la ventana
LvalorA.pack()
EvalorA.pack()
Bpotencia.pack()
LResultado.pack()
EResultado.pack()

# ejecucion de la ventana
gui.mainloop()