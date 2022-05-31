#Tudor está sentado en la clase de matemáticas, en su ordenador portátil. Es evidente que no está 
# prestando atención en esta situación. Sin embargo, su profesor de matemáticas le llama para que haga 
# algunos problemas. Como su profesor de matemáticas no esperaba mucho de Tudor, sólo tiene que hacer algunos 
# problemas sencillos de suma. Sin embargo, lo sencillo para ti y para mí puede no serlo para Tudor, así que ¡ayúdale!

# Especificación de la entrada
# La primera línea contendrá un número entero N (1 <= n <= 100000), el número de problemas de suma que Tudor
# necesita hacer. 
# Las siguientes n líneas contendrán cada una dos enteros separados por espacios cuyo valor absoluto es menor
# que , los dos enteros que Tudor necesita sumar.

# Especificación de la salida
# Imprime n líneas de un entero cada una, las soluciones a los problemas de adición en orden.

n = int(input())

for i in range(0, n):
    t = input().split(" ")
    a = int(t[0])
    b = int(t[1])
    print (a + b)
