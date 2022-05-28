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