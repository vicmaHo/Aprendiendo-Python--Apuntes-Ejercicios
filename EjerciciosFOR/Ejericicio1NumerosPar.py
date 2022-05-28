# Diseñe un algoritmo que permita detectar los números pares
# existentes en una serie de 1 a n, siendo n un número digitado por
# un usuario.

def evenNumber(n):
    for i in range(2, n+1, 2):
        print(i)


# Entradas


n = int(input("Enter a number: "))

# Proceso - Llamar variable - Salida
evenNumber(n)