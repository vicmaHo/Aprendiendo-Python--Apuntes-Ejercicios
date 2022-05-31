# Instrucciones condiconales
# if condicion:
    # instrucciones
# else:
    # instrucciones
    

# si algo sucede haga esto, de lo contrario haga lo otro
# basicamente lo que hacen las instrucciones condicionales es evaluar una expresion y si
# es verdadera se procede a ejecutar las instrucciones que le siguen, pero si es falso, seguira con el proceso
# o si existe alu

# desicion en secuencia -- posibilidad de que una condicion se pueda ejecutar varias veces

# los condicionales en cascada tienen dentro del else un if
# para las condiciones en cascada en el else hay un if

# si el else tiene un if lo podemos convertir en un elif 

# las desicones andidadas son desiciones dentro de desiciones


# Manejo de diccionarios
# almaceno datos con una estructura llave --- valor 


profesor = {}
profesor = dict()
# cualquiera de las anteriores sirve para crear un dicionario   
# los valores pueden ser de cualquier tipo, pero las keys tienen que ser de un solo tipo de dato para 
# to do las llaves del diccinario

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

# sacamso el diccionario estudiante y luego sacamos los valores que necesitemos
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
