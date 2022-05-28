"""
se trata de elaborar un programa que le muestre al usuario una adivinanza. la idea es utilizar 
funciones de la libreria string


"""

import string as st
respuesta = '      mango      '
segunda = 'amarilla por dentro'
primera = 'Verde por fuera'
tercera = 'y con pepa de '+ respuesta.strip() + ' en el centro.'
ultima = 'Que es?'

adivinanza = primera + ', ' + segunda + ' ' + tercera + ' ' + ultima

print(adivinanza)

intento = input("\n...")

if intento.upper().count(respuesta.strip().upper()) > 0:
    print("Hurra, has adivindo")
else:
    print("Lo siento, intenta de nuevo")