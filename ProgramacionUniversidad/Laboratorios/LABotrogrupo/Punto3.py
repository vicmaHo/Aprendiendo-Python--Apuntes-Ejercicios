#Ejercicio de cd - punto 2
import math    # import se usa para importar funciones que han sido exportadas de un servidor externo  

# entradas - nombre del profesor - capacidad de almacenamiento en GB - valor unitario del cd

nombre = input("Ingrese su nombre: ")
almacenamientoGb = int(input("Ingrese el almacenamiento en GB: "))
valorCd = int(input("Ingrese el valor unitario del CD: "))

# proceso un diso tiene 700mb y 1 gb equivale a 1024mb

almacenamientoMb = almacenamientoGb * 1024

CdNecesarios = almacenamientoMb / 700

CdNecesarios = math.ceil(CdNecesarios)

valorTotal = CdNecesarios * valorCd

# salida
print(f"Para almacenar {almacenamientoGb}GB se necesitan {CdNecesarios}CDS que cuestan {valorTotal}")

