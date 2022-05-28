"""
ambito de variables:
contexto o el espacio en donde esa varaible puede ser usada y reconocida

Variables locales: son aquellas que se crean dentro de una funcion, estas vaiables solamento son reconocidas
donde fueron creadas y su valor se pierde al finalizar la ejecucion de la misma

Variables globales,: son aquellas que son reconocidas en todo lugar del programa
estas pueden ser asiganas fuera de cualquier metodo, en el programa principal o se pueden referenciar
dentro de un metodo con la palabra reservada "global."

"""

# var local

def calcularhipotenusa (a, b):
    h = a * b
    return h # h es una variable local

"""
las funciones pueden tomar variables globales
"""