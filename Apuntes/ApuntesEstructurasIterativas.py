# Apuntes - estructuras iterativas
"""
Iterar consiste en repetir una accion varias veces
Python cuenta con dos estructuras que nos permiten realizar iteraciones (ciclos)
estas son: for y while

For: este nos permite iterar un numero fijo de veces, tambien nos permite recorrer secuencias ya sean listas
tuplas, diccionarios, strings 
While: esta estructura permite iterar siempre que se cumpla cierta condicion. 

Cuando usarlas: el For se usa cuando sabemos o podemos saber el numero de iteraciones que realizaremos, mientras que 
While se usa cuando no conocemos el numero de iteraciones que se deben realizar


Sintaxis
for variable in range(0, 11, 1):      lo que hacemos aqui es recorrer un rango de numeros(del 0 hasta el n-1 (10))
    print("iteracion", variable)      nosotros podemos definir ese rango
    
    
es importante inicializar nuestras variables de control para poder tener un control sobre la ejecucion del ciclo while
ya que sin estas, el ciclo se puede volver infinito
n = 0           inicializacion
while n <= 5;   condicion
    print("iteracion", n)
    n += 1      incremento
"""
