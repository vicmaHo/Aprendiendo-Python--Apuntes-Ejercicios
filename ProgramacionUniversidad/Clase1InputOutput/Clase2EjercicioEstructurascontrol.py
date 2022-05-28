"""
se requiere un progrma que lea dos numeros enteros y la opcoin de la operacon a realizar
1- suma, 2- resta, 3 - multiplicacion, 4- division segun la opcion elegida se deber mostrar
el resultado.
Nota: este programa usa la secuencia, la entrada/salida y las estructuras de control 
Autor:
Fecha:

"""

# entrada 

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
operacion = int(input("""Que operacion desea? 
(1- suma, 
2- resta, 
3- multiplicacion, 
4- division):\n\n """))

# proceso

if operacion == 1:
    resultado = numero1 + numero2
elif operacion == 2:
    resultado = numero1 - numero2
elif operacion == 3:
    resultado = numero1 * numero2
elif operacion == 4:
    resultado = numero1 / numero2
else:
    print("No ingreso una operacion correcta")


#salida

if operacion >= 1 and operacion <= 4: # esta condicion se va para que no salte error al no generar algun resultado
    print(f"El resultado de su operacion es: {resultado}")
