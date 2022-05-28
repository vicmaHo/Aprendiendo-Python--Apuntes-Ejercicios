# Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0. El algoritmo debe imprimir 
# el valor ingresado, y de ser una nota mayor o igual a 4.0, deberá imprimir un mensaje de 
# felicitaciones.

def notaDefinitiva(nota: float) -> str: 
    # validar los parametros
    if not(isinstance(nota, float)):
        return f"Debe ingresar un valor decimal"
    # not(nota > 0 and nota <= 5)
    if nota < 0 or nota > 5:
        return f"Su nota definitiva debe estar entre 0 y 5"
    # procesamiento
    if nota >= 4.0:
        mensaje = "Felicitaciones!!"
    else:
        mensaje = ""

    # salida
    return f"La nota es: {nota} {mensaje}"

print(notaDefinitiva(9.0))