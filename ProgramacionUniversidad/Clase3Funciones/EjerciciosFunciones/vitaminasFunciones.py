'''
Usando funciones, desarrollar un programa que dado el peso,
la altura y el sexo de un estudiante. Determine la cantidad de
vitaminas que debe consumir, con base en los siguientes
criterios:
Si es hombre, y su estatura es mayor a 1.60, y su peso es mayor
o igual a 75 kilos, su dosis, será: 20% de la estatura y 80% de
su peso, si la estatura es menor o igual a 1.60, la dosis será la
siguiente: 30% de la estatura y 70% de su peso.
Si es mujer, y su estatura es mayor o igual a 1.55 y su peso es
mayor o igual a 65 kilos, su dosis será: 25% de la estatura y
75% de su peso. Si el peso es menor a 65 kilos, será: 35% de la
estatura y 65% de su peso
'''

#---funciones
def calculaVitaminas(sexo, peso, altura):
    if sexo == 'H':
        if altura > 1.60 and peso >= 75:
            dosis = (0.2 * altura) + (0.8 * peso)
        elif altura <= 1.60:
            dosis = (0.3 * altura) + (0.7 * peso)
        else:
            dosis = 0
    elif sexo == 'M':
        if altura >= 1.55 and peso >= 65:
            dosis = (0.25 * altura) + (0.75 * peso)
        elif peso < 65:
            dosis = (0.35 * altura) + (0.65 * peso)
        else:
            dosis = 0
    else:
        return "Error"
    return dosis
#---principal

#entrada
sexo = input("Ingrese el sexo de la persona: ")
altura = float(input("Ingrese la estatura de la persona: "))
peso = float(input("Ingrese el peso de la persona: "))

#proceso
vitaminas = calculaVitaminas(sexo, peso, altura)

#salida
if vitaminas == "Error":
    print("El sexo esperado es H - M")
else:
    print("La cantidad de vitaminas es de:", vitaminas)