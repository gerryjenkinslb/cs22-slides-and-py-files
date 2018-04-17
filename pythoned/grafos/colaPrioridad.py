# Bradley N. Miller, David L. Ranum
# Solución de problemas con algoritmos y estructuras de datos usando Python
# Copyright 2014
# 
#colaPrioridad.py

class ColaPrioridad:
    def __init__(self):
        self.arregloMonticulo = [(0,0)]
        self.tamanoActual = 0

    def construirMonticulo(self,unaLista):
        self.tamanoActual = len(unaLista)
        self.arregloMonticulo = [(0,0)]
        for i in unaLista:
            self.arregloMonticulo.append(i)
        i = len(unaLista) // 2            
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
                        
    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.arregloMonticulo[i][0] > self.arregloMonticulo[hm][0]:
                tmp = self.arregloMonticulo[i]
                self.arregloMonticulo[i] = self.arregloMonticulo[hm]
                self.arregloMonticulo[hm] = tmp
            i = hm
                
    def hijoMin(self,i):
        if i*2 > self.tamanoActual:
            return -1
        else:
            if i*2 + 1 > self.tamanoActual:
                return i*2
            else:
                if self.arregloMonticulo[i*2][0] < self.arregloMonticulo[i*2+1][0]:
                    return i*2
                else:
                    return i*2+1

    def infiltArriba(self,i):
        while i // 2 > 0:
            if self.arregloMonticulo[i][0] < self.arregloMonticulo[i//2][0]:
               tmp = self.arregloMonticulo[i//2]
               self.arregloMonticulo[i//2] = self.arregloMonticulo[i]
               self.arregloMonticulo[i] = tmp
            i = i//2
 
    def insertar(self,k):
        self.arregloMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def eliminarMin(self):
        valorSacado = self.arregloMonticulo[1][1]
        self.arregloMonticulo[1] = self.arregloMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.arregloMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
        
    def estaVacia(self):
        if self.tamanoActual == 0:
            return True
        else:
            return False

    def decrementarClave(self,valor,nuevo):
        hecho = False
        i = 1
        miClave = 0
        while not hecho and i <= self.tamanoActual:
            if self.arregloMonticulo[i][1] == valor:
                hecho = True
                miClave = i
            else:
                i = i + 1
        if miClave > 0:
            self.arregloMonticulo[miClave] = (nuevo,self.arregloMonticulo[miClave][1])
            self.infiltArriba(miClave)
            
    def __contains__(self,vertice):
        for pareja in self.arregloMonticulo:
            if pareja[1] == vertice:
                return True
        return False     

