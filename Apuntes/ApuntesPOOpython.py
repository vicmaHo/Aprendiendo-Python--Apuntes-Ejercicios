# Programacion orientada a objetos

class Animal:
    def __init__(self, especie, edad) -> None: # 
        self.especie = especie                  # self es un parametro especial
        self.edad = edad
        
    def hablar(self):
        pass
    def moverse(self):
        pass
    def describeme(self):
        print(f"Soy animal de la especie {self.especie}, tipo {type(self).__name__} y edad {self.edad} años")
        
gato = Animal("mamifero", 2) # a gato le estoy asigando una clase, quiero que me cree un objeto de la clase animal y guarde ese objeto 
                # variable gato
                
gato.describeme()

# en¿ python el constructor se usa para crear los atributos del objeto
print(type(gato))