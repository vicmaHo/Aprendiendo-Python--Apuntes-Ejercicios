"""
PROBLEMA 1

Integrantes: 
-Victor Manuel Hernandez Ortiz  - 2259520
-Juan Pablo Castaño Arango      - 22559487
-Juan Pablo Escobar Viveros     - 2259519

Profesor: Andres Fernando Velasco
Grupo: 50
Laboratorio: 1

"""

#entradas
print(
"""Bienvenido, este es el programa de registro de peliculas
Por favor ingrese los datos pedidos""")

titulo = input("\nDigite el titulo de la pelicula: ")
paisOrigen = input("Digite el pais de origen de la pelicula: ")
genero = input("Digite el genero de la pelicula: ")
duracionMinutos = int(input("Digite la duracion de la pelicula en minutos: "))
anioEstreno = int(input("Digite el año de estreno de la pelicula: "))

#salida
print(
f"""\nDATOS DE LA PELICULA

TITULO: {titulo}
PAIS DE ORIGEN: {paisOrigen}
GENERO: {genero}
DURACION: {duracionMinutos} minutos
AÑO DE ESTRENO: {anioEstreno}""")

