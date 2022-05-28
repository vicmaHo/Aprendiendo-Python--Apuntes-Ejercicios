# La organización de la Feria ha lanzado la preventa para las manillas de acceso al
# coliseo con los siguientes precios: para horario diurno a $12000 y para horario nocturno a $17000.
# Considerando los siguientes descuentos por compras de 10 manillas o más así: si las manillas son solo
# diurnas el descuento es del 8%, si las manillas son combinadas el descuento es del 11% y si son solo
# nocturnas el descuento es del 15%. Usted debe desarrollar un programa de computador que permita leer,
# para un cliente, la cantidad de manillas diurnas y nocturnas que va a comprar y al final mostrar el valor de
# las manillas de cada tipo (sin descuento), el valor del descuento (si lo consiguió) y el valor a pagar.



## Funciones ##
def calculaDescuento(manillasDiurnas, manillasNocturnas):
    if manillasDiurnas >= 10 and manillasNocturnas == 0:
        descuento = 0.08
    elif manillasDiurnas >= 10 and manillasNocturnas >= 1:
        descuento = 0.11
    elif manillasDiurnas >= 1 and manillasNocturnas >= 10:
        descuento = 0.11
    elif manillasDiurnas == 0 and manillasNocturnas >= 10:
        descuento = 0.15
    else:
        descuento = 0
    return descuento

## Entradas ##
manillasDiurnas = int(input("Ingrese la cantidad de manillas diurnas que comprara: "))
manillasNocturnas = int(input("Ingrese la cantidad de manillas nocturnas que comprara: "))

## Proceso ##
valorDiurnas = manillasDiurnas * 12000
valorNocturnas = manillasNocturnas * 17000
totalNeto = (manillasDiurnas * 12000) + (manillasNocturnas * 17000)
porcentajeDescuento = calculaDescuento(manillasDiurnas, manillasNocturnas)
descuento = totalNeto * porcentajeDescuento
totalConDescuento = totalNeto - descuento

## Salida ##
print(f"El valor de {manillasDiurnas} manillas diurnas es de: {valorDiurnas}")
print(f"El valor de {manillasNocturnas} manillas nocturnas es de: {valorNocturnas}")
print(f"El porcentaje de descuento es {porcentajeDescuento * 100}%. Y un total de descuento del: {descuento}")
print(f"El valor total a pagar es de: {totalConDescuento}")
