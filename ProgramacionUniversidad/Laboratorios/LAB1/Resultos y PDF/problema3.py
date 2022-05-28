"""
PROBLEMA 3

Integrantes: 
-Victor Manuel Hernandez Ortiz  - 2259520
-Juan Pablo Castaño Arango      - 22559487
-Juan Pablo Escobar Viveros     - 2259519

Profesor: Andres Fernando Velasco
Grupo: 50
Laboratorio: 1

"""
#Entrada
print("""Bienvenido.
En este programa, se le dara el volumen y el area de su cilindro""")

altura = float(input("Digite el valor de la altura que tendra su cilindro: "))
radio = float(input("Digite el valor que va a tener el radio su cilindro: "))

#Proceso
volumen = ((3.14159 * (radio ** 2)) * altura)
area = ((2 * 3.14159) * radio * altura) + ((2 * 3.14159) * (radio ** 2))

#Salida
print("El resultado del Volumen de su cilindro es:", volumen)
print("El resultado de la Area de su Cilindro es:", area)

