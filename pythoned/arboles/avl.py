# Bradley N. Miller, David L. Ranum
# Solución de problemas con algoritmos y estructuras de datos usando Python
# Copyright 2014
#
#avl.py

from .abb import ArbolBinarioBusqueda, NodoArbol

class ArbolAVL(ArbolBinarioBusqueda):

    def _agregar(self,clave,valor,nodoActual):
    	if clave < nodoActual.clave:
    	    if nodoActual.tieneHijoIzquierdo():
    		self._agregar(clave,valor,nodoActual.hijoIzquierdo)
    	    else:
    		nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
    		self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
    	else:
    	    if nodoActual.tieneHijoDerecho():
    		self._agregar(clave,valor,nodoActual.hijoDerecho)
    	    else:
    		nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
    		self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def actualizarEquilibrio(self,nodo):
    	if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
    	    self.reequilibrar(nodo)    
    	    return
    	if nodo.padre != None:
    	    if nodo.esHijoIzquierdo():
    		    nodo.padre.factorEquilibrio += 1
    	    elif nodo.esHijoDerecho():
    		    nodo.padre.factorEquilibrio -= 1

    	    if nodo.padre.factorEquilibrio != 0:
    		    self.actualizarEquilibrio(nodo.padre)

    def reequilibrar(self,nodo):
        if nodo.factorEquilibrio < 0:
	    if nodo.hijoDerecho.factorEquilibrio > 0:
	        self.rotarDerecha(nodo.hijoDerecho)
	        self.rotarIzquierda(nodo)
	    else:
	        self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
	    if nodo.hijoIzquierdo.factorEquilibrio < 0:
	        self.rotarIzquierda(nodo.hijoIzquierdo)
	        self.rotarDerecha(nodo)
	     else:
	        self.rotarDerecha(nodo)
           
    def rotarIzquierda(self,rotRaiz):
    	nuevaRaiz = rotRaiz.hijoDerecho
    	rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
    	if nuevaRaiz.hijoIzquierdo != None:
    	    nuevaRaiz.hijoIzquierdo.padre = rotRaiz
    	nuevaRaiz.padre = rotRaiz.padre
    	if rotRaiz.esRaiz():
    	    self.raiz = nuevaRaiz
    	else:
    	    if rotRaiz.esHijoIzquierdo():
    	        rotRaiz.padre.hijoIzquierdo = nuevaRaiz
    	    else:
    	    	rotRaiz.padre.hijoDerecho = nuevaRaiz
    	nuevaRaiz.hijoIzquierdo = rotRaiz
    	rotRaiz.padre = nuevaRaiz
    	rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
    	nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

    def rotarDerecha(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + min(rotRaiz.factorEquilibrio, 0)  

