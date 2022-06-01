## APUNTES CLASE 12 PROGRAMACION FUNCIONAL EN PYTHON
## Recordatorio de lo visto anteriormente en funciones

# definicion de funciones
from doctest import FAIL_FAST
from email.mime import multipart
from syslog import LOG_DAEMON


def saludar(nombre):
    print("Hola mundo" + str(nombre))
    
saludar("Victor")

# retornar mas de un valor
def retornaVarios():
    return "victor", "Hernandez", 18, "Buga"
# esto retorna una tupla con estos datos

tuplaValores = retornaVarios()


# recibir parametros de forma dinamica
# el asteristico indica que eso sera dinamico es decir variable (recibe varios parametros) y los guarda en la variable args como una tupla
def sumaVariable(*args):
    pass

def promedioNotas(codigoEstudiante, *notas):
    if len(notas) == 0:
        promedio = 0
    else:
        promedio = round(sum(notas)/len(notas), 1)
    return f"El estudiante {codigoEstudiante} obtuvo una nota de: {promedio}"

# con un doble asteristo **datos se convierte en un diccionario

def imprimirDiccionarios(**datos):
    print(datos)

sexo = "Masculino"
imprimirDiccionarios(sexo=sexo,nombre={"primerNombre": "Victor", "segundoNombre": "Manuel"}, apellido="Hernandez", edad=18, ciudad="Pereira") # los datos se los damos con nombre de llave y valor


## ALCANCE DE LAS VARIABLES(scope = en qúebloque existe una variable)
## Las variables declaradas fuera de la funcion son globales, se pueden usar en funciones sin necesidad de declararlas
## las variables declaradas en funciones solo se pueden usar en funciones
## se recomienda no usar variables globales
nombre = "Victor"
edad = 18
def imprimirNombreEdad():
    nombre = "Manuel"
    edad2 = edad +1
    print("Nombre en funcion:", nombre, edad2)
imprimirNombreEdad()
print("Nombre fuera de función:", nombre, edad)

## podemos modificar variables globales dentro de funciones añadiendo "global nombreVariable, nombrevariable2" (se recomienda nunca usar esto)
nombre = "victor"
def imprimirGlobal():
    global nombre
    nombre = "manuel"
    print("Nombre dentro de la funcion:", nombre)
print("Nombre fuera de la variable:", nombre)

## PROGRAMACION FUNCIONAL
# funcionaes lambda (anonimas)
def incrementar(x): # esta funcion tiene nombre
    return x +1
incremento = lambda x: x +1 # lambda indica que es una funcion sin nombre, guardar funciones en variables

print (f"Incremento de 9: {incremento(9)} {incrementar(9)}") # la llamamos de esta forma

raizCuadrada = lambda x: x**(1/2)
print(raizCuadrada(121))
diferenciCuadrado = lambda x1, x2 = 0: (x1 - x2)**2
print(diferenciCuadrado(10, 8))

# las lambda solo deben ser usadas para realizar tareas simples qeu no requieran de definir una funcion 
# la idea es que se realicen en una sola linea, si esto no es posible lo mejor es usar una funcion nomal

funcionCompleja = lambda x, func: x + func(x)
print(funcionCompleja(2, lambda x: x * x))    # lo que hago es mandar le parametro dos que se almacenaen x y una funcion lammda que se almacenae n func
print(funcionCompleja(2, lambda x: x + 3))
# en esto vemos que se pueden recibir funciones lambda como parametro, nos facilita realizar
# cambios al codigo sin necesidad de modificar demasiadas cosas 

# Closure (envolturas) funciones que generan funciones

def construieMultiplos(factor):
    return lambda valor: valor * factor

multiplosDe2 = construieMultiplos(2) # esto devuelve un lamba valro: valor * 2
multiplosdDe7 = construieMultiplos(7)
print(multiplosDe2(10))

print([multiplosdDe7(num) for num in range(1, 11)])

print([ construieMultiplos(57)(num) for num in range(1,11)])


def outerFunc(x):
    y = 4
    def innerFunc(z):
        print(f"x = {x}..")
        return x + y + z
    return innerFunc
clousure = outerFunc(0)
print(f"clousure(5) = {clousure(5)}") 




### FUNCIONES SOBRE COLECCIONES
# funcion map(function, iteralble(s))
# aplica trasnfomraciones a una lista y genera elementos 
fruit = ["Apple", "Banana","Pear", "Apricot", "Orange"]

def starsWithA(s):
    return s[0] == "A"

lista = list(map(starsWithA, fruit)) # map coje cada elemento de la lista le aplica la trasnformacion a cada una de la lista
# y lo almacenamos en luna lista
print(lista)
# con lo anterior generamos una lista la cual contiene true o false dependiendo de la evaulacion de map

# podemos hacerlo con funciones lambda
lista = list(map(lambda s: s[0] == "A", fruit))
print(lista)


## FUNCION filter(function, iterable(s))
# aplica una condicion y solo deja pasar a los que la culpen
lista = list(filter(starsWithA, fruit)) # filta los que cumplen la funcion y los pasa a lista, la funcion
# de filter tiene que devolver un true o false, puede ser lambda o funcion normal
print(lista)

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes)) # [::-1] empieza desde el principio hasta el final con saltos de -1
print(palindromes)


## FUNCCION REDUCE(funcion, secuencia, valor inicial)
# coje una coleccion y la convierte en un solo dato
from functools import reduce

lista = [2, 4, 7, 3]
valor = reduce(lambda x, y: x+ y, lista)
print(valor)

lista = [2, 4, 7, 3, "ABC", [1,2, "a"]]
valor = reduce(lambda x, y: str(x) + str(y), lista, 10)
print(valor)

## FUNCION ZIP
# zip(*terables) une los elementosde una lista los comprime

a = [1, 2]
b = ["uno", "dos"]

print(list(zip(a, b))) # devuelve una lista de tuplas

# solo puedo comprimir hasta la misma cantidad de elementos 

# podemos cancelar el zip (descomprimir lo generado por zip)
c = [(1, "one"), (2, "two"), (3, "three")]
a, b = zip(*c)
print(a)
print(b)


## FUNCION enumerate(iterable)
lenguajes = ("java", "c", "c++", "rsut", "elixier")
print(list(enumerate(lenguajes, 1))) # se le añade un numero a cada elemento

print([f"{index}. {value}" for index, value in enumerate(lenguajes, 1)])

print({indice : lenguaje for indice, lenguaje in enumerate(lenguajes)})
# los enumero para verificar en que indice de la lista estan


### FUNCION all(iterable)
# valida si todos los elementos de la coleccion son verdades, devulve falso si alguno de los elementos es falso
# todos deben ser verdaders
## FUNCION any(iterable)
# valida si almenos hay un true en una coleccion de elementos
print(all([True, False,True]))
print(any[False, False, False])

print(all([])) #el all de una lista vacia me da true
print(any([])) # e lany de una lista vacia me da false,
      
# EJERCICIO
# Ejercicio
# La empresa ABCD tiene hasta 100 empleados.  
# La compañía decide crear un número de identificación único UID para cada uno de sus empleados.  
# La compañía le ha asignado la tarea de validar los UIDs generados aleatoriamente.  
# Un UID válido debe cumplir con las siguientes reglas:
# * Debe contener por lo menos dos letras mayúsculas en el alfabeto inglés.
# * Debe tener por lo menos 3 dígitos.
# * Contener únicamente dígitos alfanuméricos.
# * No tener repeticiones.
# * Contener exactamente 10 caracteres.


