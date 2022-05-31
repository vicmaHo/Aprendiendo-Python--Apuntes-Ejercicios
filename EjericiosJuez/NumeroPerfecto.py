# Un entero positivo n se llama perfecto si n es igual a la suma de todos sus divisores diferentes de él. 
# Por ejemplo, 6 es perfecto porque 6=1+2+3. Escriba un programa que reciba como entrada un número entero 
# positivo y retorne un booleano indicando si es perfecto o no.

n = int(input())

def numero_perfecto(n):
    acc_num = 0
    for i in range(1, n):
        print(f"I: {i}")
        if n % i == 0:
            acc_num+= i
    if acc_num == n:
        return True
    else:
        return False

print(numero_perfecto(n))