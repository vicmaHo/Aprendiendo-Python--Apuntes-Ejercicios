# Se está realizando una encuesta sobre el medio de transporte que prefieren las personas en la ciudad de Cali. 
# A cada persona se le pregunta el sexo y el medio de transporte. Usted debe desarrollar un programa que permita
# registrar los datos de la encuesta. Para ingresar los datos de cada persona se utilizan los siguientes códigos:

# Sexo:
# Femenino: 1
# Masculino: 2

# Transporte
# MIO: 1
# Vehiculo Particular: 2
# Bicicleta: 3

# Tenga en cuenta que el programa debe permitir registrar la información de N personas, donde N es un número entero 
# digitado por el usuario. Una vez se termine de ingresar los datos, debe aparecer la siguiente información 
# estadística:

# La cantidad de mujeres que prefieren como medio de transporte el MIO
# El porcentaje de hombres que se transportan en bicicleta


n = int(input())

def encuesta_transporte(n):
    acc_hombres_bicicleta = 0
    acc_mujeres_mio = 0
    acc_total_hombres = 0
    for i in range(n):
        genero = int(input())
        transporte = int(input())
        if genero == 1 and transporte == 1:
            acc_mujeres_mio += 1
        if genero == 2:
            acc_total_hombres += 1
            if transporte == 3:
                acc_hombres_bicicleta += 1
    porcentaje_hombres_bicicleta = (acc_hombres_bicicleta / acc_total_hombres) * 100
    return f"Cantidad de mujeres en el MIO: {acc_mujeres_mio} y porcentaje de hombres en bicicleta {porcentaje_hombres_bicicleta}%"


print(encuesta_transporte(n))