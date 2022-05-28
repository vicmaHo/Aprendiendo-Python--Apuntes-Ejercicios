# Diseñe un algoritmo que determina si un número es par o impar. Recuerde que un número 
# es par si el resto de una división entera con el número 2 es cero.

def ParOImpar(n):
    if n % 2 == 0:
        return f"El numero es par"
    else:
        return f"El numero es impar"
    
n = int(input("Ingrese un numero: "))

print(ParOImpar(n))
