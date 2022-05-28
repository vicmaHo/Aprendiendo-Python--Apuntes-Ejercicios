# funciones ejemplo 3 pdf de la clase 
"""
se recomienda no capturar datos en las funciones, dejar esto solo para el programa principal
"""
################## definicon de funciones

def calculaPinos(m2):
    if m2 > 1000000:
        numPinos = ((m2*0.7)/10)*8
    else:
        numPinos = ((m2*0.5)/10)*8
    return numPinos


def calculaOyameles(m2):
    if m2 > 1000000:
        numOyameles = ((m2*0.2)/15)*15
    else:
        numOyameles = ((m2*0.3)/15)*15
    return numOyameles

def calculaCedros(m2):
    if m2 > 1000000:
        numCedros = ((m2*0.1)/18)*10
    else:
        numCedros = ((m2*0.2)/18)*10
    return numCedros



# entrada --- cantidad de hectareas
numHectareas = int(input("Digite el numero de hectareas: "))

#proceso calcular numero de 
metrosCuadrados = numHectareas * 10000

numPinos = calculaPinos(metrosCuadrados)
numeroOyameles = calculaOyameles(metrosCuadrados)
numeroCedros = calculaCedros(metrosCuadrados)


# salida --- cantidad de pinos, oyameles y cedros 

print(f"Pinos: {numPinos}, Oyameles: {numeroOyameles}, Cedros: {round(numeroCedros, 0)}")