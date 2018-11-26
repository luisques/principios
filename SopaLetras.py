class SopaDeLetras:

  def __init__(self, sopa, lista):
    self.sopa = sopa
    self.lista = lista
    self.direccionF = [-1,-1,0,1,1,1,0,-1]
    self.direccionC = [0,1,1,1,0,-1,-1,-1]

  def buscarPalabra(self, palabra):
    palabra = palabra.upper()
    resultado = palabra + " no se encuentra en la sopa"
    for fila in range(len(self.sopa)):
      for columna in range(len(self.sopa[fila])):
        if(palabra[0] == self.sopa[fila][columna]):
          encontrado = self.buscarPalabraEnLasDirecciones(fila, columna, palabra)
          if(encontrado[0]):
            resultado = (
              palabra + " encontrada, inicia en: "+ str(fila) +" "+ str(columna) + " y termina en: " + 
              str(fila+(self.direccionF[encontrado[1]]*len(palabra))) + " " + 
              str(columna+(self.direccionC[encontrado[1]]*len(palabra)))
            )
            
    return resultado

  def estaEnLosLimitesDeLaMatriz(self, f,c):
    return  (f >= 0 and 
            c >= 0 and 
            f < len(self.sopa) and 
            c < len(self.sopa[f]))

  def buscarPalabraEnLasDirecciones(self, fila, columna, palabra):
    exito = False
    dF = [-1,-1,0,1,1,1,0,-1]
    dC = [0,1,1,1,0,-1,-1,-1]     
    direcciones = 0
    direccionExito = -1
    while(direcciones < 8 ):
      letraEncontrada = True
      if(self.estaEnLosLimitesDeLaMatriz(fila+dF[direcciones], columna+dC[direcciones]) and
        self.sopa[fila+dF[direcciones]][columna+dC[direcciones]] == palabra[1]
      ):
        letraEncontrada = True
        letrasEncontradas = 1
        filaT = fila
        columnaT = columna
        while(letraEncontrada and  letrasEncontradas < len(palabra) ):
              
          if( self.estaEnLosLimitesDeLaMatriz(filaT+dF[direcciones], columnaT+dC[direcciones]) and
            palabra[letrasEncontradas] == self.sopa[filaT + dF[direcciones]][columnaT + dC[direcciones]]):
            letrasEncontradas += 1
            filaT += dF[direcciones]
            columnaT += dC[direcciones]
          else:
            letraEncontrada = False

          if(letrasEncontradas >= len(palabra)):
            exito = True
            direccionExito = direcciones

      direcciones+= 1

    return [exito, direccionExito]

  def resolverSopa(self):
    resultados = []
    for palabra in self.lista:
      resultados.append(self.buscarPalabra(palabra))
    return "\n".join(resultados)

def main():
  lista1 = ["WWWWW", "WCSWW", "WWAWW", "WWLSW", "WAISA"]
  lista2 = ["SAL", "ASIA", "PAPEL", "CASA"]
  sopaI = SopaDeLetras(lista1,lista2)
  resultado = sopaI.resolverSopa()
  print(resultado)

if __name__ == "__main__":
  main()