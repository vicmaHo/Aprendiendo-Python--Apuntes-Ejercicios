''' *comentario multilinea*
Se trata de elaborar un programa que lea el nombre y el añp de nacimieno de una persona
y muestre al final un saludo a esa persna indicando ademas la edad a cumplir en el 2022
NOTA: Este programa utiliza "la secuencia" e instrucciones de "entrada/salida" 
Autor: Nombre del autor
Fecha: fecha en la que hizo el programa
Contacto: 


La estructura es ---- entrada----> proceso ----> salida

para poder entender el programa comenzamos por la salida, esto en caso de que no tengamos muy presente
cuales son las entradas

'''

"""La secuencia: """

"""los comentarios los puedo usar cuando necesite que por ejemplo mi yo del futuro entienda el codigo
"""

# entrada de datos
nombre = input("Ingrese el nombre\n")  # salto de linea para ingresar el nombre, se puede hacer por dos
anioNacimiento = int(input("Ingrese el año en que nacio: "))

# proceso de datos

anioCumple = 2022 - anioNacimiento # se calcula edad a cumplir en el 2022

# salida 
print(f"Hola {nombre}, este año cumples {anioCumple} años")  # es un f string
print("Hola", nombre, "este año cumples", anioCumple, "años")
