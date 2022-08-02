#Reto 4 - uso de lambdas, map y reduce

def ordenes(rutinaContable: list):
    from functools import reduce as re
    # proceso
    totalOrden = list(map(lambda x: [x[0]] + list(map(lambda z: z[1] * z[2], x[1:])), rutinaContable)) # sacamos el numero de orden y el total de cada producto
    totalOrden = list(map(lambda x: [x[0]] + [re(lambda a, b: a+b, x[1:])],totalOrden)) # reducimos la lista sumando sus elementos
    for i in totalOrden: # verficamos la condicion para añadir el incremento
        if i[1] < 600000:
            i[1] += 25000
    # salida
    print("------------------------ Inicio Registro diario ---------------------------------")
    for i in totalOrden:
        print("La factura {} tiene un total en pesos de {:,.2f}".format(i[0],i[1]))
    print("-------------------------- Fin Registro diario ----------------------------------")




# Sumar el total de cada tupla de cada lista -- multiplicar cantidad por precio unitario
# Sumar los totales de todas las tuplas de toda la lista
# Suma el incremento si la compra no llega a un mínima de 600.000 pesos, en este caso, se
# incrementa 25.000 pesos al total de la compra.


# rutinaContable = [
# [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
# [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
# [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
# [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
# ]
# rutinaContable = [ [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
#                    [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)],
# ]

	
rutinaContable = [ [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
                   [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
                   [6591, ("7812", 2, 11.99), ("9652",11,18.99)],
]
ordenes(rutinaContable)
