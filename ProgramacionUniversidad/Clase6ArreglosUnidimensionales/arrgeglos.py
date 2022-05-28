"""
Arreglos unidimensionales
 
lista de datos con un numero fijo de componentes, todos del mismo tipo, que esta referenciados
bajo un mismo nombre, en python se pueden combinar los tipos pero lo ideal es que sea solo uno

todos bajo un mismo nombre: nombre del conjunto de datos

a cada componente del arreglo se identifican con un indice (0 , 1, 2, ...)  n-1

estos permiten manejra de fomra sencilla y directa conjuntos de datos del mismo tipo, de los cuales conocemos
su cantidad y con los cuales se realizaran operaciones similares


un arreglo puede verse como cajas ordenadas en fila y numeradas, donde cada caja se almacena un solo 
elemento u objeto

nombre = elementos (indice 0, 1, 2, 3, ....)
- datos del mismo tipo
- tamaño fijo
- cada elemento se guarda en un espacio independiente
- cada espacio se referencia con un indice

(el pc no maneja reales, maneja enteros representados como reales) se les llama float ya que el punto
que identifica la parte entera y la decimal es flotante ya que se puede desplazar segun la necesidad

float 8 bytes - double 16 bytes ---> la misma 


DECLARACION DE UN ARREGLO
variable = [dato1, dato2, ..., daton]



"""

a = [None]*5 # None: Asiganr 5 espacios a el arreglo a
print (a)


nombres = ["Pedro", "Mao", "Vic"]
print (nombres)


for nombre in nombres:
    print(nombre)

"""
INSERTAR DATOS EN UN ARREGLO

nombreVariable[posicion del dato] = valor del dato

"""

nombres = [None]

"""
RECUPEERAR UN DATO DE UN ARREGLO:

nombreArreglo[indice]           de forma 

"""

