## Entradas ## segundos y vueltas por minuto
segundos = 640
vueltasPorMinuto = 147
## Proceso ## trasnformar los segundos a minutos y con esto calcular el numero de vuletas por minuto
minutos = segundos // 60 # division entera
vueltas =  vueltasPorMinuto * minutos
## Salidas ##

print(
    "El fidget spinner dara en", minutos, " minutos que son", segundos, "segundos,", vueltas, "vueltas"
)