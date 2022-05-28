
# El mismo ejercicio de los asteriscos planteado de una forma diferente

numeroFilas = int(input("Ingrese el numero de filas: "))
triangulo = ""
for i in range(1, numeroFilas+1, 1 ):
    for j in range(1, i+1, 1):
        triangulo += "*"
    triangulo += "\n"
    
print(triangulo)