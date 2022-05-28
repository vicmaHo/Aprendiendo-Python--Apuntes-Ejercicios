# ejercicios - Ejercicio 5
## Entraddas ## total del ordenador y porcentaje de descuento
PcSindescuento = 660
descuento = 10
## Salidas ## si al 100 porciento le quitamos el 10, nos queda el 90: este seria el precio ral del pc

precioTotal = PcSindescuento * (90 / 100)
# estos dos de abajo son una manera alternativa de realizarlo
precioDescuento = PcSindescuento * (10 / 100)
precioTotal2 = PcSindescuento - precioDescuento
## Salidas ##  total a pagar por el ordenador con todos los accesorios
print("El precio total del pc es de:", precioTotal)
print("El precio total del pc es de:", precioTotal2)