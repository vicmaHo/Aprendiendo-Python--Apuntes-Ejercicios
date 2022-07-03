"""
Desarrollar un programa para un club de Bolos, que permita calcular el valor total a pagar según la
frecuencia semanal y la antigüedad en meses. Para cada persona se solicitan tres datos: el nombre,
la frecuencia y la antigüedad. El programa muestra cuatro valores para cada persona: el nombre, el
tipo, el descuento y el valor a pagar. La categoría y el valor a pagar sin descuento se calculan de
acuerdo a la siguiente tabla:

Frecuencia              Categoría           Valor mes
1 día                   Bajo                14000
2 a 3 días              Normal              22000
4 o más días            Alto                40000

Cabe resaltar que se aplica un descuento según la antigüedad así: menos de un año sin descuento,
entre 1 y 5 años 10% y más de 5 años 20%. El programa a desarrollar debe definir una función en la
que se calculan los valores de salida para una persona.

"""

def categoria(frecuencia):
    if frecuencia == 1:
        categoria = "Bajo"
        valorMes = 14000
    elif frecuencia >= 2 and frecuencia <= 3:
        categoria = "Medio"
        valorMes = 22000
    else:
        categoria = "Alto"
        valorMes = 40000
    return categoria, valorMes

def descuentoSalida(antiguedadMeses, categoria, nombre):
    if antiguedadMeses < 12: 
        perDescuento = 0
    elif antiguedadMeses >=12 and antiguedadMeses <= 60:
        perDescuento = 0.1
    else: 
        perDescuento = 0.2
    
    # calcula descuento
    descuento = categoria[1] * perDescuento
    return f"NOMBRE: {nombre}\nCategoria:{categoria[0]}\nDescuento a aplicar: {perDescuento*100}%\nValor a pagar: {categoria[1]-descuento}"
    
# programa principal
i = 3
while i > 0:
    nombre = input("Ingrese su nombre: ") 
    frecuencia = int(input("En dias, ingrese la frecuencia con la que asiste en la semana: "))
    antiguedad = int(input("Ingrese la antiguedad en meses: "))
    salida = descuentoSalida(antiguedad,categoria(frecuencia), nombre)    
    print(salida)
    i -= 1
    
    