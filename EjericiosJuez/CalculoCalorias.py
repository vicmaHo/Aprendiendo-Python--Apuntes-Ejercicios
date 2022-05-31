# Desarrollar un programa que permita calcular la cantidad mínima de calorías (CMC) quemadas por
# una persona en un día. Debe utilizar la ecuación de Harris-Benedict, según la cual la cantidad 
# de calorías depende del género, la estatura, el peso y la edad. Para los hombres se utiliza la ecuación
# CMC = (13.75 × peso) + (5 × estatura) - (6.76 × edad) + 66, y para las mujeres se tiene que CMC = (9.56 × peso) + (1.85 × estatura) - (4.68 × edad) + 655.
# En ambos casos el peso debe estar en kilogramos y la estatura en centímetros.
# El programa a desarrollar debe inicialmente solicitar el género, el peso, la estatura, y la edad.
# Luego se calcula el CMC utilizando las ecuaciones según sea el caso. Finalmente, se muestra el valor calculado.

genero = input()
peso = float(input())
estatura = int(input())
edad = float(input())

def calcular_calorias(genero,peso,estatura,edad):
    if genero == "Masculino":
        cmc = (13.75 * peso) + (5 * estatura) - (6.76 * edad) + 66
    elif genero == "Femenino":
        cmc = (9.56 * peso) + (1.85 * estatura) - (4.68 * edad) + 655
    return cmc

print(calcular_calorias(genero,peso,estatura,edad))