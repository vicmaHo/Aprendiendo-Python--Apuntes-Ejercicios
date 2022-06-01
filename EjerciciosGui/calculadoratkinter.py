from tkinter import *


def suma():
    a = int(EvalorA.get())
    b = int(EvalorB.get())
    suma = a + b
    EResultado.delete(0, END)
    EResultado.insert(0, suma)
    LResultado["text"] = "Resultado de la suma"
    
def resta():
    a = int(EvalorA.get())
    b = int(EvalorB.get())
    resta = a - b
    EResultado.delete(0, END)
    EResultado.insert(0, resta)
    LResultado["text"] = "Resultado de la resta"
    
gui = Tk()
gui.geometry("200x200")
gui.title("suma y resta")
LValorA = Label(gui, text="Valor a")
LValorB = Label(gui, text="Valor b")
LResultado = Label(gui, text="Resultado")
EvalorA = Entry(gui, width=10)
EvalorB = Entry(gui, width=10)
EResultado = Entry(gui, width=10)
BSuma = Button(gui, text="a + b", command=suma)
BResta = Button(gui, text="a - b", command=resta)

# insertar en la ventana
LValorA.pack()
EvalorA.pack()
LValorB.pack()
EvalorB.pack()
BSuma.pack()
BResta.pack()
LResultado.pack()
EResultado.pack()

gui.mainloop()
