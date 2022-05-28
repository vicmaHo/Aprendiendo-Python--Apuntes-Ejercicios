"""
Una casa de cambio vende 3 tipos de divisas diferentes
(dólares $3080, euros $3469, libras $4748). La empresa
necesita desarrollar un programa que dé 2 opciones a los
clientes: 1. Consulta de precios de cada divisa, y 2. el valor
de la conversión del peso colombiano a la divisa
"""


#Programa para cambio de divisas

def conversor(divisa, valor):
    if divisa == 1:
        resultado = valor / 3080
    elif divisa == 2:
        resultado = valor / 3469
    else:
        resultado = valor / 4748
    return resultado

def mostrarDivisas():
    print("""El valor de las divisas es:
    dolar:  3080
    euro:   3469
    libra:  4768""")

# entrada
print(
"""Bienvenido. Opciones:
1) Consultar precios de divisas 
2) COnvertir pesos colombianos 
""")
opcion = int(input("Ingrese la opcion: "))

# proceso


if opcion == 1:
    mostrarDivisas()
elif opcion == 2:
    print("""Ingrese la divisa a convertir y el valor de la conversion""")
    divisa = int(input("Que divisa? 1-2-3: "))
    valor = int(input("Valor a convertir: "))
    resultado = conversor(divisa, valor)
else:
    print("La opcion ingresada no existe.")

# salida
if opcion == 2:
    print (f"El valor de la conversion es de: {resultado}")