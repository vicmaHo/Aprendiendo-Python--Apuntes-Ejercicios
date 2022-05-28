"""
desarrollar un programa que pregunte el numero de estudiantes de un curso,
 luego pregunte el nombre de cada uno de ellos. finalmente se debe mostrar un listado 
 con todos los estudiantes                        
"""

numEstudiantes = int(input("Ingrese el numero de estudiantes: "))
listaEstudiantes = ""

for i in range(0, numEstudiantes):
    nombre = input("Digite el nombre del estudiante " + str(i + 1) + ':') # con un f string sale mas sencillo
    listaEstudiantes = listaEstudiantes + nombre + '\n'

print(listaEstudiantes)
