# Bradley N. Miller, David L. Ranum
# Solución de problemas con algoritmos y estructuras de datos usando Python
# Copyright 2014
# 
#monticuloBinario.py

class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def construirMonticulo(self,unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        print(len(self.listaMonticulo), i)
        while (i > 0):
            print(self.listaMonticulo, i)
            self.infiltAbajo(i)
            i = i - 1
        print(self.listaMonticulo,i)
                        
    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
                
    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def infiltArriba(self,i):
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i//2]:
               tmp = self.listaMonticulo[i // 2]
               self.listaMonticulo[i // 2] = self.listaMonticulo[i]
               self.listaMonticulo[i] = tmp
            i = i // 2
 
    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
        
    def estaVacio(self):
        if tamanoActual == 0:
            return True
        else:
            return False
