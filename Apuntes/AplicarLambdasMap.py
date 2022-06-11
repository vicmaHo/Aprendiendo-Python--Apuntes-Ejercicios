# lambas y map

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [8, 10, 20 ,30]
print(list(map(lambda x, y, z: x*y*z, a, b, c)))  # con map iteramos en cada una de las listas a y b, y aplicamos la funcicion lambda
                                          # la cual recibe valores x y. los multiplica y los devuelve como map que posteriormente
                                          # se trasnforma en un lista. 

print("=" * 30)
# dejo la lista almacenada 
d = list(map(lambda x, y, z: x*y*z, a, b, c))

print(d)