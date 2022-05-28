# Crear una aplicación que permita:
# • Generar los números enteros pares entre p y q
# • Generar los números enteros impares entre a y b
# • Generar los primeros z múltiplos de 3
# • Generar la suma de m primeros múltiplos de 7 más los n
# primeros múltiplos de 9


# 1. Generar los numeros enteros pares entre p y q

# p = int(input())
# q = int(input())

# for i in range(p, q+1):
#     if i % 2 == 0 and i != 0: 
#         print(i)
        
# 2. Numeros impares entre a y b
# a = int(input("Numero a: "))
# b = int(input("Numero b: "))
# cantidad = 0

# for i in range(a, b+1):
#     if i % 2 !=   0: # Los numeros que son impares
#         print(i)

# 3. Generar los primeros z multiplos de 3
z = int(input("Ingresar z: "))        

for i in range(1, z+1):
    if i % 3 == 0:
        print(i)
    

        