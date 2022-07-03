"""
Desarrollar un programa que permita evaluar una función por partes. Dado un valor de x se calcula el
valor de f(x) utilizando la funcion que se muestra a continuación:
f(x) --> 8x**2 - 6      si x <= 0
f(x) --> 3x + 5         si x > 0
El programa a desarrollar debe definir una función en la que se calcula el valor de f(x).
"""
#creo la funcion
def fx(x):
    if x <= 0:
        return 8 * (x ** 2) - 6
    else:
        return 3 * x + 5

# ingreso x
x = int(input("Ingrese x: "))

# proceso
resultado = fx(x)

#salida
print(f"f({x}) = {resultado}")