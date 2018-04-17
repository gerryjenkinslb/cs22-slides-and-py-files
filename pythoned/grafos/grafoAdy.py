# Bradley N. Miller, David L. Ranum
# Solución de problemas con algoritmos y estructuras de datos usando Python
# Copyright 2014
#
#grafoAdy.py


import sys
import os

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0
        
    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice
    
    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices
    
    def agregarArista(self,de,a,costo=0):
            if de not in self.listaVertices:
                nv = self.agregarVertice(de)
            if a not in self.listaVertices:
                nv = self.agregarVertice(a)
            self.listaVertices[de].agregarVecino(self.listaVertices[a],costo)
    
    def obtenerVertices(self):
        return list(self.listaVertices.keys())
        
    def __iter__(self):
        return iter(self.listaVertices.values())
                
class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        self.color = 'blanco'
        self.dist = sys.maxsize
        self.predecesor = None
        self.desc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id
    
    def  agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion
        
    def asignarColor(self,color):
        self.color = color
        
    def asignarDistancia(self,d):
        self.dist = d

    def asignarPredecesor(self,p):
        self.predecesor = p

    def asignarDescubrimiento(self,tiempoDescubrimiento):
        self.desc = tiempoDescubrimiento
        
    def asignarFinalizacion(self,tiempoFinalizacion):
        self.fin = tiempoFinalizacion
        
    def obtenerFinalizacion(self):
        return self.fin
        
    def obtenerDescubrimiento(self):
        return self.desc
        
    def obtenerPredecesor(self):
        return self.predecesor
        
    def obtenerDistancia(self):
        return self.dist
        
    def obtenerColor(self):
        return self.color
    
    def obtenerConexiones(self):
        return self.conectadoA.keys()
        
    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":desc " + str(self.desc) + ":fin " + str(self.fin) + ":distancia " + str(self.dist) + ":predecesor \n\t[" + str(self.predecesor)+ "]\n"
    
    def obtenerId(self):
        return self.id
