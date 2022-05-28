def cliente(informacion: dict) -> dict:
    datos = {"nombre": informacion["nombre"], "edad": informacion["edad"]}
    if informacion["edad"] >= 7:
        if informacion["edad"] > 18:
            datos["atraccion"] = "X-Treme"
        elif informacion["edad"] >= 15 and informacion["edad"] <= 18:
            datos["atraccion"] = "Carros chocones"
        elif informacion["edad"] >= 7 and informacion["edad"] < 15: # podemos abreviarlo con el else
            datos["atraccion"] = "Sillas voladoras" 
        datos["apto"] = True
    else:
        datos["atraccion"] = "N/A"
        datos["apto"] = False
    datos["primer_ingreso"] = informacion["primer_ingreso"] # añado al diccionario de salida el dato de primeringreso
    # valor de atraccion
    if datos["atraccion"] == "X-Treme":
        if datos["primer_ingreso"] == True:
            datos["total_boleta"] = 20000 - (20000 * 0.05) # valor total menos el descuento del 5%
        else:
            datos["total_boleta"] = 20000
    elif datos["atraccion"] == "Carros chocones":
        if datos["primer_ingreso"] == True:
            datos["total_boleta"] = 5000 - (5000 * 0.07) 
        else:
            datos["total_boleta"] = 5000
    elif datos["atraccion"] == "Sillas voladoras":
        if datos["primer_ingreso"] == True:
            datos["total_boleta"] = 10000 - (10000 * 0.05) 
        else:
            datos["total_boleta"] = 10000
    else:
        datos["total_boleta"] = "N/A"
    return datos

    



# diccionario 
informacion = {
    "id_cliente": 4,
    "nombre": "Tatiana Ruiz",
    "edad": 8,
    "primer_ingreso": True
}

# Llamamos al diccionario
print(cliente(informacion))