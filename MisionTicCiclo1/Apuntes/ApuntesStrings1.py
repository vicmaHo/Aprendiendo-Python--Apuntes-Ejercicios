# STRINGS
# CARACTERES ESPECIALES


print("Hola \"Victor\"")
# el \ sirver para hacer un escape de un caracter especial que le siga
print("una linea\nDos lineas")
# \n sirve para realizar saltos de linea
print("Tabulo\t1")
# con \t hago una tabulacion de 8 espacios
print("")
# \U unicode para agregar simbolos de unicode

# las cadenas en python se interpreta ncomo conjutnos de caracteres, es decir que podemos acceder
# a cada caracter mediante un indice
cadena = "Hola Mundo"
print(cadena[0])

# con la funcion len() podemos saber la longitud de una cadena
print(len(cadena))

# cuando tenemos un indice negativo vamos a analizar el conjunto de datos desde el lado derecho
print(cadena[-1])

# SUBCADENA ---> eextraer un pedazo/rango/bloque/parte de una cadena comṕleta
# le damos el indice en una forma de rango
cadena = "esta es una cadena demasiado larga"
print(cadena[0:10]) #[0,10] i>=0 and i < 10     es decir que incluye la primera posicion pero no la segunda
# esto es un

print("'" + cadena[1:5] + "'")      # 'sto '



# en estas porcioens podemos usar [:] para imprimir toda la cadena, [n:] imprimir desde un indice hasta que termine la cadena
# [:n] imprimir desde el inicio hasta un indice

# operadores en cadenas ----> suma para concatenar
# multiplicacion para repetire la cadena varias veces
# modulo para hacer formateo de cadenas (el menos comun pero puede llegar a ser util)


# FUNCIONES PARA CADENAS
cadena = "esto es una cadena muy larga. y esto?"
# caden.capitalize() --> sirver para capitalizr una cadena, es decir, pone mayuscula inicial
print(cadena.capitalize())

#cadena.upper() todo a mayusculas
#cadena.lower() todo a minuscula

# cadena.split()  me devuelve una lista con cada una de las palabras que estaban separadas por un espacio
print(cadena.split()) # ["esto", "es", "una",....]   dentro del split() podemos decir cual es el caracter que usamos de separador
print(cadena.split(".")) ["esto es una cadena muy larga", " y esto?"]


# cadena.strip() quita los espacios al principio y al final y los borra, ajustando el texto
# le puedo mandar un parametro para que borre un caracter que queramos de los lados
# podemos añadir otro strip () para quitar lo que queramos


# buscar en cademas
# cadena.find("caractar", despues de x posicion) devuelve la posicion de un caracter, si le agregamos el segundo parametro
# buscara

