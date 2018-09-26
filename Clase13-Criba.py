# -*- coding: utf-8 -*-
def cribaEratostenes(lista):
    #Requiere: Lista de números enteros
    #Retorna: Lista de números primos
    p = 0
    lres = []
    for i in range(len (lista)):
        if (lista[p]!=0):
            lres.append(lista[p])
        if (lista[p] != 0):
            for j in range(p,len(lista),lista[p]):
                lista[j]= 0
        p+=1
    return lres



def main():
    n = input("Digite un entero: ")
    lista = range (2, int(n)+1)
    #si usa python 3, cambie la instrucciones anterior por:
    #lista = [i for i in range (2, int(n)+1)]

    print (cribaEratostenes(lista))



if __name__ == "__main__":

    main ()


