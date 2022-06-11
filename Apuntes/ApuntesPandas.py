# APUNTES PANDAS
# pandas es una herramienta que sirve para el manejo y analisis de datos
# Las estructuras mas usadas son SEties y DataFrame
# importamos pandas
from re import S
from sqlite3 import Row
import pandas as pd
import numpy as np

# las series es infromacion de un elemento, los DataFrames son formacion de varios eleemntos unidos

# en pandas Series(data=lista, index=indices, dtype=tipo)
# los indices se generan automaticamente
s = pd.Series(["matematicas", "historia", "Economia", "Programacion", "Inges"], dtype="string")
print(s)
print("="*30)  # accedo con los indices explicitos
print(s[2])
print("="*30)
print(s[1:3])
print("="*30)
print(type(s[1:3]))

# Indice explicito
s = pd.Series([15, 12, 21], index = ["Ene", "Feb", "Mar"])
print(s)
print("="*30)
print(s["Ene"]) # acceder alos indices implicitos 

# series a partir de un diccionario
s = pd.Series({"Matematicas": 6.0, "Programacion": 10, "Ingles": 10})
print(s)
print("="*30)
print(s[1:3])
print("="*30)
print(s["Programacion"])
print("="*30)
print(s[["Programacion", "Matematicas"]])
print("="*30)

# Filtrar la serie
print(s > 5) # verifica si los valores son mayores a 5 y devuelve una serie con el valor boolenao dependieno de la condicion anterior
print("="*30)
print(s[s > 5]) # extrae los valores que son verdaderos 

# cumsum  ---> suma acumuladad de los valores

# conteo de valores --> muestra cuantas veces se repiten los valores

# funciones de estadistica

# decirle a la serie qeu se describa --- > nos brinda una serie con todos los datos estadisticos

# metodo apply equivalenre al map de python

# DATAFRAME --- > varias coleeciones juntas

datos = {
    'nombre' : ['María', 'Luis', 'Carmen', 'Antonio'],
    'edad' : [18, 22, 20, 21],
    'grado' : ['Economía', 'Medicina', 'Arquitectura', 'Economía'],
    'correo' : ['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
}
df = pd.DataFrame(datos)  
print(df)

print("="*30)

df = pd.DataFrame(["Maria", 18], ["Luis", 22], ["Carmen", 20], columns="Nombre", )

#...

# Leyendo datos desde un archivo csv
