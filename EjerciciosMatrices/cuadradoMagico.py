# Se trata de agregar la opción para que el cuadrado mágico sea par
# Cuadrado mágico
n = int(input("Digite el tamaño del cuadrado: "))
cuadro = [[0 for i in range(0,n)] for j in range(0,n)]
f=0
c=n//2
for num in range(1, n**2+1):
    cuadro[f][c] = num
    if(num%n==0):
        f += 1
    else:
        c += 1
        if(c==n):
            c=0
        f -= 1
        if(f==-1):
            f=n-1
for i in range(0, n):
    print(cuadro[i])