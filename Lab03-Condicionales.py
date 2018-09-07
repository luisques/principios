# Principios de informática - Laboratorio 3 - grupo 14
# 7/Septiembre/2018

# Instrucciones: 
# 1. Lea cuidadosamente todos los comentarios de este archivo. 
# 2. Guarde este archivo como Lab03-SuNombre.py
# 3. Agregue un comentario con su nombre al inicio del archivo recién creado

class Edificio:

    def __init__ (self, nombre, numPisos, numLamparasT1, numLamparasT2, numLamparasT3, detalleLamparaT1, detalleLamparaT2, detalleLamparaT3):
        #-->Iniciar atributos aquí, de acuerdo a los parámetros recibidos
        #nombre: nombre del edificio
        #numPisos: número de pisos del edificio
        #numLamparasT1, numLamparasT2 y numLamparasT3 corresponde a la cantidad de lámparas de tipo 1, 2 y 3 respectivamente en todo el edificio
        #detalleLamparaT1, detalleLamparaT2 y detalleLamparaT3 corresponde a una instancia cada uno con un objeto de tipo Lámpara que tiene la información de la misma
    
    def calcularLamparasEncendidas (self, horario, detalle):
        #-->Implementar aquí un método que calcule uno de los siguientes datos, dependiendo del valor de la variable detalle:
        #   - "cantidad": calcula la cantidad total de lámparas encendidas  
        #   - "cantidadT1": calcula la cantidad de lámparas de tipo 1 encendidas 
        #   - "cantidadT2": calcula la cantidad de lámparas de tipo 2 encendidas 
        #   - "cantidadT3": calcula la cantidad de lámparas de tipo 3 encendidas 
        #   - En caso de que el parámetro detalle tenga un valor distinto a los anteriores, deberá devolver un -1
        #Hay tres tipos de horarios: "matutino", "vespertino" y "nocturno". 
        #En horario matutino (de 7 a 14 horas), sólo un tercio de las lámparas de tipo 1 están encendidas. 
        #En horario vespertino (de 14 a 17 horas), todas las lámparas de tipo 1 están encendidas y un cuarto de las de tipo 2.
        #En horario nocturno (de 17 horas a 21:30 horas), todas las lámparas de tipos 2 y 3 están encendidas. 
        #Recuerde que no es posible encender 10.4 lámparas, por lo que deberá redondear hacia abajo siempre al valor entero correspondiente.
        #Deberá devolver siempre un número correspondiente al detalle solicitado. 
        return cantidadDeLamparas

    def calcularLumens (self, horario):
        #-->Implementar un método que calcula la cantidad de lumens emitididos en el edificio según la hora del día. Se siguen las mismas reglas que en el método anterior. 
        return lumensEmitidos    

    def calcularConsumoPorHora (self, precioWatt, hora):
        #-->Calcular en este método el consumo (en dinero) durante una hora del edificio de acuerdo a la cantidad de lámparas y a la hora del día. 
        #Suponga que la hora del día se representará como un número entero de 7 a 21. Fuera de ese horario el consumo por hora se considerará de cero. 
        #El precio por watt se recibirá por parámetro. 
        #La cantidad y tipos de lámparas encendidas dependerán de los atributos de la clase con dicha información y con las reglas descritas en el método anterior.
        #Es decir, puede invocar al método anterior para no tener que volver a realizar los mismos cálculos.  
        return consumoPorHora

    def calcularConsumoPorDia (self, precioWattMatutino, precioWattVespertino, precioWattNocturno):
        #-->Calcular aquí el consumo por día del edificio considerando la cantidad de lámparas, el consumo de cada una y un precio diferenciado
        #   de acuerdo a la hora del día. Suponga las reglas descritas anteriormente sobre la cantidad de lámparas encendidas de acuerdo a la hora.
        #Puede invocar métodos ya implementados. 
        return consumoPorDia  

class Lampara:

    def __init__ (self, modelo, lumens, wattsPorHora):
        #-->Iniciar aquí los atributos de una lámpara:
        #El modelo es una variable de tipo string que tiene el tipo de lámparas
        #lumens se refiere a la cantidad de lumens de la lámpara. Es un número entero mayor que cero. 
        #wattsPorHora es un número flotante con la cantidad de watts consumidos por hora por la lámpara. 

    def describirLampara (self):
        #-->Construye un string con los datos que describen la lámpara.
        #Importante: el string no se imprime, solo se construye y se retorna.
        return descripcion 

    def calcularCantidadDeLamparas (self, totalLumens):
        #-->Calcula la cantidad de lámparas de este tipo necesarias que emitan al menos la cantidad de lumens indicados en el parámetro totalLumens. 
        return cantidad

def main():
    # Aquí debe crear las instancias de al menos 3 tipos de lámparas. 
    # Solicite los datos al usuario en al menos una instancia
    # y convierta los datos numéricos correspondientes. 
    # Si desea con las otras instancias puede pasarle valores predefinidos

    # Aquí debe crear las instancias de al menos 2 edificios. 
    # Solicite los datos al usuario en al menos una de ellas y 
    # convierta los datos numéricos correspondientes. 
    # Debe usar las instancias de los tipos de lámparas creadas anteriormente. 

    # Invoque los métodos construidos tanto para las instancias de las lámparas como de los edificios e imprima los resultados. 
    # IMPORTANTE: este será el único lugar donde se permita usar la instrucción print. Es decir, ningún print deberá escribirse en los metodos de los objetos.
    #             Note como todos los métodos (a excepción de los constructores) retornan un valor. Ese valor retornado tendrá el tipo de la variable que se 
    #             devuelva. Es ese valor el que deberá imprimir aquí con los rótulos correspondientes.

    
if _name_ == "_main_":
	main()