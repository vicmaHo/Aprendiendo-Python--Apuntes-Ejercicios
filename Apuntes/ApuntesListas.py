"""
Las listas son colecciones ordenadas de valores los cuales pueden ser de cualquier tipo
las listas en python son mutables, es decir poseen un amplio manejo de los elementos que contienen
"""

# Definicion de una lista ---> para representarla usamos los corchetes []
lista = [] # una lista vacia
lista = list() # tambien se puede definir de esta forma

# podemos poner los elementos en su creacion
lista = [1, 2, 3, 4, 5, "Hola", "Victor"]

# A ada uno de los valores de una lista se le conoce como elemento
# Las listas pueden (al igual que los otros tipos de iterables) almacenar otras listas, tuplas, conjuntos...

"""Acceder a los elementos de una lista:
Primero tenemos que saber que cada lista esta ordenada mediante indices, los cuales comienzan
en el 0, por lo tanto, la lista [1, 2, 3] tiene indices 0 - 1 - 2
Estos indices nos sirven para indicar la posicion del elemento en la lista
asi que, el 1 se encuentra en el indice 0
el 2 se encuentra en el indice 1
el 3 se encuentra en el indice 2
y asi sucesivamente...

Indices negativos: los indices negativos recorren la lista de derecha a izquierda
es decir: -1 seria el indice que contiene el ultimo elemento de la lista
"""

# accedemos a los elementos de esta forma
lista[1]
lista[0]


"""Para asignar valores a una lista, hacemos uso del metodo append(elemento o insert(indice, elemento)"""
lista.append("Hola") # agregamos un elemento
lista.insert(0, "vic") # agregamos "vic" al indice 0


"""Slicing:
El slicing; tambien conocido como rebanar, pedazo, etc, es usado para sacar partes de una lista
con esto podemos recortar pedazos de una lista
lista[inicio:fin] --> el fin no lo tomamos

tambien podemos añadir otro paremetro, el salto, indicaria cada cuantos elementos se toma un valor
lista[inicio:fin:salto]
"""
lista[1:3] # tomariamos los elementos del indice 1 hasta el indice 2
lista[:] # tomamos todos los elementos de principio a fin
lista[1:] # tomamos los elementos desde el indice 1 hasta el fin
lista[:3] # tomamos los elementos desde el inicio hasta el indice 2

# tambien lo podemos hacer con indices negativos
lista[:-1] # toma todos los elementos de la lista, menos el ultimo

# con salto
lista = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10]
lista[0:8:2] # va desde el inicio hasta el indice 8, saltando de dos en dos


"""Para recorrer los elementos de una lista usamos un for
con esto podemos realizar diversas operaciones con la lista
tambien la podemos recorrer mediante sus indices usando range()
"""
# recorrer por elemento
for elemento in lista:
    print(elemento)
    
for i in range(len(lista)): # recorrermos la longitud de la lista, es decir, el numero de indices
    print(lista[i]) # imprimimos el elemento que se encuentra en el indice i
    
# Otros metodos de listas
# append() agregar elementos
# count() nos devuelve la cantidad de veces que aparece el valor dentro de la lista
lista.count(3) # devuelve 1, ya que el 3 solo esta una vez en la lista

lista2 = [1, 2]
# extend() con este podemos extender la lista con otra coleccion
lista.extend(lista2) # le agregamos a lista los elementos de lista2


# index() nos sirve para hallar el indice en el cual se encuentra cierto elemento
lista2.index(2) # nos devuelve el indice 1

# pop() elimina el ultimo elemento de la lista, y lo muestra
elimiado = lista.pop() # podemos indicar que elemento eliminaos dandole un indice como parametro

# remove() remueve un elemento de la lista, en este caso nosotros indicamos el elemento
lista.remove(3)

# sort() ordena la lista
# reverse() invierte la lista
# clear() borra todos los elementos de la lista

del lista # con del eliminamos la variable 

# split() nos sirve para separar una cadena, este la separa dependiendo del valor que le asignemos
# y la convierte en una lista
mensaje = "Hola soy victor"
lista3 = mensaje.split()
print(lista3)