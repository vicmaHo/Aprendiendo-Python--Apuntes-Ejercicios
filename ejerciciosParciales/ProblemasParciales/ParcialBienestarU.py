"""
Bienestar está adelantando una consulta con los
estudiantes para definir la oferta de espacios deportivos para el próximo semestre. A cada estudiante se le
pregunta por la cantidad de horas que espera dedicar a actividades deportivas y el deporte que más le gusta.
Usted debe desarrollar un programa que permita registrar los datos de la encuesta. Para ingresar los datos
de cada estudiante se utilizan los siguientes códigos:
Deporte			CÓDIGO

Fútbol			1
Baloncesto		2
Voleibol		3
Atletismo		4


Tenga en cuenta que el programa debe permitir registrar la información de N personas, donde N es un
número entero digitado por el usuario. Una vez se termine de ingresar la información, debe aparecer la
siguiente información estadística:

Distribución porcentual según el deporte escogido como favorito.
El promedio de edad de los que gustan más de Fútbol y Atletismo
La cantidad de personas que prefiere Voleibol y que piensan dedicar más de 6 horas.
"""

## Declaracion - iniciacion de variables
cantidadFutbol = 0
cantidadBaloncesto = 0
cantidadVoleibol = 0
cantidadAtletismo = 0
personasVoleibol = 0
acumulaEdad = 0
numeroPersonas = 0
while True:
        
    print("""Deportes:
    Codigo - Deporte
    1 - Futbol
    2 - Baloncesto
    3 - Voleibol
    4 - Atletismo""")
    # entradas
    deporteFavorito = int(input("Ingrese su deporte favorito(codigo): "))
    if deporteFavorito == -1:
        numeroPersonas = 1
        break
    horasActividad = int(input("Ingrese la cantidad de horas que planea dedicar a actvidad deportiva: "))
    edad = int(input("Ingrese su edad: "))

    ## Proceso ##
    numeroPersonas += 1
    if deporteFavorito == 1:
        cantidadFutbol += 1
    elif deporteFavorito == 2:
        cantidadBaloncesto += 1
    elif deporteFavorito == 3:
        cantidadVoleibol += 1
    elif deporteFavorito == 4:
        cantidadAtletismo += 1



    # para calcular promedio de los que gustan de futbol y altetismo
    if deporteFavorito == 1 or deporteFavorito == 4:
        acumulaEdad += edad


    # para calcular los que prefieren voleibol
    if deporteFavorito == 3 and horasActividad > 6:
        personasVoleibol += 1
    
# calculamos el proemdio de los que gustan de futbol y atletismo
promedioEdad = acumulaEdad / numeroPersonas



## salidas ##

print(f"De {numeroPersonas} a {cantidadFutbol} les gusta el futbol\nA {cantidadBaloncesto} les gusta el baloncesto\nA {cantidadVoleibol} Les gusta\
    el voleibol\nA {cantidadAtletismo} les gusta el atletismo")
print("El promedio de edad de los que gustan de futbol y atletismo:", promedioEdad)
print("Las personas que prefieren el voleibol y que piensan dedicar mas de 6 horas:", personasVoleibol)
