# Se trata de hacer un progrma que lea una matriz ciadrada de enteros y,
# 1. calcule la suma de los elementos de la diagonal principal
# 2. Funcion que sume solo la ddiagonal secundaria, un solo for
# 3. Calcule los elementos encima de la diagonal principal ( Triangular superior)
# 4. Para una matriz cuadrada de lado impar, imprimir en secuencia los elelemntos desde el [0][0]
#   hasta el [n//2][n//2] en espiral en el sentido de las manecillas del reloj
# 5. Si en la matriz solo se ingresan 0's y 1's, hacer una funcion que se encuentre en secuencias de n 1's o n 0's
#   bien sea en horizontal, vetival o diagonal
# 6. Utilice la función del punto anterior para ayudarse en la implementacion de un programa para 
#   jugar triqui (triki, tic tac toe)


# Funcion para calcular la suma de la diagonal principal
def sumaDigonal1():
    suma = 0
    for f in range(0, n):
        for c in range(0, n):
            if f == c:
                suma += cuadro[f][c]
    return suma
                
# def sumadiag11():
#     suma = 0
#     for f in range(0, n):
#         suma += cuadro[f][f]   # con esta hago que la f haga de fila y de columna, ira 1, 1; 2, 2
#     return suma 


# Funcion para calular la diagonal secundaria
def sumaDiagSecundaria():
    columna = 0
    suma = 0
    for f in range(len(cuadro)-1, 0-1, -1):
        suma += cuadro[f][columna]
        columna += 1
    return suma
    
# Calcular la suma de los elementos encima de la diagonal superior
def sumaTriangularSupe():
    pass
n = int(input("Digite el tamaño del cuadro PAR: "))
# cuadro = [[0 for i in range(n)] for j in range(n)]
cuadro = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
# f = fila
# c = columna
# for f in range(0, n):
#     for c in range(0, n):
#        # cuadro[f][c] = int(input("Digite cadrado[" + str(f) + "][" + str(c) + "]: "))
#        cuadro[f][c] = int(input(f"Digite cuadrado[{f}][{c}]: "))
for i in cuadro:
    print(i)
print(f"Suma de la diagonal principal: {sumaDigonal1()}")
print(f"Suma de la diagonal secundaria: {sumaDiagSecundaria()}")

