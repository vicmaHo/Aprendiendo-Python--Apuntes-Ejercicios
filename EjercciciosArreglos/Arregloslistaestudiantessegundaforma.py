# Generar una lista de estudiantes de un curso

n = int(input("Ingrese el numero de estudiantes: "))

listaEstudiantes = [None] * n

for i in range(n):
    listaEstudiantes[i] = input("Ingrese el nombre del estudiante: ")
    
    
print("\nLista estudiantes")
for i, n in enumerate(listaEstudiantes):
    print(f"{i+1}.{n}")