"""
Descripcion del ejercicio

"""

# entrada

cedula = int(input("ingrese la cedula: "))
anio = int(input("Ingrese el año: "))
salarioBasico = float(input("Ingrese el salario basico: "))

# proceso
if salarioBasico > 1200000 and anio > 1990:
    salarioNeto = salarioBasico - (salarioBasico * 0.08)     # podemos factorizar, salario basico factor comun de 1 - 0.08 = 0.92, es decir que si le descuento el 8 porciento me quedara el 92 porciento
elif salarioBasico < 550000 or anio == 1990:
    salarioNeto = salarioBasico - (salarioBasico * 0.02)
else:
    salarioNeto = salarioBasico - (salarioBasico * 0.05)

print(f"Cedula: {cedula}, salario neto: {salarioNeto}")


"""Chequear todas las rutas con al menos una prueba, asegurandose de relaizar la prueba de escritorio"""