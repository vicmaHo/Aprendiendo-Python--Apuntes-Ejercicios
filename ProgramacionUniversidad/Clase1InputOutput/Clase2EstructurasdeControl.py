# estructuras de control, clase 2

"""programa para indicar si una personaa es mayor de edad  o no
Nota: este programa utiliza la secuencia, instrucciones de entrada 
y salida y estructuras de control(if else)
"""

# entrada 
edad = int(input("Ingrese su edad: "))

# proceso, si es mayor o igual que 18, es mayor de edad, si no, no es mayor de edad
"""Si, sino. sino-si"""

if edad >= 18:
    mensaje = ("Usted es MAYOR de edad")
else:
    mensaje = ("Usted es MENOR de edad") # podemos almacenar el mensaje dentro de una variable

# salida (separando el proceso de la salida en una variable llamada mensaje)

print(mensaje)