# Ejercicio del cuadrado magico

# la matriz se puede recoger por filas o por columnas 

# hago un for que contendra otro for, ambos for van de 0 a n--->  el primer for fija i, y se empieza a mover la j recorrido por folas 
# dentro ira matriz[i, j] se quiero fijar la fila e ir por columnas, matriz[j, i] si quiero fijar la fila e ir por columnas

# Programa del cuadrado magico


n = int(input("Digite el tamaño del cuadrado magico (un impar): "))

cuadro = [[0 for i in range(n)] for j in range(n)]
# establezco la posicion del primer numero el primero lo coloco en la mitadad de la primer fila
fila = 0
columna = n // 2 # asi para que nos devuelva el numero entero
for num in range(1, (n**2) + 1):
    cuadro[fila][columna] = num
    # cuando ponemos un termino, preparamos las coordenadas apara poner otro
    if num % n == 0:
        fila += 1
    else: 
        columna += 1
        if columna == n:
            columna = 0
        fila -= 1
        if fila == -1:
            fila = n - 1
            
for i in range(0, n):
    print(cuadro[i])
    
# reto: hacerlo para cuadrados pares