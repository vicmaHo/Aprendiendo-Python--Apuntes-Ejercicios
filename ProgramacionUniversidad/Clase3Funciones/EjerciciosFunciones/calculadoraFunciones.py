#### funciones
def sumar (a, b):
    resultado = a + b
    return resultado

def restar (a, b):
    resultado = a - b
    return resultado

def multiplicar (a, b):
    resultado = a * b
    return resultado

###  programa principal



# entrada
print("""
Calculadora, opciones:
1) Sumar
2) Restar
3) Multiplicar""")
opcion = int(input("\nQue opcion desea?: "))

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))

# proceso
if opcion == 1:
    resultado = sumar(num1, num2)
elif opcion == 2:
    resultado = restar(num1, num2)
elif opcion == 3:
    resultado = multiplicar(num1, num2)

# salida
if opcion >=1 and opcion <=3:
    print(f"El resultado de su operacion es: {resultado}")
else:
    print("No selecciono una opcion correcta")
