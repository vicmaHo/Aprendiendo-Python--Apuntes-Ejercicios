"""
elaborar un program que lea una frase o parrafo e indique el numero de palabras del parrafo
NOTA: Supongs que el usuario digita unicamente un espacio entre cada par de palabras
"""

frase = input("Digite la frase: ")

# contar el numero de espacios, es decir cada palabra 

palabras = 1
for i in frase:
    if i == ' ':
        palabras += 1
print('el numero de palabras es:', palabras)


# version corta
print(f"el numero de palabras es: {frase. count(' ') + 1}")