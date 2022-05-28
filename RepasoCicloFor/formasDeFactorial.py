# Testeo

# Calcular el factorial de un numero  
# Lo hacemos usando una funcion la cual se usa asi misma para calcular el factorial

def factorial(n):
    if n == 0 or n == 1:
        result = 1
    elif n > 1:
        result = n * factorial(n-1) 
    return result

n = int(input("Enter a number: "))

print(factorial(n))


# Forma de calcular el factorial con un for
n = int(input("Enter a number: "))
fac = 1
for i in range(1, n+1, 1):
#for i in range(n, 0, -1):
    fac *= i
print(fac)
