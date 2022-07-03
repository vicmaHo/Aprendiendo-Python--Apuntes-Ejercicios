"""
Se va a llevar a cabo una primera fase del censo nacional de manera virtual. Para ello, los
ciudadanos deben registrar sus datos personales y algunos datos de las personas que
conforman su hogar en una plataforma diseñada con este fin. La persona que ingresa a la
plataforma será el (la) jefe de hogar y debe proporcionar los siguientes nueve datos:•

Nombre
Apellido
Tipo de documento de identidad
Número de documento de identidad
Fecha de nacimiento
Departamento de nacimiento
Ciudad de nacimiento
Dirección de residencia
Cantidad de familiares a registrar
Posteriormente, para cada miembro del hogar se deben registrar los siguientes seis datos:

Nombre
Apellido
Tipo de documento de identidad
Número de documento de identidad
Fecha de nacimiento
Parentesco
Al finalizar el registro de un hogar, se debe mostrar una confirmación con todos los datos
proporcionados por el usuario. Al finalizar todos los hogares (no se sabe cuántos) se debe
presentar el promedio de personas que conforman cada hogar. Desarrolle u
"""
cantidadTotalPersonas = 0
evento = "si"
hogares = 0
while evento == "si": 
    jefeHogar = {
        "nombre": None, 
        "apellido": None, 
        "tipo de documento": None, 
        "numero de documento": None,
        "fecha de nacimiento": None, 
        "departamento de nacimiento": None, 
        "ciudad de nacimiento": None,
        "direccion de residencia": None, 
        "cantidad de familiares que desea registrar": None
        }
    # ingreso de datos jefe hogar
    print("="*10 + "INGRESO DE DATOS DEL JEFE DEL HOGAR" + "="* 10)
    for key in jefeHogar.keys():
        jefeHogar[key] = input("ingrese su %s: " %(key))
        if key == "cantidad de familiares que desea registrar":
            cantidadFamiliares = int(jefeHogar[key])
            
    # declaracion de las listas para almacenar los datos
    nombre = []
    apellido = []
    tipoDocumento = []
    numDocuemnto = []
    fechaNac = []
    parentesco = []

    # ingreso de los datos por familiar
    for i in range(cantidadFamiliares):
        print("="*6+"Ingreso de datos del familiar "+ str(i+1)+"="*6)
        nombre.append(input("Ingrese su nombre: "))    
        apellido.append(input("Ingrese su apellido: "))
        tipoDocumento.append(input("Ingrese su tipo de documento: "))
        numDocuemnto.append(input("Ingrese su numero de documento: "))
        fechaNac.append(input("Ingrese su fecha de nacimiento: "))
        parentesco.append(input("Ingrese su parentesco: "))
    print()
    print("="*15+"JEFE DEL HOGAR"+"="*15)
    for key, value in jefeHogar.items():
        print(key.upper() + " : " + value.upper())
    print()
    for i in range(cantidadFamiliares):
        print(f"===============FAMILIAR {i+1}===============")
        print("NOMBRE : {}\nAPELLIDO : {}\nTIPO DE DOCUMENTO : {}\nDOCUMENTO : {}\nFECHA NACIMIENTO : {}\nPARENTESCO : {}".format(nombre[i].upper(), apellido[i].upper(), tipoDocumento[i].upper(), numDocuemnto[i], fechaNac[i].upper(),parentesco[i].upper()))
    # acumulador para sacar el promedio de personas por hogar mas adelante
    cantidadTotalPersonas += cantidadFamiliares + 1
    hogares += 1
    print()
    evento = input("Desea registrar otro hogar ( si - no ): ")

promedio = cantidadTotalPersonas / hogares

print("\n====================================\nEl promedio de personas por hogar es de: {}".format(promedio))






