# separar la cadena en 2 partes por el caracter "." donde cada parte debe estar con mayuscula inicial

cadena = "esto es una Cadena muy larga. y esto?"
pos_punto = cadena.find(".")
parte_1 = cadena[:pos_punto].capitalize()
parte_2 = cadena[pos_punto + 1:].strip().capitalize()
print(parte_1)
print(parte_2)

# iterar una cadena con salto
mensaje = "Hola, como estas tu?"
print(mensaje[::3]) # cojo toda la cadena pero dando satlos de 3 en 3

# invertir la cadena
cadena = "esto es una Cadena muy larga. y esto?"
print(cadena[::-1])  # hago saltos de -1 es decir que voy desde la derecha hasta la izquierda  



