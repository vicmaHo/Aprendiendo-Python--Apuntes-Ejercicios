"""
Escriba un programa en python que solicite los nombres de caada estudaiante de cualquier curso y 
los muestre a ttodoa de forma numerada al final. Use un arreglo para almacenar el nombre
de cada estudiante

"""

# numero de estudiantes, preguntamos por el nombre y lo alamacenamos en un arreglo

#leer el numero de estudiantes
n = int(input("Numero de estudiantes: "))

#Leer los nombres de n estudiantes
listaEstudiantes = [None] * n
controlador = 0

# con un for seria:
# for i in range(0, n):
#   nombres[i] = input(f"Digite el nombre del estudiante { i + 1} :")
while controlador < n:
    listaEstudiantes[controlador] = input(f"Digite el nombre del estudiante {controlador + 1} : ")
    controlador += 1


# imprimimos los nombres de forma numerada al final
for i in range(0, n, 1):
    print(f"{i + 1}. {listaEstudiantes[i]}")


linea = ""
for i in range(0, n):
    linea += str(i + 1) + ". " + listaEstudiantes[i] + " -- "
print(linea)





