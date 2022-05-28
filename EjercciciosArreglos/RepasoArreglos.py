# repaso de arreglos - ingresar a los estudiantes de un curso en un arreglo

numeroEstudiantes = int(input("Ingrese el numero de estudiantes: "))
listaEstudiantes = [None] * numeroEstudiantes

for i in range(numeroEstudiantes):
    listaEstudiantes[i] = input("Ingrese el nombre del estudiante: ")
    
# imprimir la lista en forma descente

numero = 0
for estudiante in listaEstudiantes:
    numero += 1
    print(f"{numero}. {estudiante}")
# agregar un elemento externo a un arreglo
listaEstudiantes.appendinput("Ingrese el nuevo estudiante: ")
    
for i in range(len(listaEstudiantes)):
    print(f"{i + 1}. {listaEstudiantes[i]}")
    
