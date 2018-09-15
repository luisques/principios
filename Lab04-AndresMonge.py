#Andrés Monge Zúñiga
#14/09/18
#Laboratorio -4

def obtenerPrecioDePesoEnKilos (pesoKilos):
    if(0.01 <= pesoKilos <= 0.99):
        tarifaDolares = pesoKilos * 9.30 
    elif(1.00 <= pesoKilos <= 4.99):
        tarifaDolares = pesoKilos * 15.45
    elif(5.00 <= pesoKilos <= 9.99):
        tarifaDolares = pesoKilos * 25.85
    elif(10.00 <= pesoKilos <= 14.99):
        tarifaDolares = pesoKilos * 50.15
    elif(15.00 <= pesoKilos < 16.00):
        tarifaDolares = pesoKilos * 65
    elif(pesoKilos >= 16.00):
        tarifaDolares = 65 + (2.27*(pesoKilos -15.00))
    return tarifaDolares

def obtenerImpuestosDelProducto (tipo):
    if(tipo == "Artículo electrónico"):
        impuesto = 0.13
    elif(tipo == "Libro"):
        impuesto = 0.01
    elif(tipo == "Ropa"):
        impuesto = 0.29
    elif(tipo == "Instrumento Musical"):
        impuesto = 0.27
    else:
        impuesto = 0.21
    return impuesto
    
def calcularFlete (tipo, pesoKilos, valorProducto):
    flete = valorProducto + obtenerPrecioDePesoEnKilos(pesoKilos) + (valorProducto + (pesoKilos * 0.10)) * obtenerImpuestosDelProducto(tipo)
    return flete

def main():

    print(obtenerPrecioDePesoEnKilos(25))  
    print(obtenerImpuestosDelProducto("Libro"))
    print(calcularFlete("Ropa", 0.25, 5))
    
if __name__=="__main__":
    main()
    
    