import csv

class GestorCSV:
    def __init__(self, nombre):
        self.nombreArchivo  = nombre
        self.ptrArchivo     = None
        self.ptrArchivoCSV  = None
    
    def abrir (self, modo):
        self.ptrArchivo = open(self.nombreArchivo, modo)
        if modo == "w" or modo == "a":
            self.ptrArchivoCSV = csv.writer(self.ptrArchivo)
        else:
            self.ptrArchivoCSV = csv.reader(self.ptrArchivo)

    def cerrar (self):
        self.ptrArchivo.close()

    def escribir (self, lista):
        self.ptrArchivoCSV.writerows(lista)

    def leer (self):
        lres = []
        for i in self.ptrArchivoCSV:
            lres.append(i)
        return lres




i = GestorCSV("elementos.txt")
i.abrir("r")
lista = i.leer()
print(str(lista[0]).split(" "))
print(lista)
i.cerrar()