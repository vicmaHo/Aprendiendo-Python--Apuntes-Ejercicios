# practica arreglos 1

n = int(input("Ingrese una cantidad para n: "))

arreglo = [None] * n

# solicitar al usuario cada uno de los n numeros

for i in range(n):
    arreglo[i] = int(input(f"Ingrese el dato numero {i + 1}: "))
    
    
# mostrar todos los numero en un solo mensaje
print(arreglo)

# mostrar los numeros almacenados en posiciones pares
for i in range(n):
    if i % 2 == 0:
        print(f"en la posicion par {i} se encuentra almacenado el numero: {arreglo[i]}")
            
for i in arreglo:
    if i % 2 != 0:
        print(f"El numero {i} contenido en el arreglo es impar.")