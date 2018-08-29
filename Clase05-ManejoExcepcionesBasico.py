#Manejo de excepciones utilizando Python

edad = input("Digite su edad") # La edad recibida, es una hilera
try:
	#Note que la edad al ser un entero, debemos realizar una conversion
	#La cual puede fallar
	edadNumerica = int(edad)
	edadNumerica = edadNumerica + 1
	print("El próximo año tendrá ", edadNumerica , "años")
except Exception as error:
	#Si ocurre un error, se dispara el bloque Exception
	print ("Ocurrió el error: ", error)

#Intente ejecutar este programa escribiendo números o letras para ver los resultados

