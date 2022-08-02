# Programa con GUI(tkinter) el cual cuenta con ciertas bebidas, con diferente tamaño
# y a diferentes precios
from tkinter import *

# funciones del programa
def calcularVenta():
    bebida = str(Ebebida.get())
    tamanio = str(Etamaño.get())
    cantidad = int(Ecantidad.get())
    
    if bebida == "Tropical" and tamanio == "Junior":
        Eventa.delete(0, END)
        valor = 22000 * cantidad
        aporte = 0.15   * valor
        Eventa.insert(0, valor)
        Eaporte.delete(0, END)
        Eaporte.insert(0, aporte)
    elif bebida == "Tropical" and tamanio == "Supremo":
        Eventa.delete(0, END)
        valor = 35000 * cantidad
        aporte = 0.15 * valor
        Eventa.insert(0, valor)
        Eaporte.delete(0, END)
        Eaporte.insert(0, aporte)
    elif bebida == "Paraiso" and tamanio == "Junior":
        Eventa.delete(0, END)
        valor = 35000 * cantidad
        aporte = 0.15 * valor
        Eventa.insert(0, valor)
        Eaporte.delete(0, END)
        Eaporte.insert(0, aporte)
    elif bebida == "Paraiso" and tamanio == "Supremo":
        Eventa.delete(0, END)
        valor = 50000 * cantidad
        aporte = 0.15 * valor
        Eventa.insert(0, valor)
        Eaporte.delete(0, END)
        Eaporte.insert(0, aporte)


# defino la ventana
ventana = Tk()
ventana.geometry("300x300")
ventana.title("Bebidas!!")
ventana.resizable(False, False) 

# genero los elementos de la interfaz
Lbebida = Label(ventana, text="Bebida")
Ebebida = Entry(ventana, width=10)

Ltamaño = Label(ventana, text="Tamaño")
Etamaño = Entry(ventana, width=10)

Lcantidad = Label(ventana, text="Cantidad")
Ecantidad = Entry(ventana, width=10)

BCalcularValores = Button(text="Calcular valores", command=calcularVenta)

Lventa = Label(ventana, text="Valor Venta")
Eventa = Entry(ventana, width=10)

Laporte = Label(ventana, text="Valor aporte")
Eaporte = Entry(ventana, width=10)


# insertar elementos en la ventana
Lbebida.pack()
Ebebida.pack()

Ltamaño.pack()
Etamaño.pack()

Lcantidad.pack()
Ecantidad.pack()

BCalcularValores.pack()

Lventa.pack()
Eventa.pack()

Laporte.pack()
Eaporte.pack()

ventana.mainloop()