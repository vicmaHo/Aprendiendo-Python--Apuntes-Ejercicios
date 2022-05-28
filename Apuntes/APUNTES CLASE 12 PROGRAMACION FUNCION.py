## APUNTES CLASE 12 PROGRAMACION FUNCIONAL EN PYTHON
## Recordatorio de lo visto anteriormente en funciones

# definicion de funciones
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