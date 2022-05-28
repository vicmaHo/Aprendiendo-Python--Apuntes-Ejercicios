#funcion para determinar el IMC
def determinarIMC(peso, estatura):
    imc = peso / (estatura * estatura)
    return imc

#funcion para determinar el estado de obesidad
def determinarObesidad(imc):
    if imc < 18.5:
        estado = "Bajo peso"
    elif imc >= 18.5 and imc <= 29.9:
        estado = "Peso normal"
    elif imc >= 25.0 and imc <= 29.9:
        estado = "Sobrepeso"
    else: # >=30
        estado = "Obesidad tipo 1"
    return estado

#programa principal

#entradas
print("Ingrese sus datos\n")
nombre = input("Nombre....: ")
peso = float(input("Peso......: "))
estatura = float(input("Estatura..: "))

print("=====================================================")

#proceso
imc = determinarIMC(peso, estatura)
estado = determinarObesidad(imc)

#salidas
print(f"""Nombre.........:   {nombre}
Peso...........:   {peso}
Estatura.......:   {estatura}
IMC............:   {imc}
Estado obesidad:   {estado}""")


