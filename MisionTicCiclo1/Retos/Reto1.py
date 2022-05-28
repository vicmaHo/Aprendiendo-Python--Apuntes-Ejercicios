## Reto 1 ## 

def CDT(usuario: str,  capital: int, tiempo: int):
    porcentajeInteres = 3 / 100
    porcentajeAperder = 2 / 100
    if  tiempo <= 2:
        valorAperder = capital * porcentajeAperder 
        valorTotal = capital - valorAperder 
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}"
    else:
        valorIntereses = (capital * porcentajeInteres * tiempo) / 12
        valorTotal = capital + valorIntereses 
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}"

