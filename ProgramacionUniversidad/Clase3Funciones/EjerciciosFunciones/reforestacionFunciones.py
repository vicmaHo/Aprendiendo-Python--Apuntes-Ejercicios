"""
Se desea reforestar un bosque que mide un número n de hectáreas. Si la
superficie del terreno excede a 1'000.000m2
, entonces se siembra así:

    % superficie    tipo de arbol
    70%             Pino
    20%             Oyamel
    10%             Cedro

la superficie del terreno es menor o igual a 1'000.000m2 entonces se
siembra así:

    % superficie    tipo de arbol
    50%             Pino
    30%             Oyamel
    20%             Cedro

Se desea saber el número de pinos, oyameles y cedros que se deben
sembrar, si se sabe que en 10m2 caben 8 pinos; en 15m2 caben 15
oyameles, y en 18m2 caben 10 cedros.
"""


#----funciones----
def calculaPino(hectareas):
    m2 = hectareas * 10000
    if m2 > 1000000:
        numeroPinos = ((m2 * 0.7) / 10) * 8
    else:
        numeroPinos = ((m2 * 0.5) / 10) * 8
    return numeroPinos

def calculaOyamel(hectareas):
    m2 = hectareas * 10000
    if m2 > 1000000:
        numeroOyameles = ((m2 * 0.2) / 15) * 15
    else:
        numeroOyameles = ((m2 * 0.3) / 15) * 15
    return numeroOyameles

def calculaCedro(hectareas):
    m2 = hectareas * 10000
    if m2 > 1000000:
        numeroCedro = ((m2 * 0.1) / 18) * 10
    else:
        numeroCedro = ((m2 * 0.2) / 18) * 10
    return numeroCedro


#----principal

#entrada

hectareas = int(input("Ingrese la cantidad de hectareas: "))

#proceso

numeroPinos = calculaPino(hectareas)

numeroOyameles = calculaOyamel(hectareas)

numeroCedros = calculaCedro(hectareas)

#salida
print(
f"""En {hectareas} caben:
{numeroPinos} pinos
{numeroOyameles} oyameles
{numeroCedros} cedros""")