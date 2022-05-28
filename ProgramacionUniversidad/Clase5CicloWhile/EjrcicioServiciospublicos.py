# '''
# Una empresa de servicios públicos presta servicios de acueducto (incluye alcantarillado),
# electricidad (incluye alumbrado público), aseo y telefonía.  Para facturar los servicios la
# empresa tiene en cuenta lo siguiente:
# 1. Para acueducto se cobra teniendo en cuenta el consumo mensual en metros cúbicos así:
#    Los primeros 20 metros se cobran a $3680, los siguientes 15 metros se cobrar a 4850 y los
#    metros por encima de 35 se cobran a $5950 cada uno.  Existe un cargo fijo adicional para los
#    consumos superiores a 60 metros correspondiente a $38.600.  Para el valor de alcantarilla se
#    cobra un 45% del valor liquidado por acueducto.
# 2. Para el caso de la electricidad se cobra considerando el consumo mensual en KiloWatios por
#    Hora (KWH) asi: Los primeros 180 KWH se cobrar a $320, los siguientes 120 KWH se cobran a
#    $410 y los KWH adicionales se cobran a $590 cada uno. El alumbrado público se cobra como
#    el 28% del valor liquidado de electricidad.
# 3. Para el servicio de aseo se cobra según el estrato así: Los estratos 1 y 2 pagan $8900, los
#    estratos 3 y 4 pagan $15700 y los estratos 5 y 6 pagan $37800 mensuales.
# 4. El servicio de telefonía se cobra según la cobertura contratada (puede ser local, regional o
#    nacional) así: Cobertura local $5900, cobertura regional $12300 y cobertura nacional se
#    cobran $21500.
# Usted debe hacer un programa que lea par─a cada cliente el consumo en metros cúbicos, el consumo
# en KWH, el estrato y la cobertura de telefonía y mostrar al final el valor a pagar por cada 
# servicio así como el total.  Como no se sabe cuantos clientes son, se recomienda utilizar un
# registro centinela.
# '''

######## Funciones ########
def calculaAcueducto(metrosCubicos):
   if metrosCubicos <= 20:
      valor = metrosCubicos  * 3680
   elif metrosCubicos <=35:
      valor = 20 * 3680 + (metrosCubicos - 20) *4850
   elif metrosCubicos <= 60:
      valor = 20 * 3680 + 15 * 4850 + (metrosCubicos - 35) * 5950
   else:
      valor = 20 * 3680 + 15 * 4850 + (metrosCubicos - 35) * 5950 + 38600 # esto ultimo es el cargo de ser mayor que 60
   alcantarillado = valor * 0.45
   valorTotal = valor + alcantarillado
   return valorTotal

def calculaEnergia(kwh):
   if kwh <= 180:
      valor = kwh * 320
   elif kwh <= 300:
      valor = 180 * 320 + (kwh - 180) * 410
   else:
      valor = 180*320 + 120 * 410 + (kwh - 300) *590
   alumbrado = valor  * 0.28
   valorTotal  = valor + alumbrado
   return valorTotal

def aseo(estrato):
   if estrato == 1 or estrato == 2:
      valor = 8900
   elif estrato == 3 or estrato == 4:
      valor =  15700
   else:
      valor = 37800
   return valor

def telefonia(tipoServicio):
   if tipoServicio == "L":
      valor = 5900
   elif tipoServicio == "R":
      valor = 12300
   elif tipoServicio == "N":
      valor = 21500
   return valor

# 4. El servicio de telefonía se cobra según la cobertura contratada (puede ser local, regional o
#    nacional) así: Cobertura local $5900, cobertura regional $12300 y cobertura nacional se
#    cobran $21500.
      


######## Programa principal  ########
while True:
   ## Entrada de datos ###
   metrosCubicos = int(input("Ingrese el consumo de agua en metros cubicos: "))
   if metrosCubicos <= 0:
      print("Gracias por usar el programa.")
      break
   kwh = int(input("Ingrese el consumo de electricidad en kwh: "))
   estrato = int(input("Ingrese el estrato: "))
   cobertura = \
      input("Digite la cobertura del servicio de telefocnia asi - (L) Local, (R) Regional o (N) Nacional: ")
   cobertura = cobertura.upper()

   ## Proceso ##
   valorAcueducto = calculaAcueducto(metrosCubicos)
   valorEnergia = calculaEnergia(kwh)
   valorAseo = aseo(estrato)
   valorTelefonia = telefonia(cobertura)
   valorTotal = valorAcueducto + valorEnergia + valorTelefonia + valorAseo
   ## Salida de resultados ##
   print(f"==========EMPRESA DE SERVICIOS PUBLICOS MUNICIPALES==========")
   print("==================Municipio  de Buga====================")
   print(f"Valor de acueducto: {valorAcueducto}")
   print("=================================")

   print(f"Valor de acueducto: {valorEnergia}")
   print("=================================")

   print(f"Valor de acueducto: {valorAseo}")
   print("=================================")

   print(f"Valor de acueducto: {valorTelefonia}")
   print("=================================")

   print(f"\nTOTAL A PAGAR: ")
   print(f"========{valorTotal}=======")
   print("\nGracias por su pago oportuno")