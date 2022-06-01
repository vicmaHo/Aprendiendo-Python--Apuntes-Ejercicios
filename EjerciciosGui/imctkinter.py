# import tabnanny


# Al ingresar a un centro medico se solicitan los siguientes datos para un paciente:
# nombre, peso (kg) y altura (mts), se debe calcular el indice de masa corporal
# (OMC= peso / altura²) e identificaar la categoria que tiene el paciente segun el valor calulado
# Hay tres categorias que se puden identificar segun el IMC utilizando la aiguiten tabla

# IMC < 18.5          Infrapeso
# 18.5 < IMC < 25.0   Normal
# IMC > 25.0          Sobrepeso

# Desarrollar un programa que mediante una ventan, le pregunte al usuario sus datos y le informe mediante
# una entrada su IMC, y mediante una eqiueta su categoria


from tkinter import *


def calculoImc():
    peso = float(EPeso.get())
    estatura = float(EEstatura.get())
    IMC  = round(peso / (estatura ** 2), 2)
    
    if IMC <18.5:
        Eimc.delete(0, END)
        Eimc.insert(0, IMC)
        LimcUser["text"] = "Se encuentra en Infrapeso"
    elif IMC >= 18.5 and IMC < 25.0:
        Eimc.delete(0, END)
        Eimc.insert(0, IMC)
        LimcUser["text"] = "Se encuentra en Normal"
    else:
        Eimc.delete(0, END)
        Eimc.insert(0, IMC)
        LimcUser["text"] = "Se encuentra en Sobrepeso"

gui = Tk()
gui.geometry("300x200")
gui.title("Calculando su IMC")

LPeso = Label(gui, text="Ingrese su peso (kg)")
LEstatura = Label(gui, text="Ingrese su estatura (mts)")
LimcUser = Label(gui, text="Se encuentra en... ")
LimcInfor = Label(gui, text="Su IMC es: ")
EPeso = Entry(gui, width=6)
EEstatura = Entry(gui, width=6)
Bcalculo = Button(gui, text="Calcular IMC", command=calculoImc)
Eimc = Entry(gui, width=7)


# insertando elementos en la ventana

LPeso.pack()
EPeso.pack()
LEstatura.pack()
EEstatura.pack()
LimcInfor.pack()
Bcalculo.pack()
Eimc.pack()
LimcUser.pack()

gui.mainloop()


