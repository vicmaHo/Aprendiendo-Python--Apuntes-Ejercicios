cantidad = 0
cantidad_leer = 0
cantidad_tv = 0
cantidad_depor = 0
cantidad_dormir = 0
leer_6_9_horas = 0 
prefiere_ver_television_9_horas = 0
while True:
    print("""Codigo \t\tTiempo libre\n\n1 \t\tMenos de 6 horas\n2 \t\tEntre 6 y 9 horas\n3 \t\tMás de 9 horas""")

    tiempo_libre = int(input("Digite el codigo de tiempo libre [-1 --> para finalizar]: "))
    if tiempo_libre == -1:
        break 
    
    print("""\nCodigo \t\tActividad principal\n\n1 \t\tLeer\n2 \t\tVer televisión\n3 \t\tHacer deporte\n4 \t\tDormir""")
    actividad_principal = int(input("Digite la actividad principal: "))

    
    cantidad += 1 
    if actividad_principal == 1:
        cantidad_leer += 1
    elif actividad_principal == 2:
        cantidad_tv += 1
    elif actividad_principal == 3:
        cantidad_depor += 1
    else:
        cantidad_dormir += 1
        
    
    if tiempo_libre == 2 and actividad_principal == 1:
        leer_6_9_horas += 1

    if actividad_principal == 2 and tiempo_libre == 3:
        prefiere_ver_television_9_horas += 1
    
porcentaje_lectura = round((cantidad_leer * 100) / cantidad, 2)
porcentaje_tv = round((cantidad_tv * 100) / cantidad, 2)
porcentaje_depor = round((cantidad_depor * 100) / cantidad, 2)
porcentaje_dormir = round((cantidad_dormir * 100) / cantidad, 2)

porcentaje_prefieren_leer_6_9_horas = round((leer_6_9_horas * 100) / cantidad_leer, 2)

# salida
print(
f"""
Porcentaje de los que Leen: {porcentaje_lectura}%
Porcentaje de los que ven television: {porcentaje_tv}%
Porcentaje de los que hacen deporte: {porcentaje_depor}%
Porcentaje de los que duermen: {porcentaje_dormir}%
""")

print(f"Porcentaje de cantidad que prefieren leer de 6 a 9 horas, con respecto a los que prefieren leer: {porcentaje_prefieren_leer_6_9_horas}%")
print(f"Cantidad de cantidad que prefieren ver televisiony tienen mas de 9 horas disponibles; {prefiere_ver_television_9_horas}")