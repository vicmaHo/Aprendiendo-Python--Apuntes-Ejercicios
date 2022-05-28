

def calculoVenta(cantidad, precio):
    if cantidad < 5:
        descuento = 0.1
    elif cantidad >= 5 and cantidad < 10:
        descuento = 0.2
    else:
        descuento = 0.4
    
    precioTotal = cantidad * precio
    descuentoObtenido = precioTotal * descuento
    valorTotal = precioTotal - descuentoObtenido

    print(f"Precio de las computadoras:    {precioTotal} pesos\nDescuento obtenido........:    {descuentoObtenido} pesos\nValor total a pagar es....:    {valorTotal} pesos")



#programa principal

#son 3 facturas de venta por lo tanto, son 3 veces las entradas y 3 veces las salidas

print("""Venta No. 1
##################################################""")
nombre = input("Nombre del cliente: ")
cantidad = int(input("Cantidad de computadoras a comprar: "))
precio = float(input("Precio unitario por computadora: "))
print("##################################################")
calculoVenta(cantidad, precio)
print("##################################################\n")

print("""Venta No. 2
##################################################""")
nombre = input("Nombre del cliente: ")
cantidad = int(input("Cantidad de computadoras a comprar: "))
precio = float(input("Precio unitario por computadora: "))
print("##################################################")
calculoVenta(cantidad, precio)
print("##################################################\n")

print("""Venta No. 3
##################################################""")
nombre = input("Nombre del cliente: ")
cantidad = int(input("Cantidad de computadoras a comprar: "))
precio = float(input("Precio unitario por computadora: "))
print("##################################################")
calculoVenta(cantidad, precio)
print("##################################################")