#Los comentarios en Python inician con el símbolo -> #
#Un comentario es descartado a la hora de compilar y ejecutar un programa
#Es utilizado para hacer el código fuente más legible para quien lo lee
#Cualquier elemento luego del # es descartado hasta el siguiente inicio de línea

class Carta: #Declaración de una clase, usando la palabra resevada class
	
	#Los elementos indentados (con sangría a este nivel) serán parte de la clase
	
	#Constructor de clase, la acción __init__ es llamada sólo una vez
	#Cuando se crea una nueva instancia de la clase
	#Entre los paréntesis se definen las variables que se desean recibir al
	#Crear un objeto y usarlas para dar valor a los atributos
	def __init__(self, numero, palo): 
		#Los elementos con sangría a este nivel serán parte del método __init__
		self.numero = numero #Se crea un atributo numero usando la sintaxis self.X
		self.palo = palo #Se crea e inicializa el atributo palo

	def imprimir(self):
		print("La carta es: " + str(self.numero) + " de " + self.palo)
		#Recuerde que para concatenar (unir) Strings, todos los elementos
		#Deben ser del mismo tipo por lo que convertimos el numero en un String


#Creamos instancias de la clase Carta
#Note que esto no es parte de la clase, por tanto la indentación (Sangría)
#Vuelve a la izquierda
c1 = Carta(7,'Corazones')
c1.imprimir()

#Creamos una segunda instancia
c2  = Carta(10,'Diamantes')
c2.imprimir()

#Sobre una instancia existente, sobreescribir los valores de los atributos:
c1.numero = 3
c1.imprimir()