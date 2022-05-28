# Doña Marina va al supermercado a comprar carne de cerdo y/o pollo. Cada libra
# de carne de cerdo cuesta $10500, mientras que el kilo de pollo está en $12800. Cabe mencionar que en la
# Distribuidora de Productos Cárnicos a la que va doña Marina, tienen una promoción del 5% si se compran
# en total más de 5 libras entre cerdo y pollo siempre y cuando la proporción de carne de pollo respecto del
# total sea al menos del 60%; o del 15% si se compran más de 5 kilos entre ambos tipos de carne siempre y
# cuando la proporción de carne de cerdo respecto del total sea al menos del 65%. Cabe mencionar que en
# caso de dudas el descuento a aplicar será el mayor. Usted debe desarrollar un programa de computador que
# permita leer, para un cliente, la cantidad de libras tanto de carne de cerdo como de pollo que va a comprar
# y al final mostrar el valor a pagar por cada tipo de carne, el valor del descuento alcanzado (si lo consiguió)
# y el valor a pagar.


def porcentaje_descuento(cerdo, pollo):
    libras_totales = cerdo + pollo
    proporcion_cerdo = (cerdo * 100) / libras_totales
    proporcion_pollo = (pollo * 100) / libras_totales
    if libras_totales > 5:
        if proporcion_pollo < 60:
            descuento = 0.05
        elif proporcion_cerdo < 65:
            descuento = 0.15
        else:
            descuento = 0.15
    else:
        descuento = 0
    return descuento 
# entrada
libras_cerdo = float(input("Digite la s libras de cerdo: "))
libras_pollo = float(input("Digite las libras de pollo: "))

# proceso 
libra = 0.45359
valor_pollo_libras = 12800 * libra

# libras_ambos = libras_cerdo + libras_pollo
# proporcion_cerdo = (libras_cerdo * 100) / libras_ambos
# proporcion_pollo = (libras_pollo * 100) / libras_ambos
# porcen_total = 100
# if libras_ambos > 5:
#     if proporcion_pollo < 60:
#         descuento = 0.05
#     elif proporcion_cerdo < 65:
#         descuento = 0.15
#     else:
#         descuento = 0.15
# else:
#     descuento = 0
descuento = porcentaje_descuento(libras_cerdo, libras_pollo)    

valor_cerdo = 10500 * libras_cerdo
valor_pollo = libras_pollo * valor_pollo_libras
valor_de_ambos = valor_cerdo + valor_pollo

valor_descuento = valor_de_ambos * descuento

valor_total = valor_de_ambos - valor_descuento



# salida 
print(f"valor de cerdo: {valor_cerdo}")
print(f"valor de pollo: {valor_pollo}")
print(f"valor de descuento: {descuento * 100}%")
print(f"valor a pagar: {valor_total}")