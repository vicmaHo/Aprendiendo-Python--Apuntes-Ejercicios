#  Imprimir en pantalla ---> print
from pickle import TRUE


print("Hello")
# Entradas de datos
input("Enter data: ") # Podemos transformar esto a diferentes datos indicando el tipo de dato anteriormente

# Tipos de datos

a = 12             #Integeer Int
b = 12.5        #Float 
c = "Hello"     #string str
d = True        #Boolean bool
e = 3j          # Complex

# Funcion rango --- > genera un rango de 0, a n-1 numeros, con saltos n
range(0, 10, 2) # De 0 a 9, de dos en dos

# Estructuras basicas de datos:  T IPOS SECUENCIALES 

# Lista, un conjunto de elementos el cual puede ser  modificado  - mutables
list = [1, "vic", "3", 4.15, True, ["in", "out"]] # Lo ideal es que en las listas solo se encuentren elementos de un tipo de dato

# Tupla ---> Conjunto de elementos, NO puede ser modificado
tuple = (1, 2, "Hello", False, "Abril") # Al igual que las lo ideal es que tengan un tipo de dato


# Mapas o diccionarios --> coleccion de elementos que tienen una clave y un valor
dict = {"key": "value",
            "nombre": "name",
            32: 456,
            True: False, 
            "age": 18,}
# Las llaves siempre tienen que tener el mismo tipo de dato
# Ejemplo de diccionario ----> almacenar la informacion de una persona nombre, edad, estatura etc

# Coinjuntos --> elementos de daots simples los cuales no se pueden REPETIR-
setFrontset = {1, 2, 3, 4} # En los conjutnos no existe orden a diferencia de en las tuplas y listas que si existe un orden

# frozenset ----> conjuntos que no se pueden modificar 
print(setFrontset)

# TIPOS BOOLEANOS Verdadero o falso, prendido o apagado ----> toma de desiciones
True
False


# VARIIABLES --> Espacio en memoria en donde se guarda una informacion
# Cuenta con un nombre y un valor --> Guardar cualquier tipo de informacion 
# Se asignan de la siguiente forma nombre = valor, el igual se usa para asignar, guardar el valor 
 
 
mi_variable1 = 3
# Como python es de tipado dinamico no es necesario declarar el tipo de valor que tendra la variable
# Podemos reasignar valores a las variables

# Podemos nombrar las variables con mayusculas minusculas numeros, estas tienen que iniciar con un caracter (min mayu o linea baja)
 #snake_case o camelCase o PascalCase ---> formas de escribir variables
 # Para declarar constantes y no variables, usamos mayusculas sostenidas ----> las constantes son variables que no deberian de cambiar de valor
 
 
 # CONVERTIR TIPOS DE DATOS
 # esto lo podemso hacer con la funcion referente a cada tipo de dato
flotante = float (8); cadena = str(3) ; entero = int("3") # convertimos cada valor en lo que se encuentra afuera

# tambien se pueden convertir rangos en conjuntos, listas, tuplas ---- > list(), tuple(), set()
rango = range(1, 7)
print(list(rango))
print(set(rango))

cadena = "Hola"
print(list(cadena)) # cogemos todos los elementos de la cadena y los convertimos a individuales en una lista
lista = list(cadena)

print(list[4])

# asignacion de operacions
# podemos simplificar lo siguiente
sumar = 0
sumar = sumar + 1

# lo hacemos asi
sumar += 1
 # lo que estamos haciendo es a la variable suamr le sumamos 1 mas lo que tenga almacenado y este resultado lo guardamos en la mis a variable