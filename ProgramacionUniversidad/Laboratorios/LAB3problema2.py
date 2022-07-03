"""
La División de Recursos Humanos de la Universidad requiere un programa que le permita
calcular el neto a pagar para cada uno de sus empleados. Este valor se calcula con base
en los pagos y descuentos que se realizan para cada empleado. Los conceptos de pago y
descuento a tener en cuenta son:

PAGOS                       DESCUENTOS

SALARIO BÁSICO              SALUD
SUBSIDIO DE TRANSPORTE      PENSIÓN
BONIFICACIÓN DE SERVICIOS   RETEFUENTE

Estos pagos y descuentos se calculan como un porcentaje sobre el salario básico de la
siguiente manera:
CONCEPTO                    PORCENTAJE

SUBSIDIO DE TRANSPORTE      20%
BONIFICACIÓN DE SERVICIOS   10%
SALUD                       4%
PENSIÓN                     4%
RETEFUENTE                  5%

Desarrolle un programa que permita:
1. Realizar los cálculos para N empleados, siendo N un número digitado por el usuario.
2. Capturar el número de documento de identidad, nombre completo y salario básico de
cada empleado.
3. Calcular el total de pagos, total descuentos y el neto a pagar.
4. Calcular y mostrar cada uno de los conceptos.

"""
numeroEmpleados = int(input("Digite el numero de empleados: "))

for i in range(numeroEmpleados):
    print("="* 20 + "Ingreso de datos" + "="*20)
    # ingreso de datos de cada empleado
    numeroDocumento = input("Ingrese su numero de documento: ")
    nombre = input("Ingrese su nombre: ")
    salario = float(input("Ingrese el salario: "))
    
    # proceso de datos
    bonificacionServicios = salario * 0.1
    subsidioTransporte = salario * 0.2
    
    salud = salario * 0.04
    pension = salario * 0.04
    retefuente = salario * 0.05
    
    totalesPago = salario + bonificacionServicios + subsidioTransporte
    totalesDescuento = salud + pension + retefuente
    netoApagar = totalesPago - totalesDescuento
    
    # salida
    print("="* 20 + "DATOS DEL EMPLEADO" + "="*20, f"\nNombre: {nombre.upper()}\nDocumento: {numeroDocumento}")
    
    print("="* 20 + "PAGOS" + "="*20,f"\nSalario: {salario}\nBonificacion de servicios: {bonificacionServicios}\nSubsidio de transporte: {subsidioTransporte}")
    
    print("="* 20 + "DESCUENTOS" + "="*20, f"\nSalud: {salud}\nPensión: {pension}\nRetención: {retefuente}")
    
    print("="* 20 + "TOTALES" + "="*20, f"\nTotale pagos: {totalesPago}\nTotal descuento: {totalesDescuento}\nNeto a pagar: {netoApagar}")
    

    
    