"""
Un comerciante se dedica a la venta de sillas. Vende tres tipos de sillas:

    tipo    precio
    1       5000
    2       7000
    3       10000

Por cada cinco sillas compradas se obtiene un descuento, de acuerdo a la tabla

    tipo    descuento
    1       3%
    2       5%
    3       10%

El resto de sillas se cobran a precio normal. Diseñe un programa que lea el tipo de
silla y la cantidad a comprar e imprima la cantidad, el precio unitario, el descuento
y el precio total, de lo que debe cancelar el cliente por la compra.
"""

def sillasTipo1 (cantidad):
    adicionales = cantidad % 5
    descuento = ((cantidad - adicionales) * 5000) * 0.03
    total = (cantidad * 5000) - descuento
    print 