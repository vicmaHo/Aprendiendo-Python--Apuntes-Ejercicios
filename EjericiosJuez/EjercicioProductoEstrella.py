import numpy as np 
# creacion de la lista
dias=int(input("Ingrese la cantidad de dias en los que vendio productos: "))
productos=np.array([None]*dias)
# introduccion de datos en la lista
for i in range (dias):
    productos[i]=int(input(f"Ingrese el codigo del producto del dia {i+1}: "))

#arreglo de prueba
# productos = np.array([11,16,19,11,17,13,19,19,13,12,11,19,15,14,14,18,18,16,17,12])
# dias = len(productos)
def productoEstrella(productos):
    posiciones1 = []
    posiciones2 = []
    contador=0
    repeticiones=np.array([None]*dias)
    mayor1=0
    mayor2=0
    estrella1=0
    estrella2=0
    for i in range(0,productos.size):
        for k in range(0,dias):
            if productos[i]==productos[k]:
                contador+=1
        for l in range(0,dias): 
            repeticiones[i]=contador
        if contador>0:
            contador=0
        else:
            contador=contador
    for i in range(0,repeticiones.size):
        if mayor1<repeticiones[i]:
            mayor1=repeticiones[i]
    for n in range(0,repeticiones.size):
        for m in range(0,repeticiones.size):
            if repeticiones[m]>repeticiones[n] and repeticiones[m]!=mayor1:
                mayor2=repeticiones[m]
                #manipulando
    for v in range(0,productos.size):     
        for b in range(0,repeticiones.size):
            if repeticiones[b]==mayor1:
                estrella1=productos[b]
                # sacando el segundo
    for i in range(0,productos.size):     
        for j in range(0,repeticiones.size):
            if repeticiones[j] == mayor2:
                estrella2 = productos[j]
    # hallar posiciones donde se repitieron
    for i in range(len(productos)):
       if repeticiones[i] == mayor1:
           posiciones1.append(i+1)

    for i in range(len(productos)):
        if repeticiones[i] == mayor2:
            posiciones2.append(i+1)
    return f"{estrella1} ---> estrella en {mayor1} ocasiones, en los dias {posiciones1}\n{estrella2} ---> estrella en {mayor2} ocasiones, en los dias {posiciones2}"

print (productoEstrella(productos))

