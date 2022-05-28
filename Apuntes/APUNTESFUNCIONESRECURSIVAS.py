# Funciones recursivas apuntes
# Hacer que algunos patrones se repitan, se repiten los mismos elementos pero mas pequeños
# no es un cilclo, es un elemento repetitibo 
# en pocas palabras ES UNA FUNCION QUE SE LLAMA ASI MISMA

from random import random
from time import sleep


def cuentaRegresiva(n):
    sleep(1)
    if n > 0:
        print(random())
        
        cuentaRegresiva(n + 1)
        sleep(1)
    else:
        sleep(1) 
        print("Booom!")
        
cuentaRegresiva(10)