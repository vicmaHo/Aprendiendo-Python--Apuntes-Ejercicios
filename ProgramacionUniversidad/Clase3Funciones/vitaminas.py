"""
Usando funciones, desarrollar un programa que dado el peso,
la altura y el sexo de un estudiante. Determine la cantidad de
vitaminas que debe consumir, con base en los siguientes
criterios:
Si es hombre, y su estatura es mayor a 1.60, y su peso es mayor
o igual a 75 kilos, su dosis, será: 20% de la estatura y 80% de
su peso, 
si la estatura es menor o igual a 1.60, la dosis será la
siguiente: 30% de la estatura y 70% de su peso.

Si es mujer, y su estatura es mayor o igual a 1.55 y su peso es
mayor o igual a 65 kilos, su dosis será: 25% de la estatura y
75% de su peso. 

Si el peso es menor a 65 kilos, será: 35% de la
estatura y 65% de su peso
"""


#------ funciones
def calculaMujeres(peso, altura):
    if altura >= 1.55 and peso >= 65:
        dosis = (altura * 0.25) + (peso * 0.75)
    elif peso < 65:
        dosis = (altura * 0.35) + (peso * 0.65)
    else:
        dosis = 0
    return dosis

def calculaHombres(peso, altura):
    if altura >= 1.60 and peso >= 75:
        dosis = (altura * 0.2) + (peso * 0.8)
    elif altura <= 1.60:
        dosis = (altura * 0.3) + (peso * 0.7)
    else:
        dosis = 0
    return dosis


#------ programa principal
# entrada de datos

sexo = input("Ingrese el sexo. H o M: ")
peso = float(input("Ingrese el peso: "))
altura = float(input("Ingrese la altura: "))

# proceso

if sexo == 'H':
    vitaminas = calculaHombres(peso, altura)
else:
    vitaminas = calculaMujeres(peso, altura)


# salida de resultados

print(f"La cantidad de vitaminas es: {vitaminas}")