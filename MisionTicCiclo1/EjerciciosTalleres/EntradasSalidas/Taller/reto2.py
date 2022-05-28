## Entradas ## precio neto del movil, porcentaje de incremento
precioNeto = 420
porcentaIncremento = 20 / 100

## Proceso ##  multiplicando el preicio neto del producto con el porcentaje obtenemos el valor del porcentaje que sumamos para obtener el valro total
valorDelIncremento = 420 * porcentaIncremento
valorTotal = precioNeto + valorDelIncremento
valorTotal2 = precioNeto * (120 / 100) # otra forma de calcular el precio aumentado (sumando el 20 porciento al 100 porciento y multiplicandolo por el 120%)

## Salida ## cuanto cuesta el movil si se espera hasta el otro dia (con el porcentaje agregado)
print("El precio total del producto aplicando un incremento del 20% es de:", valorTotal)
print("El precio total del producto aplicando un incremento del 20% es de:", valorTotal2)