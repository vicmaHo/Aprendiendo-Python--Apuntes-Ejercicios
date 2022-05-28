"""
PROBLEMA 2

Integrantes: 
-Victor Manuel Hernandez Ortiz  - 2259520
-Juan Pablo Castaño Arango      - 22559487
-Juan Pablo Escobar Viveros     - 2259519

Profesor: Andres Fernando Velasco
Grupo: 50
Laboratorio: 1

"""
# entrada
print("""Bienvenido, ciudadano.
Por favor, digite aqui su peso en la tierra para saber su peso en los diferentes cuerpos celestes.""")
pesoT = float(input("Aqui: "))

#proceso
if (pesoT > 0):
    masa = pesoT / 9.8
    pesoMarte = masa * 3.711
    pesoJupiter = masa * 24.79
    pesoLuna = masa * 1.622
else:
    print(
    """Usted ha ingresado un valor igual o inferior a 0, o un tipo de valor no numeral.
    Por lo tanto, reinicie y digite nuevamente.""")

#salida
if pesoT > 0:
    print ("Su peso en los diferentes cuerpos celestes es:")
    print("Peso en marte:", pesoMarte, "kgs\nPeso en Jupiter:", pesoJupiter, "kgs\nPeso en la Luna:", pesoLuna, "kgs")

