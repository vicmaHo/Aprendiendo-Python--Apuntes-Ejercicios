# Suponga que el calculo de la pensión de una persona se realiza
# de la siguiente manera: por cada año de servicio se paga $80 si
# el empleado ingresó en o después de 1995 y $100 si ingresó
# antes, dicho valor (80 o 100) se multiplica por el número de cada
# año más la edad que tenía en el año (ej.
# (100*1994+32)+(100*1995+33)+…), el descuento de seguridad
# social en salud es del 12%. El programa debe recibir el año de
# ingreso y la edad del empleado en el año de ingreso, devolver el
# sueldo o mesada bruta, la mesada neta y el valor del descuento
# por salud.
# Ejemplo: Para una persona que ingresó en el 2009 y que tenía 44
# años en dicho año, su mesada o sueldo bruto para el 2011 es
# $482.535, el descuento por salud es $57.904 y por lo tanto su
# sueldo o mesada neta es $424.630.

def calculoSueldoBruto(edad, anio, anioRetiro):
    sueldoBruto = 0
    edadAcumulado = edad
    if anio >= 1995:
        for i in range(anio, anioRetiro+1, 1):
            sueldoBruto += 80 * i + edadAcumulado
            edadAcumulado+=1
    else:
        for i in range(anio, anioRetiro+1, 1):
            sueldoBruto = 100 * i + edadAcumulado
            edadAcumulado += 1
    return sueldoBruto


anio = int(input("Ingrese el año en el que comenzo a trabajar: "))
edad = int(input("Ingrese la edad en ese año: "))
anioRetiro = int(input("Ingrese el año en el que se retira: "))
sueldoBruto = calculoSueldoBruto(edad, anio, anioRetiro)

descuentoSalud = sueldoBruto * 0.12

sueldoNeto = sueldoBruto - descuentoSalud

print(f"el suelo bruto es de: {sueldoBruto}\nEl descuento de salud es de: {descuentoSalud}\nSu sueldo neto es de: {sueldoNeto}")

        