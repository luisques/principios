from Lector import Lector
from EscritorDeArchivos import EscritorDeArchivos

class CadenasADN:

	def __init__(self, nombreArchivo):
		self.nombreArchivo = nombreArchivo

		lector = Lector(nombreArchivo)
		self.contenido = lector.leerArchivo()
		self.contenido = self.contenido.upper().replace("\n","")

	def escribirPuentes(self):
		escritor = EscritorDeArchivos("puentes.txt")
		for letra in self.contenido:
			escritor.escribir(self.obtenerPuente(letra) + "\n")
		escritor.cerrar()

	def escribirPuenteInvertido(self):
		escritor = EscritorDeArchivos("PuenteInvertidoHorizontalmente.txt")
		for letra in self.contenido:
			puente = self.obtenerPuente(letra)
			escritor.escribir(puente[::-1] + "\n")

		escritor.cerrar()


	def invertirVerticalmente(self):
		indice = len(self.contenido)-1
		escritor = EscritorDeArchivos("PuenteInvertidoVerticalmente.txt")
		while(indice >= 0):
			puente = self.obtenerPuente(self.contenido[indice])
			escritor.escribir(puente+ "\n")
			indice -= 1

	def obtenerPuente(self, letra):
		puente =""
		if(letra == "A"):
			puente = "A=T"
		elif(letra == "T"):
			puente = "T=A"
		elif(letra =="G"):
			puente = "G=C"
		else:
			puente = "C=G"
		return puente



instancia = CadenasADN("cadenasADN.txt")
instancia.escribirPuentes()
instancia.escribirPuenteInvertido()
instancia.invertirVerticalmente()


