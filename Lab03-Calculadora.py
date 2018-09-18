class Calculadora:

	# Todos los metodos tienen la siguiente forma:
	# 1. Palabra reservada def (para definir un metodo)
	# 2. Nombre del metodo con el que se identificara: e.g sumar
	# 3. Parentesis con parametros (los que se necesiten para que funcione correctamente)
	# 3.1 si el metodo es parte de una clase, debera llevar como primer parametro self
	# 4 Opcional un return al final del metodo, este sera el valor o resultado que
	# devolvera el metodo una vez ejecutado

	# En el siguiente ejemplo tenemos un metodo sumar, queremos que quien llame al metodo
	# envie por parametro dos valores de tipo numerico.
	# De igual forma, el metodo retornara un valor numerico con el resultado de la suma
	# a quien invoco al metodo.
	def sumar(self, valor1, valor2):
		resultado = valor1 + valor2
		return resultado

	def dividir(self, dividendo, divisor):
		resultado = 0
		try:
			resultado = dividendo/divisor
		except zeroDivision as error:
			print ("Error al dividir")

		return resultado

# El siguiente metodo (main) no es parte de la clase Calculadora
# Este metodo se ejecutará al ejecutar el programa
# Esto permite tener un mayor orden y claridad a la hora de ejecutar archivos o scripts
def main():
	calculadora = Calculadora()
	valorA = 5.25
	valorB = 8.10
	# El metodo sumar requiere que se le envien por parametro dos valores numericos
	# Tambien retornara un valor numerico, resultado al que se le asignara a la variable
	# bautizada resultado1
	resultado1 = calculadora.sumar(valorA, valorB)
	print(resultado1)
	resultado2 = calculadora.dividir(valorA, valorB)
	print(resultado2)


# La siguiente instruccion if, permite determinar si el archivo se esta ejecutando 
# como main (o hilo principal), esto se determina al ejectura python Calculadora.py
# Esto permite luego, tener varios archivos y que solo se ejecute el main que nos interesa
# y no todo el codigo de todos los archivos
if __name__ == "__main__":
	main()
