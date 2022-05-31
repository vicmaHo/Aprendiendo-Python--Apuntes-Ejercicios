'''
Se trata de hacer un programa que lea una matriz cuadrada de enteros y, 
1. calcule la suma de los elementos de la diagonal principal
2. calcule la suma de los elementos de la diagonal secundaria
3. calcule la suma de los elementos encima de la diagonal principal (triangular superior)
4. para una matriz cuadrada de lado impar, imprimir en secuencia los elementos desde el [0][0]
   hasta el [n//2][n//2] en espiral en el sentido de las manecillas del reloj
5. Si en la matriz solo se ingresan 0's y 1's, hacer una función que encuentre secuencias de
   n 1's o n 0's bien sea en horizontal, vertical o diagonal
6. Utilice la función del punto anterior para ayudarse en la implementación de un programa para
   jugar triqui (triki, tic tac toe)
'''
def sumaDiag1():
    suma = 0
    for i in range (0, n):
        suma += cuadro[i][i]
    return suma

n = int(input("Digite el tamaño de la matriz: "))
cuadro = [[0 for i in range(0,n)] for j in range(0,n)]
for i in range (0, n):
    for j in range(0, n):
#        cuadro[i][j] = int(input("Digite cuadro["+str(i)+"]["+str(j)+"]: "))
        cuadro[i][j] = int(input(f"Digite cuadro[{i}][{j}]: "))
print(f"La diagonal principal suma: {sumaDiag1()}")