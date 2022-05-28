# factorial

'''
permitir imprimir en pantalla el factoial de cada numero existente en la serie 1 a n, siendo un numero 
menor a 20 el cual es digitado por un usuario 
'''

n = int(input("Digite el valor de n: "))

for j in range (1, n + 1):
    f = 1
    for i in range(1, j + 1):
        f *= i
    print(f"el factorial de {j} es {f}")