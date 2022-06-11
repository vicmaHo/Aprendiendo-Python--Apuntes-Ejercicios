# MANEJO DE DICCIONARIOS
# almaceno datos con una estructura llave --- valor 


profesor = {}
profesor = dict()
# cualquiera de las anteriores sirve para crear un dicionario   
# los valores pueden ser de cualquier tipo, pero las keys tienen que ser de un solo tipo de dato para 
# todo las llaves del diccinario

profesor = {
    "key": "value",
    "nombre": "Victor",
    "nacionalidad": "colombiano",
    "soltero": True,
    "edad": 18
}

# esto lo puedo cargar en un archivo csv
print(profesor)

# MANIPULAR DICCINARIOS recordar que los diccionarios son modificables
profesor["nombre"] = "Manuel" # al diccionario[elemento/llavea buscar que quiero modificar] = elemento nuevo

print(profesor)

profesor["edad"] += 43
print(profesor)

# añado una llave y un valor a un diccionario
profesor["estudiante"] = {"nombre": "Alex", "nota": 3.0}
print(profesor)

# para eliminar algo en python --> del
del profesor["key"]
print(profesor)

# extraer informacion de un diciconario
print("Nombre:", profesor["nombre"])
# sacar un dato de un diccionario dentro de un diccionario
print("Estudiante:", profesor["estudiante"]["nombre"]) # de profesor sacamso estudiante y de estudiante sacamos el nombre

# sacamos el diccionario estudiante y luego sacamos los valores que necesitemos
# estudiante = profesor["estudiante"]
# print("Nombre estudiante:", estudiante["nombre"])


# uso de diccionarios en funciones
def calculoPromedio(estudiante):
    promedio = (estudiante["nota1"] + estudiante["nota3"] + estudiante["nota4"] + estudiante["nota2"]) / 4
    return f"El estudiante {estudiante['nombre']} ha obtenido una nota de {promedio:.1f}"

estudiante = {
    "nombre": "victor",
    "nota1": 3.0,
    "nota2": 5.0,
    "nota3": 5.0,
    "nota4": 4.5
    
}

promedio = calculoPromedio(estudiante)
print(promedio)
