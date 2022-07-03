# Se requiere un programa para almacenar los
# resultados de las ultimas elecciones de rector de la universidad.
# Los datos deben almacenarse en una matriz donde
# cada fila corresponde a una sede y cada columna corresponde a
# un candidato. El programa debe mostrar la tabla con los
# nombres de las sedes y los nombres de los candidatos y cada
# uno de los resultados. La aplicación también debe mostrar el
# candidato ganador.

nCan = int(input("Ingrese la cantidad de candidatos: ")) + 1
nSedes = int(input("Ingrese la cantidad de sedes: ")) + 1

array = [[0 for c in range(nCan)] for f in range(nSedes)]

## ingresar candidatos
for c in range(1,len(array[0])):
    array[0][c] = input(f"Ingrese el candidato {c}: ")

for f in range(1,len(array)):
    array[f][0] = input(f"Ingrese la sede {f}: ")
    
for i in array:
    print(i)

## ingreso de votos

for c in range(1, len(array[0])):
    for f in range(1, len(array)):
        array[f][c] = int(input(f"Ingrese los votos de {array[0][c]} en {array[f][0]}: "))
        
for i in array:
    print(i)
    
# array = [
#     [0, 'Victor', 'Manuel'],
#     ['Buga', 21, 34],
#     ['Cali', 12, 54]
# ]

array[0][0] = "Candidatos\nSedes"
## mostrar la tabla
Tabla = ""
for i in range(len(array)):
    for j in range(len(array[0])):
        Tabla += str(array[i][j]) + "\t\t"
    Tabla += "\n"
print(Tabla)
    
# mostrar el candidato ganador
candidatos = []
totalvotos = []

for c in range(1, len(array[0])):
    votos = 0
    for f in range(1, len(array)):
        candidato = array[0][c]
        votos += array[f][c]
    candidatos.append(candidato)
    totalvotos.append(votos)
    
votosGanador = max(totalvotos)
candidatoganador = candidatos[totalvotos.index(votosGanador)]
print("=" * 30)
print(f"El candidato ganador es: {candidatoganador} con un total de {votosGanador} votos")

