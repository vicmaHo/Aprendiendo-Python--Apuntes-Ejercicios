# Diseñe un algoritmo que permita solicitar tanto el nombre como la edad de una persona 
# y posteriormente indicar si es “Mayor de edad” o “Menor de edad” según la información ingresada. 
# Una persona se considera mayor de edad si tiene 18 años o más.

def mayorEdad(edad: int)->str:
    # validacion de datos
    if edad <= 0:
        return f"La edad no puede ser negativa o cero"
    if edad < 18:
        return f"La persona es menor de edad"
    else:
        return f"La persona es mayor de edad"

edad = int(input("Ingrese su edad: "))

print(mayorEdad(edad))