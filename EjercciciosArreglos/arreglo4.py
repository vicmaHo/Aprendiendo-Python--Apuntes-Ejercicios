# Escriba un programa en Python que lea una lista de n
# enteros, calcule el promedio de los datos ingresados, el
# mayor y el menor de ellos.

n = int(input("Ingrese n enteros: "))
listaN = [None] * n

for i in range(len(listaN)):
    listaN[i] = int(input(f"Ingrese el numero en la posicion {i}: "))

accPromedio = 0
for i in listaN:
    accPromedio += i

promedio = accPromedio / len(listaN)
print(f"El promedio es de; {promedio}")

# maximo
print(f"El maximo numero en la lista es {max(listaN)}")

# minimo
print(f"El minimo numero en la lista es: {min(listaN)}")    
