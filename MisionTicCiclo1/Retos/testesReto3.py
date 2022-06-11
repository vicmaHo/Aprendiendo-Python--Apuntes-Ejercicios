
lists =[
(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),    
(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')
]

for ite in lists:
    print(ite)
    
dictionary = {}
# for i in range(len(lists)):
#     dictionary[lists[i][0]] = tuple(lists[i][1:])
# print(dictionary)
for i in range(len(lists)):
    dictionary[i] = tuple(lists[i])
    


print("="* 30)
for key in dictionary.keys():
    print(key)
    print(dictionary[key])
print("="* 50)
print("Longitud de la lista",len(lists))
print("="* 50)
print(len(dictionary))
print("="* 50)
idProducto = 2010



# print("="* 50)
# dicctest = {0: ("VIctor", 18, "Masculino"), 0: ("Rick", 22, "Rarito")}

# for key in dicctest.keys():
#     print(key)

# for i in range(len(dicctest)):
#     for j in range(len(dicctest[i])):
#         print(dicctest[i][j])

consultaRegistro(AutoPartes([
(5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
(3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
(3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
(8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]), 2001)

consultaRegistro(AutoPartes([
(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),    
(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)


consultaRegistro(AutoPartes([
(9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
(9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
(2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
(5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]), 9852)