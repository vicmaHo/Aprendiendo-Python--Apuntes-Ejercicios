# Suponga que se desea crear un programa en Python que permita imprimir
# en pantalla la cantidad de números múltiplos de 3 que se encuentran en la
# serie 1 a n, siendo n un número digitado por un usuario.
def esMultiploDeTRes(a):
    if a % 3 == 0:
        return True
    else:
        return False

def multiploTres(n):
    contador = 0
    for i in range(1, n+1):
        if esMultiploDeTRes(i):
            contador += 1
            
    print(f"La cantidad de numero multiplos de 3 desde 1 hasta {n} es: {contador}")
    
n = int(input("Ingrese el numero: "))

multiploTres(n)
