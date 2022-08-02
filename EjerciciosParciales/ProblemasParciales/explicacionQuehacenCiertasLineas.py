# Explicaciones a una serie de instrucciones

datos = [[0 for x in range(3)] for y in range(3)]
datos[0][0]=3
datos[0][1]=7
datos[0][2]=6
datos[1][0]=9
datos[1][1]=12
datos[1][2]=2
datos[2][0]=7
datos[2][1]=5
datos[2][2]=10

for i in datos:
    print(i)
    
############## primer punto
s=0
for i in range(0,3,1):
    for j in range(0,3,1):
        if (i+j==2) and (datos[i][j]%3==0):
            s = s + datos[i][j]
print(s)
# RESPUESTA:
"""
Al ejecutar estas resulta: 18

lo que hace esta parte del codigo es definir una variable s, y se inicializa en 0
posteriormente con un for anidado se recorre cada valor de la matriz "datos".
Primero se recorren las filas, usando los indices desde 0 hasta 3 yendo de 1 en 1, cuando hace
esto se queda "anclada" la fila y se pasa a recorrer las columnas
igualmente se recorren con un for desde 0 hasta 3 saltando de 1 en 1.
Cuando hacemos una iteracion de la columna, se verfica la siguiente condicion:
si la fila mas la columna son iguales a 2 y si el valor que se encuentra en la posicion
respectiva de la fila y la columna es multiplo de 3, pues entonces a "s" se le suma
el valor que se encuentra en la posicion fila columna actuallmente
se pasa al for que recorre las filas y se vuelve a realizar lo mismo, usando de acumulador
la varible s quien al final es impresa en pantalla
"""
print("="*50)

############## Segundo punto
for i in range(0,3,1):
    for j in range(0,3,1):
        if (i<j):
            print(datos[i][j])
# RESPUESTA:
"""
Este codigo arroja lo siguiente:
7
6
2

lo que hace esta parte de codigo es recorrer los indices de la matriz
se realiza con un for anidado, con el primer for se recorren las filas, de 0 hasta 3 con saltos de 1 en 1
con el segundo for se recorren las columnas de 0 hasta 3 con salto de 1 en 1.
Primero se queda fijada la fila, y se reccorren las columnas correspondientes a esta fila
al recorrer cada columna se da la siguiente condicion: si el indice de fila es menor que el 
indice de columna, entonces se debe imprimir el dato que se encuentra en la posicion correspondinte
a la fila y la columna que se estaba verficando
"""
print("="*50)


############## Tercer punto
# 3 Escriba el segmento de código necesario para promediar los elementos que se encuentran bajo la
#diagonal principal (Su solución debe servir para cualquier tamaño de una matriz cuadrada)

# RESPUESTA:
sumElemento = 0
numElemento = 0
for i in range(len(datos[0])):
    for j in range(i):
        numElemento +=1
        sumElemento += datos[i][j]

print("El promedio de la suma de los elementos que estan bajo la diagonal principal es de: ", sumElemento/numElemento)
print("="*50)
"""
En este caso se realiza el ejemplo con la matriz "datos"
"""
"""
Aca presento otro ejemplo para verificar si se puede realizar con cualquier tamaño de matriz cuadrada:
"""
datos2 = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [7, 21, 3, 4, 6],
    [8, 9, 1, 2, 0],
    [2, 1, 5, 6, 7]
]
sumElemento = 0
numElemento = 0
for i in range(len(datos2[0])):
    for j in range(i):
        numElemento +=1
        sumElemento += datos2[i][j]
print("El promedio de la suma de los elementos que estan bajo la diagonal principal es de: ", sumElemento/numElemento)