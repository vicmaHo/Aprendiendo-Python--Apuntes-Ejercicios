"""
l ingresar a cierto banco le solicitan los siguientes datos a cada cliente: nombre, edad (años) y
duración estimada (minutos) de la diligencia a realizar. Se debe calcular el valor de la prioridad de
atención para cada cliente (Prioridad=edad/tiempo) e identificar la categoría que tiene el cliente según
el valor calculado. Hay tres categorías que se pueden identificar y se calculan utilizando la siguiente
tabla:
X =Edad/tiempo
X<2
2 <= x <5
X5
Prioridad:
Baja
Normal
Alta
Desarrollar un programa que defina una función donde se calculen los valores de salida para un
paciente. Utilizar la función para los tres pacientes que se muestran en la siguiente tabla:

"""
def prioridad(nombre: str, edad: int, tiempo: int) -> str:
    prioridad = edad / tiempo
    if prioridad < 2:
        prioMsj = "Baja"
    elif prioridad <= 2 and prioridad < 5:
        prioMsj = "Normal"
    else:
        prioMsj = "Alta"
    return f"NOMBRE: {nombre}\nEdad/Tiempo: {prioridad}\nPrioridad: {prioMsj}"

# Entradas
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
tiempo = int(input("Ingrese el tiempo: "))

# Salida
print(prioridad(nombre, edad, tiempo))
    