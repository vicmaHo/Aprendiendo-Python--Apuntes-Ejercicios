# version mia 
n = int(input("Ingrese el numero: "))
m = 0
for i in range (1, n+1):    # cuenta cuantas veces se cumple la condicion del if 
    if (i % 3) == 0:
        print(i)
        m +=1
print(f"existen {m} numeros multiplos de 3")


# forma mas sencilla
m = 0

for i in range(3, n+1, 3): #  cuenta cuantas veces esta pasando por el for
    print(i)
    m += 1
print(f"existen {m} numeros multiplos de 3")

