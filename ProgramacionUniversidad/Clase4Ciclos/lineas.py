
"""
hacer un programa que imprima el numero delineas solicitado por el usuasrio de la siguiente figura
*
**
***
****
*****
******
el anterior ejemplo para 6 lineas
"""

n = int(input("Ingrese el numero de lineas: "))

# for para las lineas

def imprimirLineas(n):
    for linea in range(1, n + 1):
        contenido = ''
        for i in range(0, linea):
            contenido += '*'
        print(contenido)

imprimirLineas(n)


# forma mas sencilla

def imprimirFacil(n):
    for j in range(1, n+1):
        print(f"{'*' * j}")

imprimirFacil(n)