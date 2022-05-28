# entrada
altura = float(input("Ingrese la altura del cilindro: "))
radio = float(input("Ingrese el radio de la base el cilindro: "))

#proceso

volumen = ((3.14159265359 * (radio ** 2)) * altura)

area = ((2 * 3.14159265359) * (radio * altura)) + ((2 * 3.14159265359) * (radio ** 2))

# salida

print(
f"""
\nVOLUMEN DEL CILINDRO: {volumen}
AREA DEL CILINDRO: {area}
""")