# Diseñe un algoritmo que determine si un número real (x) se encuentra dentro del
# rango abierto-cerrado (3.5, 7.8].




def estaRango(x):
    if x > 3.5 and x <= 7.8:
        return f"el numero si se encuentra en el rango"
    else:
        return f"el numero no se encuentra en el rango"

n = float(input("Ingrese un numero: "))

print(estaRango(n))