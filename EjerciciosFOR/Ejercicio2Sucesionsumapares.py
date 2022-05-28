# Diseñe un algoritmo que permita obtener la suma de todos los
# números enteros existentes en una serie de 1 a n y la cantidad de
# números pares encontrados, siendo n un número digitado por un
# usuario. Use un ciclo for en su diseño.

def esPar(n):
    cantidadPar = 0
    if n % 2 == 0:
        cantidadPar += 1
    return cantidadPar

def sumaSerie(n):
    sumaTotal = 0
    conteoPares = 0
    for i in range(1, n+1):
        conteoPares += esPar(i)
        sumaTotal += i
    print(f"La suma de los numeros desde 1 hasta {n} es: {sumaTotal}")
    print(f"La cantidad de pares entre 1 y {n} es de: {conteoPares}")
    
# Entrada
numero = int(input("Ingrese un numero para sacar su suma de 1 hasta numero y la cantidad de pares: "))

# Proceso
sumaSerie(numero)
    