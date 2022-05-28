pesoT = float(input("Digite su peso en la tierra: "))


# proceso - calcular el peso de la persona en diferentes cuerpos celestes

masaPersona = pesoT / 9.8

pesoMarte = masaPersona * 3.711
pesoJupiter = masaPersona * 24.79
pesoLuna = masaPersona * 1.622

# salida

print(
f"""\n\nSU PESO EN MARTE ES DE: {pesoMarte} kgs
SU PESO EN JUPITER ES DE: {pesoJupiter} kgs
SU PESO EN LA LUNA ES DE: {pesoLuna} kgs
"""
)
