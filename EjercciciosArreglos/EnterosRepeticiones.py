"""
Escriba un programa en Python que dada una lista de
enteros y un valor x por parte del usuario, diga cuántas
veces x aparece en la lista. El programa como salida
debe mostrar la lista ingresada por el usuario e indicar
cuántas veces aparece el valor x y en cuáles posiciones.
"""

lista =[]
posiciones = []
while True:
    valor = int(input("Ingrese un valor a la lista (ingrese -1 para finalizar): "))
    if valor == -1:
        break
    lista.append(valor)
x = int(input("Ingrese x: "))
print("la lista es: \n",lista, "\n")


print(f"{x} se repite {lista.count(x)}")

for i,n in enumerate(lista):
    if n == x:
        posiciones.append(i)
        print(f"x se encuentra en la posicion {i}")

print("\nx se encuentra en las posiciones: ", end=" ")
for i in posiciones:
    print(i, end=",")



