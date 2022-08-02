# Ejercicio Encuesta
# Realizar un programa que piede ciertos datos a un cantidad de personas desconocida
# posteriormente el programa debe realizar ciertos calculos e imprimirlos


personas = 0
personas_lectura = 0
personas_tv = 0
personas_depor = 0
personas_dormir = 0
leer_6_9_horas = 0 
prefiere_ver_television_9_horas = 0
print(
"""Codigo \t\tTiempo libre\n
1 \t\tMenos de 6 horas
2 \t\tEntre 6 y 9 horas
3 \t\tMás de 9 horas""")
tiempo_libre = int(input("Digite el codigo de tiempo libre: "))
while tiempo_libre != -1: 
    print("""\nCodigo \t\tActividad principal\n\n1 \t\tLeer\n2 \t\tVer televisión\n3 \t\tHacer deporte\n4 \t\tDormir""")
    actividad_principal = int(input("Digite la actividad principal: "))
    
    personas += 1 
    if actividad_principal == 1:
        personas_lectura += 1
    elif actividad_principal == 2:
        personas_tv += 1
    elif actividad_principal == 3:
        personas_depor += 1
    else:
        personas_dormir += 1
        
    
    if tiempo_libre == 2 and actividad_principal == 1:
        leer_6_9_horas += 1
    print("Registrado !!\n\n")
    print("""Codigo \t\tTiempo libre\n\n1 \t\tMenos de 6 horas\n2 \t\tEntre 6 y 9 horas\n3 \t\tMás de 9 horas""")

    tiempo_libre = int(input("Digite el codigo de tiempo libre [-1 --> para finalizar]: "))
    
    
    if actividad_principal == 2 and tiempo_libre == 3:
        prefiere_ver_television_9_horas += 1
    
porcentaje_lectura = round((personas_lectura * 100) / personas, 2)
porcentaje_tv = round((personas_tv * 100) / personas, 2)
porcentaje_depor = round((personas_depor * 100) / personas, 2)
porcentaje_dormir = round((personas_dormir * 100) / personas, 2)

porcentaje_prefieren_leer_6_9_horas = round((leer_6_9_horas * 100) / personas_lectura, 2)

# salida
print(
f"""
Porcentaje de los que Leen: {porcentaje_lectura}%
Porcentaje de los que ven television: {porcentaje_tv}%
Porcentaje de los que hacen deporte: {porcentaje_depor}%
Porcentaje de los que duermen: {porcentaje_dormir}%
""")

print(f"Porcentaje de personas que prefieren leer de 6 a 9 horas, con respecto a los que prefieren leer: {porcentaje_prefieren_leer_6_9_horas}%")
print(f"Cantidad de personas que prefieren ver televisiony tienen mas de 9 horas disponibles; {prefiere_ver_television_9_horas}")
