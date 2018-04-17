# Bradley N. Miller, David L. Ranum
# Solución de problemas con algoritmos y estructuras de datos usando Python
# Copyright 2014
# 
#arbolBinario.py

class ArbolBinario:
    def __init__(self,objetoRaiz):
        self.clave = objetoRaiz
        self.hijoIzquierdo = None
        self.hijoDerecho = None
    
    def insertarIzquierdo(self,nuevoNodo):
        if self.hijoIzquierdo == None:
            self.hijoIzquierdo = ArbolBinario(nuevoNodo)
        else:  
            t = ArbolBinario(nuevoNodo)
            t.hijoIzquierdo = self.hijoIzquierdo
            self.hijoIzquierdo = t

    def insertarDerecho(self,nuevoNodo):
        if self.hijoDerecho == None:
            self.hijoDerecho = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.hijoDerecho = self.hijoDerecho
            self.hijoDerecho = t

    def esHoja(self):
        return ((not self.hijoIzquierdo) and (not self.hijoDerecho))

    def obtenerHijoDerecho(self):
        return self.hijoDerecho
    
    def obtenerHijoIzquierdo(self):
        return self.hijoIzquierdo
    
    def asignarValorRaiz(self,obj):
        self.clave = obj

    def obtenerValorRaiz(self):
        return self.clave

    def inorden(self):
        if self.hijoIzquierdo:
            self.hijoIzquierdo.inorden()
        print(self.clave)
        if self.hijoDerecho:
            self.hijoDerecho.inorden()

    def postorden(self):
        if self.hijoIzquierdo:
            self.hijoIzquierdo.postorden()
        if self.hijoDerecho:
            self.hijoDerecho.postorden()
        print(self.clave)

    def preorden(self):
        print(self.clave)
        if self.hijoIzquierdo:
            self.hijoIzquierdo.preorden()
        if self.hijoDerecho:
            self.hijoDerecho.preorden()

    def imprimirExpresion(self):
        if self.hijoIzquierdo:
            print('(', end=' ')
            self.hijoIzquierdo.imprimirExpresion()
        print(self.clave, end=' ')
        if self.hijoDerecho:
            self.hijoDerecho.imprimirExpresion()
            print(')', end=' ')

    def evalPostorden(self):
        opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        res1 = None
        res2 = None
        if self.hijoIzquierdo:
            res1 = self.hijoIzquierdo.evalPostorden()  #// \label{peleft}
        if self.hijoDerecho:
            res2 = self.hijoDerecho.evalPostorden() #// \label{peright}
        if res1 and res2:
            return opers[self.clave](res1,res2) #// \label{peeval}
        else:
            return self.clave

def inorden(arbol):
    if arbol != None:
        inorden(arbol.obtenerHijoIzquierdo())
        print(arbol.obtenerValorRaiz())
        inorden(arbol.obtenerHijoDerecho())

def imprimirExpresion(arbol):
    if arbol.hijoIzquierdo:
        print('(', end=' ')
        imprimirExpresion(arbol.obtenerHijoIzquierdo())
    print(arbol.obtenerValorRaiz(), end=' ')
    if arbol.hijoDerecho:
        imprimirExpresion(arbol.obtenerHijoDerecho())
        print(')', end=' ') 

def imprimirExpresion(arbol):
  valorCadena = ""
  if arbol:
      valorCadena = '(' + imprimirExpresion(arbol.obtenerHijoIzquierdo())
      valorCadena = valorCadena + str(arbol.obtenerValorRaiz())
      valorCadena = valorCadena + imprimirExpresion(arbol.obtenerHijoDerecho())+')'
  return valorCadena

def evalPostorden(arbol):
    operadores = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if arbol:
        res1 = evalPostorden(arbol.obtenerHijoIzquierdo()) #// \label{peleft}
        res2 = evalPostorden(arbol.obtenerHijoDerecho())  #// \label{peright}
        if res1 and res2:
            return operadores[arbol.obtenerValorRaiz()](res1,res2) #// \label{peeval}
        else:
            return arbol.obtenerValorRaiz()

def altura(arbol):
    if arbol == None:
        return -1
    else:
        return 1 + max(altura(arbol.hijoIzquierdo),altura(arbol.hijoDerecho))

t = ArbolBinario(7)
t.insertarIzquierdo(3)
t.insertarDerecho(9)
inorden(t)
import operator
x = ArbolBinario('*')
x.insertarIzquierdo('+')
l = x.obtenerHijoIzquierdo()
l.insertarIzquierdo(4)
l.insertarDerecho(5)
x.insertarDerecho(7)
print(imprimirExpresion(x))
print(evalPostorden(x))
print(altura(x))
