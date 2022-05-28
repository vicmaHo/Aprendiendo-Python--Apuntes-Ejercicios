# Desarrollar un programa Python que pregunte al usuario el número
# de estudiantes de un curso, luego pregunte el nombre de cada uno
# de ellos. Finalmente, se debe mostrar un listado con todos los
# estudiantes.

numberStudents = int(input("Enter the number of students: "))

listStudents = ""
for i in range(0, numberStudents, 1):
    listStudents += input(f"Student name {i + 1}: ") + "\n"

print("The list of estudents:")
print(listStudents)