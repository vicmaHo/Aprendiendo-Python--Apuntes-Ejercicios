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