# -*- coding: utf-8 -*-
#Jose Antonio Ciccio
#Modificado por Luis Quesada 


class Edificio:

  def __init__ (self, nombre, numPisos, numLamparasT1, numLamparasT2, numLamparasT3, detalleLamparaT1, detalleLamparaT2, detalleLamparaT3):
    self.nombre             = nombre            #string
    self.numPisos           = numPisos          #int
    self.numLamparasT1      = numLamparasT1     #int
    self.numLamparasT2      = numLamparasT2     #int
    self.numLamparasT3      = numLamparasT3     #int
    self.instanciaLamparaT1 = detalleLamparaT1  #Lampara
    self.instanciaLamparaT2 = detalleLamparaT2  #Lampara
    self.instanciaLamparaT3 = detalleLamparaT3  #Lampara
  
  def calcularLamparasEncendidas (self, horario, detalle):
    # horario: "matutino", "vespertino" y "nocturno".
    # detalle: "cantidad", "cantidadT1", "cantidadT2", "cantidadT3"
    lamparasT1 = 0
    lamparasT2 = 0
    lamparasT3 = 0
    cantidadDeLamparas = 0

    if (horario == "matutino"):
      lamparasT1 = self.numLamparasT1 // 3
    elif(horario == "vespertino"):
      lamparasT1 = self.numLamparasT1
      lamparasT2 = self.numLamparasT2 // 4
    elif(horario == "nocturno"):
      lamparasT2 = self.numLamparasT2
      lamparasT3 = self.numLamparasT3

    if(detalle == "cantidad"):
      cantidadDeLamparas = lamparasT1 + lamparasT2 + lamparasT3
    elif(detalle == "cantidadT1"):
      cantidadDeLamparas = lamparasT1
    elif(detalle == "cantidadT2"):
      cantidadDeLamparas = lamparasT2
    elif(detalle == "cantidadT3"):
      cantidadDeLamparas = lamparasT3


    return cantidadDeLamparas

def calcularLamparasEncendidas2 (self, horario, detalle):
    # horario: "matutino", "vespertino" y "nocturno".
    # detalle: "cantidad", "cantidadT1", "cantidadT2", "cantidadT3"
    cantidadDeLamparas = -1

    if (horario == "matutino"):
      if (detalle == "cantidad" or detalle == "cantidadT1"):
        cantidadDeLamparas = self.numLamparasT1 // 3
      else:
        cantidadDeLamparas = 0
    elif(horario == "vespertino"):
      if (detalle == "cantidad"):
        cantidadDeLamparas = self.numLamparasT1 + self.numLamparasT2 // 4
      elif (detalle == "cantidadT1"):
        cantidadDeLamparas = self.numLamparasT1
      elif (detalle == "cantidadT2"):
        cantidadDeLamparas = self.numLamparasT2 // 4
      else: 
        cantidadDeLamparas = 0
    elif(horario == "nocturno"):
       if (detalle == "cantidad"):
        cantidadDeLamparas = self.numLamparasT2 + self.numLamparasT3
      elif (detalle == "cantidadT1"):
        cantidadDeLamparas = 0
      elif (detalle == "cantidadT2"):
        cantidadDeLamparas = self.numLamparasT2 
      else: 
        cantidadDeLamparas = self.numLamparasT3 
    return cantidadDeLamparas


  def calcularLumens (self, horario):

    # horario -> hay tres distintos : "matutino", "vespertino" y "nocturno".
    cantidadLamparasT1 = self.calcularLamparasEncendidas(horario, "cantidadT1")
    cantidadLamparasT2 = self.calcularLamparasEncendidas(horario, "cantidadT2")
    cantidadLamparasT3 = self.calcularLamparasEncendidas(horario, "cantidadT3")

    lumensEmitidos = cantidadLamparasT1 * self.instanciaLamparaT1.lumens + cantidadLamparasT2 * self.instanciaLamparaT2.lumens + cantidadLamparasT3 * self.instanciaLamparaT3.lumens 
    return lumensEmitidos    

  def calcularConsumoPorHora (self, precioWatt, hora):

    consumoPorHora = 0
    if (hora >= 7 and hora <= 21):

      horario = ""
      if (hora >=7 and hora < 14):
        horario = "matutino"
      elif (hora >=14 and hora < 17):
        horario = "vespertino"
      elif (hora >=17 and hora <= 21):
        horario = "nocturno"

      cantidadLamparasT1 = self.calcularLamparasEncendidas(horario, "cantidadT1")
      consumoPorHora += (cantidadLamparasT1 * self.instanciaLamparaT1.wattsPorHora * precioWatt)

      cantidadLamparasT2 = self.calcularLamparasEncendidas(horario, "cantidadT2")
      consumoPorHora += (cantidadLamparasT2 * self.instanciaLamparaT2.wattsPorHora * precioWatt)

      cantidadLamparasT3 = self.calcularLamparasEncendidas(horario, "cantidadT3")
      consumoPorHora += (cantidadLamparasT3 * self.instanciaLamparaT3.wattsPorHora * precioWatt)

    else:
      consumoPorHora = 0

    return consumoPorHora

  def calcularConsumoPorDia (self, precioWattMatutino, precioWattVespertino, precioWattNocturno):

    horasMatutinas = self.calcularConsumoPorHora(precioWattMatutino, 7) * 7
    horasVespertinas = self.calcularConsumoPorHora(precioWattVespertino, 15) * 3
    horasNocturnas = self.calcularConsumoPorHora(precioWattNocturno, 18) * 5

    return horasMatutinas + horasVespertinas + horasNocturnas

class Lampara:

  def __init__ (self, modelo, lumens, wattsPorHora):
    self.modelo = modelo
    if (lumens > 0):
      self.lumens = lumens
    else:
      self.lumens = 0
    self.wattsPorHora = wattsPorHora

  def describirLampara (self):
    descripcion = "Lampara: " + self.modelo + " lumens: " + str(self.lumens) + " Watts por hora: " + str(self.wattsPorHora)
    return descripcion 

  def calcularCantidadDeLamparas (self, totalLumens):
    # 80 lumens
    # quiero 801
    # => necesito 11 lamparas
    cantidadLamparas = (totalLumens // self.lumens) + 1
    return cantidadLamparas


def main():

  l1 = Lampara("T1", 100, 1000)
  l2 = Lampara("T2", 125, 1175)
  l3 = Lampara("T3", 163, 1374)

  e1 = Edificio("Acobo", 7, 35, 50, 80, l1,l2,l3)
  e2 = Edificio("Equus", 13, 15, 90, 160, l1,l2,l3)
  
  print(l1.describirLampara())
  print(l2.describirLampara())
  print(l3.describirLampara())

  print(e1.calcularLamparasEncendidas("matutino", "cantidad"))
  print(e1.calcularLamparasEncendidas("vespertino", "cantidadT2"))
  print(e1.calcularLamparasEncendidas("nocturno", "cantidadT3"))
    
if __name__ == "__main__":
	main()
