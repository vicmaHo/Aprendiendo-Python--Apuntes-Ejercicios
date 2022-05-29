# Este taller debe crear una biblioteca llamada taller y la solución de cada ejercicio 
# se realizará en una función llamada 
# ejercicio_X, donde X es el número del ejercicio.

# 1. Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
def saludo(nombre: str)-> str:
    return f" ¡Hola {nombre}"

# 2.Escribir una función que reciba un número entero positivo y devuelva su factorial.
def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


# 3. Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver 
# el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%.

def totalFactura(cantidad, porcentajeIva = 0.19):
    descuento = cantidad * porcentajeIva
    total = cantidad - descuento
    return total

# Escribir una función que calcule el área de un
# círculo y otra que calcule el volumen de un cilindro usando la primera función.

def calculaArea(radio):
    PI = 3.1415
    area = PI * (radio**2)
    return area
def calculaVolumen(radio, altura):
    volumen = calculaArea(radio) * altura
    return round(volumen, 2)
    
# 5. Escribir un programa que lea un entero positivo n, introducido por el usuario y después
# muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los primeros 
# enteros positivos puede ser calculada de la siguiente forma: (n(n+1)) / 2

def sumaNumeros(numero):
    resultado = numero * (numero + 1) / 2
    return resultado

# 6. scribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla 
# la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado 
# redondeado con dos decimales.
def calculoIMC(peso, estatura):
    imc = peso / (estatura * estatura)
    return f"Tu índice de masa corporal es {round(imc, 2)}"

# 7. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por 
# correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
# peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
# cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último 
# pedido y calcule el peso total del paquete que será enviado.

def calculaPeso(cantidadMunecas, cantidadPayasos):
    pesoPayaso = 112
    pesoMuneca = 75
    pesoTotal = (pesoPayaso * cantidadPayasos) + (pesoMuneca * cantidadMunecas)
    return f"El peso total del paquete de payasos y muñecas es de: {pesoTotal}g"

# 8. Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un
# descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que 
# no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el
# descuento que se le hace por no ser fresca y el coste final total.

def panaderia(barrasVendidas):
    precioNormal = 3.49
    porcentajeDescuento = 0.6
    valorSinDescuento = barrasVendidas * precioNormal
    descuento = valorSinDescuento * porcentajeDescuento
    valorReal = valorSinDescuento - descuento
    return f"Precio habitual de la barra de pan: {precioNormal}\nPrecio Sin Descuento: {round(valorSinDescuento,2)}\nDescuento: {descuento}\nValor final: {round(valorReal, 2)}"

# 9. Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de 
# tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la 
# cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
# la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

def cuentaAhorro(cantidadDepositada):
    interes = 0.04
    ahorroPrimeranio = cantidadDepositada + (cantidadDepositada * interes)
    ahorroSegundoanio = ahorroPrimeranio + (ahorroPrimeranio * interes)
    ahorroTerceranio = ahorroSegundoanio + (ahorroSegundoanio * interes)
    return f"El ahorro al primer año es de: {ahorroPrimeranio}\nEl ahorro al segundo año es de:{ahorroSegundoanio}\nEl\
 ahorro el tercer año es de: {ahorroTerceranio}"

# 10. Crea un programa que dado un número entero que designa un periodo de tiempo expresado 
# en segundos, imprima el equivalente en días, horas, minutos y segundos.
# Por ejemplo:
# 300000 segundos serán 3 días, 11 horas, 20 minutos y 0 segundos.
# 7400 segundos serán 0 días, 2 horas, 3 minutos y 20 segundos.

def calculaTiempo(segundos):
    dias = segundos //  86400
    horas = segundos // 3600
    horasReales = horas % 24
    minutos = segundos // 60
    minutosReales = minutos % 60
    segundosReales = segundos % 60
    return f"{dias} dias, {horasReales} horas, {minutosReales} minutos y {segundosReales} segundos."
    
    
    


