"""
grupo de instrucciones que permiten la ejecucion repetitiva de otro grupo de instrucciones
"""

"""
desarrollar un programa que solicite un numero y muestre los numeros del 1 hasta el numero solicitado 


entrada: n

salidas: imprimir numero 1, numuero 2....

proceso para n imprimir n veces

expresion de incio, expresion de condicion, expresion de aumento --- tange
"""

n = int(input("Numero: "))

for i in range (0, n, 2):
    print (i)

for i in range (100, 0, -2):
    print (i)

i = 0

for i in range (0, 10):
    print (i)
print(f"el valor final de i: {i}")


