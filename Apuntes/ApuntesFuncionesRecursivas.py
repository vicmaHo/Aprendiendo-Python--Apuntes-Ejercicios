# Funciones recursivas apuntes
# Hacer que algunos patrones se repitan, se repiten los mismos elementos pero mas pequeños
# no es un ciclo, es un elemento repetitivo.
# en pocas palabras ES UNA FUNCION QUE SE LLAMA ASI MISMA
# La recursión se define como el acto de una función llamándose a sí misma.

# aqui añadi librerias para probar algunas cosas
from time import sleep

def cuentaRegresiva(n):
    sleep(1)
    if n > 0:
        print(n)
        cuentaRegresiva(n - 1)
        sleep(1)
    else:
        sleep(1) 
        print("Booom!")
        
cuentaRegresiva(10)