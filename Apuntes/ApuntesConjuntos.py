# CONJUNTOS
"""
Los conjuntos son colecciones no ordenadas de objetos unicos, es decir, no se pueden repetir
Creacion de conjuntos:
los elementos de un conjunto se especifican entre llaves, sus elementos pueden ser de diversos tipos
Pero no pueden ser elementos mutables, como listas, diccionarios u otros conjuntos.

conjuntoA = {1, 2, 3, 4, (1,2), True, "False", 1.5}}

"""

# Python interpreta lo siguiente como la creacion de un diccionario vacio
conjunto = {}
# Por lo tanto para crear un conjunto vacio usamos la siguiente instruccion
conjunto = set() # set : conjunto

# se pueden obtener conjuntos a partir de cualquier objeto iterable
conj1 = set([1, 2, 4, 5])
conj2 = set(range(1,6))

# los conjuntos se pueden transformar en listas
conj1 = list({1, 2, 3, 4})
# las listas se pueden transformar en conjutnos, los elementos que se repiten son unificados en un solo elemento
# ya que los conjuntos no pueden contener elementos duplicados
conj2 = set([1, 2, 2, 3, 3, 3, 4, 4]) # ---> {1, 2, 3, 4}


"""Cosas aprendidas random: a is b --> is devuelve True si las dos variables apuntan a el mismo objetivo, 
compara la identidad de dos objetos .

in --- > el operador in devuelve True si un elementos se encuentra dentro de otro

len ---> obtenemos el numero de elementos de una coleccion
"""

"""
Los conjuntos son coleccines mutables, para esto usamos los metodos add() y discard(), clear()
"""
# añadir elementos
conj2.add(3.4)
# remover elementos
conj2.remove(2)

# eliminar todos los elementos
conj3 = {2, 3, 1, 4 , 6}
conj3.clear()


"""
Operaciones principales entre conjuntos:
union: | --> Retorna un conjunto que contiene los elementos que se encuentran en almenos uno de los dos conjuntos
interseccion: & ----> retorna un nuevo conjunto con los elementos que se encuentran en ambos
diferencia: - ---> retorna un nuevo conjunto con los elementos de a que no esten en b
"""
# para ralizar una copia del conjunto
conjuntoNuevo = conj3.copy()


"""
CONJUNTOS INMUTABLES: frozenset
estos se comportan como conjuntos, pero tienen la caracteristica de que no pueden ser modificados, no podemos usar add(), discard(), clear
Pero podemos realizar todas las demas operaciones entre conjuntos
"""
inmutable = frozenset({1, 2, 3})

