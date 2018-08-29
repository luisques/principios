#---------------------------------
#Para ejecutar este código, hacerlo desde consola 
#Para ejecutar desde consola escribir: python <nombreDelArchivo>.py
#O utilizando el plugin SublimeREPL (mostrado en la sección de consultas)
#---------------------------------

#Ejemplo de entrada y salida por consola

#Para desplegar datos en consola podemos utilizar el metodo print
#Como se vió, el método se puede llamar de varias formas, a continuación algunos ejemplos:

#Forma básica
print("Hola mundo")

#Mezclando tipos de datos
print("hoy es", 28, "de agosto del ", 2018)

#Formato de Strings
print("Hoy es %d de %s del %d" %(28,"agosto" ,2018))

#Cambiando el final de línea para sobreescribir un \n
print("Hola", end=" ")
print("Mundo")

#Para solicitar datos se utiliza el método input
#De forma predeterminada el método retorna una hilera de caracteres
#Podemos almacenar esa hilera dentro de una variable para poder utilizarla posteriormente
#Por ejemplo:
nombre = input("Digite su nombre") #la variable nombre contiene entonces el valor digitado por el usuario
print("Hola",nombre,"!")