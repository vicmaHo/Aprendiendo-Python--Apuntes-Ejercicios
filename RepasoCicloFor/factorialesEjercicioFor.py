# Suponga que se desea crear un programa en Python que permita imprimir
# en pantalla el factorial de cada número existente en la serie 1 a n, siendo
# n un número menor a 20 el cual es digitado por un usuario.


# Funcion para sacar el factorial de n numero en este caso usaremos un for para hallar el factorial - no la estoy usando
def factorial(n):
    if n == 1 or n== 0:
        result = 1
    elif n > 1:
        result = n * factorial(n-1)
    return result

#  Funcion para comprobar que el numero ingresado se encuentre en el rango correcto
def check():
    while True:
        n = int(input(("Numero entre 1 y 20:")))
        if n >= 1 and n <= 20:
            return n 
            break

n = check()
resultado = 1
for i in range(1, n+1, 1):
    resultado = 1
    for j in range(1, i+1 , 1):
        resultado *= j
    print(f"El factorial de {i} es: {resultado}")
        
        


