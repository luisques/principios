import random
import string
def seleccionarPalabraSecreta():
    lp = string.ascii_lowercase[:10]
    respuesta = ""
    for i in range(4):
        respuesta+=lp[random.randint(0,9)]
    return respuesta

def contarCoincidencias(palabraSecreta, intento):
    contador = 0
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i]==intento[i]:
            contador += 1
    return contador 

def jugarMastermind():
    ps = seleccionarPalabraSecreta()
    print (ps)
    intento = input("Digite la clave: ")
    while len(intento) != 4:
        intento = input("Digite la clave: ")
    cc = contarCoincidencias(ps, intento)
    print ("Tiene "+str(cc)+" coincidencias")
    numIntentos = 1
    while numIntentos <= 16 and cc != 4:
        intento = input("Digite la clave " + "(le quedan " + str(16-numIntentos) + " intentos): ")
        while len(intento) != 4:
            intento = input("Digite la clave " + "(le quedan " + str(16-numIntentos) + " intentos): ")
        cc = contarCoincidencias(ps, intento)
        print ("Tiene "+str(cc)+" coincidencias")
        numIntentos+=1
    if cc == 4:
        print ("Felicidades, ganó... ")
    else:
        print ("Felicidades, no ganó... ")



def main ():

    jugarMastermind()


if __name__ == "__main__":
    main()