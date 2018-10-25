#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Matriz:

	def __init__ (self, filas, columnas):
		self.matriz = self.crearMatriz(filas,columnas)

	def crearMatriz(self, filas, columnas):
		matriz = [0] * filas
		for i in range(len(matriz)):
			matriz[i] = [(i*columnas)+j for j in range(1,columnas+1)]
		return matriz

	def imprimir(self):
		contenido = ""
		matriz = self.matriz
		for f in range(len(matriz)):
			for c in range(len(matriz[f])):
				contenido += (str(matriz[f][c]) + "\t")
			contenido+="\n"
		return contenido

	def getColumna(self, columna):
		arregloColumna = []
		for i in range(len(self.matriz)):
			arregloColumna.append(matriz[i][columna])

		return arregloColumna

	def getFila(self, fila):
		return self.matriz[fila]

	def __str__(self):
		return self.imprimir()

matriz = Matriz(4,4)
print(matriz)