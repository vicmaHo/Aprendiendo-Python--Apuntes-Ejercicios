# ingreso de datos ---- dimensiones del lote base y altura en metros y el precio por metro cuadrado de lote
# hectarea 10.000 m2

base = int(input("Ingrese la base del lote en metros: "))
altura = int(input("ingrese la altura del lote en metros: "))

precio = int(input("Ingrese el precio por metro cuadrado: "))


#procesamiento de datos
area = base * altura

valor = area * precio

hectareas = area / 10000

#salida ---- numero de hectareas del lote y el valor de venta correspondiente

print("El numero de hectareas del lote es de: ", hectareas)

print("El valor de lote es de: ", valor)

