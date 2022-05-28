## Entradas ##
cajasDeRefresco = 9
personas = 56
latasPorCaja = 24 
## Proceso ##
totalLatas = latasPorCaja * cajasDeRefresco
latasQuesobran = totalLatas % personas
cantidadqQueConsumenLasPersonas = totalLatas / personas
## salidas ##
print("latas que sobran:", latasQuesobran)
print("las personas consumen:", cantidadqQueConsumenLasPersonas)