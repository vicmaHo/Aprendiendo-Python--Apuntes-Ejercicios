# def example1():
#     n = 100
#     for i in range(0, (n), 1):
#         print(i)
# # Llamar la funcion example1
# example1()
    
# def example2():
#     n = 0
#     for i in range(100, (n - 1), -1):
#         print (i)
# example2()

# def numbersList():
#     for i in range(1, 6 + 1):
#         print(f"Numero {i}")
# numbersList()        
        

# n =   int(input("Input a number: "))

# for i in range(1, n+1):
#     print(i)
    
# print("Successful execution")

# With a while instruction
# While needs 2 control vars

# n = int(input("Input a number: "))
# i = 0
# while i < n:
#     print(i + 1)
#     i += 1 # Aumento de la variable de control
# print("While successful!!!!")

# def muestraAlgo():
#     for i in range (0, 20):
#         if (i%2 == 0):
#             print ("El valor de i es ", i)
            
# muestraAlgo() 


# def muestraAlgo2():
#     for j in range(0, 101):
#         if j % 3 ==0:
#             print (f"J is {j}")      
#         else:
#             print(f"{j} no es multiplo de 3")
# muestraAlgo2()
            
            
# Tener en cuenta que cuando el ciclo es interrumpido se ejecuta la instruccion que sigue despues
a = 0
for k in range(0, 5, 1): # iniciamos en 0 y llegamos hasta 5 - 1, (nunca llegamos hasta el n) y damos saltos de 1
    a += 1
print ("El valor de a es:", a)


