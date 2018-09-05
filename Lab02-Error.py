#Nombre: 
#INSTRUCCIONES:
#NO AGREGUE NI ELIMINE líneas de código. Sólo debe corregir los errores sintácticos o lógicos 
#presentes en el código a continuación. 
#Para cada uno de los errores vea el mensaje. Identifique y corrija el error. 
#Al final de cada Caso, usando comentarios, describa el o los errores encontrados y qué fue lo que hizo para corregirlo. 


#˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
#Caso #1
#Identifique y corrija el error en la instrucción print
varA = 6
varB = "núcleos"

print ("Mi computadora tiene " + varA + varB)


#˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
# #Caso #2
#Lea el siguiente código cuidadosamente. El objetivo es instanciar 2 veces la clase carta y e imprimir la información de las 2 cartas instanciadas
#Ejecutélo. El intérprete de Python lanzará al menos un error. 
#Note que el error se da en el print. Sin embargo, ahí no está el error. 
#Analice cuál es el error y corrija el código. 
class Carta:

	def __init__(self, numero, palo):
		self.numero = numero
		self.palo = palo

	def imprimir(self):
		print("La carta es: " + str(self.numero) + " de " + self.palo)

carta1 = Carta (1, "Diamantes")
carta2 = Carta ("Corazones", 2)

carta1.imprimir()
carta2.imprimir()

#˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
#Caso #3
#Lea el siguiente código cuidadosamente.
#Hay al menos un error. Analice y corrija los errores. 
class Cable:
    def __init__(self, diámetro, marca, material):
        self.diámetro = diámetro
        self.marca    = marca
        self.material = material

    def describir(self):
        print("Marca: " + self.Marca, "Diámetro: " + self.diámetro + "mm", "Material: " + self.material)

cableNuevo = Cable (20.2, "Cable Bueno", "poliuretano") 
cableNuevo.describir()

#˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
#Caso #4
#Lea el siguiente código cuidadosamente.
#Hay dos errores. Corríjalos. 
class MaquinaDeProduccion:
    def _init_ (self, marca, velocidad, modelo)
        self.marca = marca
        self.velocidad = velocidad
        self.modelo = modelo

    def aumentarVelocidad(self):
        self.velocidad = self.velocidad + 10

    def disminutirVelocidad(self):
        self.velocidad = self.velocidad - 10

mdp = MaquinaDeProduccion("MDP La Mejor", 33, "ABC123")
mdp.aumentarVelocidad()
print (mdp.velocidad)

#˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
#Caso #5
#Lea el siguiente código cuidadosamente.
#Hay varios errores. Corríjalos. 
class ObjetoMisterioso:
    def __init__ (self, atributo0, atributo1, atributo2):
        self.a = atributo0
        self.b = atributo1
        self.c = atributo2

    def sumar(self):
        print(a+b+c)

    def restar(self):
        print(a-b-c)

    def multiplicar(self):
        print(a*b*c)

tmp1 = ObjetoMisterioso (10,10,10)
tmp2 = ObjetoMisterioso (tmp1.a+tmp1.c, 15, 100)

tmp2.multiplicar()

#˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
#Caso #6
#Lea el siguiente código cuidadosamente.
#Hay varios errores. Corríjalos. 
class ObjetoMisterioso2:
    def __init__ (self, atributo0, atributo1, atributo2):
        self.a = atributo0
        self.b = atributo1
        self.c = atributo2

    def mostrarAtributos(self):
        print (self.a, self.b, self.c)

    tmp3 = ObjetoMisterioso2 ("a", -90.23, "k")
    tmp3.mostrarAtributos()

#˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
#Caso #7
#Lea el siguiente código cuidadosamente.
#Hay varios errores. Corríjalos. 
print ((2,9), end = "/n")
print ("Hola, hoy es %s de %d" %(31, "Agosto"))
tmp4 = input ("Digite un número: ")
print (tmp4 + 1)
