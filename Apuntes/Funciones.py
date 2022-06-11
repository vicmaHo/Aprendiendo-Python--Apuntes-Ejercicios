
### Funciones ###

# Las funciones en python nos permiten crear nuevas "palabras reservadas", sabemos que por ejemplo print() o input() son funciones
# es decir que realizan ciertas acciones de acuerdo a ciertos parametros,  cuando creamos funciones podemos hacer que estas
# realicen ciertas acciones que pueden ser repetitivas y que pueden verse reducidas a una funcion que posteriormente puede
# llamarse varias veces

# Las funciones son asi 
def NOMBRE(ListaDeParametros):
    """Documentacion de la funcion (explicacion)"""
    # Instrucciones
    return # retorna un valor despues del proceso

# las funciones pueden no tener parametros () y pueden no retornar nada en fin mi es 
# En la lista de parametros incluimos los valores que vamos a enviar

# def recibirtNombreCompleto (numero): # podriamos enviar una cadena, o podriamos enviar un numero convertirlo a str y sumarlo a 
#     nombre = input(f"Ingrese el nombre de la persona {numero}: ")
#     apellido = input(f"Ingrese el apellido de la persona {numero}: ")
#     return nombre + " " + apellido
# print(recibirtNombreCompleto(1)," ", recibirtNombreCompleto(2), " y a", recibirtNombreCompleto(3))
# Dentro de las funciones debemos usar los parametros ingresados 
# A las funciones les puedo suministrar cualquier tipo de dato (str, int, float, tuple, set, dict) pero tenemos que tener en cuenta 
# Ingresar el NUMERO correcto de parametros a enviar dependiendo de los que la funcion necesite

# Funcion completa
def nombreCompleto(nombre = "3", apellido = "Abad"): # = abad, con esto hacemos que el parametro apellido tenga un valor por defecto y no suceda ningun problema si llegara a faltar
    # en pocas palabras decimos que el parametro es opcional
    """Generaicion del nombre completo de la persona
    Parametros:
        nombre: Identifica a la persona
        apellido: Representa la familia del padre y la madre 
    Retorna:
        La union de los dos parametros ingresados"""
    
    completo = nombre + " "  + apellido
    return completo
print("Generar el nombre completo de una persona...")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nombreEntero = nombreCompleto()

print(nombreEntero)


# si queremos enviar los parametros en desorden, asigando el orden que queramos al parametro y asigando su valor 
print(nombreCompleto(apellido=nombre, nombre=apellido))

# Para saber la documentacion de la funcion podemos usar un parametro

print(nombreCompleto.__doc__)


# Fuciones del sistema (Funciones con las que cuenta el python) forman parte del nucleo de pyhton

# abs() ---> Valor absoluto, el parametro que le mandemos nos lo devolcera como un valor absotulo (un valor que no importa en que plano se ubica si no cuanto se dezplasa)
# solo positivos

# min() ---> Minimo, devuelve el minimo de sus parametros,, si se leañaden letras tambien las evalua

# max() ----> Maximo, devuelve el maximo de sus parametros

# round() ---> Redondear, se le ingresan dos parametros, el numero a redondear y la cantidad de decimales que necesitamos
# si le añadimos un redondea a un valor negativo, lo evalua de derecha a izquierda convirtiendo todos estos en cero y evaluando
# si este numero se acerca mas a otro o se que da ahi mismo REDONDEO NEGATIVO    cuando pagamos en promociones 9,999 pagas
# a 10.000

#sum() ---> suma todos los parametros que se le agreguen, se le pueen enviar listas


# TABLA ASSCII ---> forma de mapeo entre un valor y un caracter (imprimible o no) de esta forma el computador
# puede entender o representar los simbolos
# cuando presionas una tecla el computador recibe un numero y dependiendo de ello el computador hara algo,  de esta
# forma los lenguajes de programacion pueden trabajar sobre caracteres o cadenas de texto

# chr() --> recibe un numero y duvelve su simbolo de assci
# ord() ---> recibe un caracter y devulve su codigo asci

# type() ---> devuelve el tipo de valor de un objeto 

#len() --> devuelve la longituf de una secuencia o cadena

# dir() --> muestra por pantalla todos los atributosm datos y metodos ytilizables con un obheto

# help(type) ---> imprime la documentacion de ese comando


# funciones de la libreria math

# math.ceil() --> devuelve el entero mas grande mayor o igual ax

# math.floor() -->devuelve el entero mas grande menor o igual que x

# estas dos anteriores devuelven el valor en un int dependiendo del caso un int u otro

# trunc() devuelve x con la parte decimal eliminada el valor seredondea hacia cero

# pow (x, y) elevo x a la y

# sqrt() raiz cuadrada


# IMPORTAR BIBLIOTECAS
# importar toda la biblioteca

# import nombrebibliote

#importar con un alias 
# import nombrebiblioteca as nombreAlias
import turtle as t

# importar funciones especificas de la biblioteca
# from biblioteca import funcionDeLaBiblioteca, otrafuncion, otrafuncion
from random import random, randrange, randint, choice


# crear biblioteca, generas un archivo py con las funcioens que necesites, posteriormente en otro archivo 
# importas la biblioteca, import nombreDel Archivo


# en las funciones se recibel parametros, y estas no imprimen, retornan un valor

def funcioncondocuemntacion(hola: str, numero: float) -> int:
    """Documentacion de la funcion
    Parametros:
        hola(int): una cadena
        numero(float): almacena un numero real
    Retorna: 
        Int: que es un simple y llano y increible 0"""
    return 0

funcioncondocuemntacion()


## OPERACIONES LOGICAS ##
# Negacion --- > not
# Conjuncion ---> and
# Disyuncion ---> or
