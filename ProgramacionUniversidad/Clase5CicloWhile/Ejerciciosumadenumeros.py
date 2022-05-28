"""
Se trata de escribir un programa que lea numeros enteros (de cualquier valor) hata que la  suma de los 
numeros leidos sea
igual os uperior a 50 al final debe mostrar el valor  de suma de los numeros leidos

imprima la cantidad de pares impares 


numeros entre -10 y 10

"""

sumaNumeros = 0
pares = 0
impares = 0
while sumaNumeros < 50:
    numIngresado = int(input("Ingrese un numero:"))
    print("========================")
    sumaNumeros += numIngresado

    if numIngresado % 2 == 0:
        pares += 1
    else: 
        impares += 1

    print(f"El numero ingresado es: {numIngresado}")
    print(f"LLeva una suma de: {sumaNumeros}\n")



print(f"En total la suma de los numeros es: {sumaNumeros}\n")
print(f"La cantidad de numeros impares es de: {impares}")
print(f"La cantidad de numeros pares es de: {pares}")