# clase Principios de informática g14
# 28/Agosto/2018

class Lobo:
    def __init__(self, nombreDelLobo, colorDePelaje):
        self.nombre = nombreDelLobo
        self.pelaje = colorDePelaje

    def comer (self, tipoDeComida):
        print ("El lobo " + self.nombre + " está comiendo " + tipoDeComida)

    def describir(self):
        print("El lobo " + self.nombre + " tiene pejaje de color " + self.pelaje)

class Ballena:
    def __init__ (self, nombre, tamano, peso, sexo):
        self.nombre = nombre
        self.tamano = tamano #tamaño en metros
        self.peso   = peso   #peso en kilogramos
        self.sexo   = sexo

    def nadar (self):
        print (self.nombre + "está nadando")

class Zoo:
    def __init__ (self, nombre, animal1, animal2):
        self.nombre = nombre
        self.animal1 = animal1
        self.animal2 = animal2
    
    def describir(self):
        print ("En el zoológico " + self.nombre + "tenemos dos animales: un lobo llamado " + self.animal1.nombre + " y una ballena llamada " + self.animal2.nombre)


nombreBallena = input ("Digite el nombre de la ballena:")
pesoBallena   = input ("Digite el peso")
ballena1 = Ballena(nombreBallena, 5.1, int(pesoBallena), "hembra")  
lobo1 = Lobo("Nestor", "gris")


zoo1 = Zoo ("zzzz", lobo1, ballena1)
zoo1.describir()