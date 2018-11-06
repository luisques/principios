# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:21:20 2018

@author: Gabriel Araya
"""
def toString (resultado):
    contenido=""
    for g in range(len(resultado)):
            for x in range(len(resultado[g])):
                contenido+=(str(resultado[g][x]) + "\t")
            contenido +="\n"
    return contenido

def multiplicarMatriz(X,Y):
    
    resultado=[0]*len(X)
    
    for i in range(len(X)):
        resultado[i]=[0]*len(X[0])


    for j in range(len(X)):
        for c in range(len(Y[0])):
            for k in range(len(Y)):
                resultado[j][c]+=X[j][k]*Y[k][c]
    
    
    return resultado

print(toString((multiplicarMatriz([[1,1],[1,1]],[[1,1],[1,21]]))))

l = [1,0,-1]
for i in range(1,-2,-1):
    print (i)