class Nodo:
    def __init__(self, valor):
        self.valor= valor
        self.padre= None
        self.hijos= []
        self.hijo1= None
        self.hijo2= None
        self.hijo3= None
        self.color= None
        self.hijosAzules= []
        self.hijosRojos= []
    def __repr__(self):
        return f"Nodo {self.valor}"

class arbol:
    def __init__(self, tamaño):
        self.nodos = []
        self.raiz= Nodo("Dummy")
        padre = self.raiz
        hijo= Nodo(tamaño)
        padre.hijos.append(hijo)
        padre.hijo1 = hijo
        hijo.padre= padre
        padre= self.raiz.hijo1
        self.agregarNodos(tamaño,padre)
        self.colorear()
        self.hijosColores()
        
                
    def agregarNodos(self, valor, padre):
        self.nodos.append(padre)
        if padre.valor-1>=0:
            hijo = Nodo(valor-1)
            padre.hijos.append(hijo)
            padre.hijo1= hijo
            hijo.padre = padre
            self.agregarNodos(valor-1,padre.hijo1)
        if padre.valor-2>=0:
            hijo = Nodo(valor-2)
            padre.hijos.append(hijo)
            padre.hijo2= hijo
            hijo.padre = padre
            self.agregarNodos(valor-2,padre.hijo2)
        if padre.valor-3>=0:
            hijo = Nodo(valor-3)
            padre.hijos.append(hijo)
            padre.hijo3= hijo
            hijo.padre = padre
            self.agregarNodos(valor-3,padre.hijo3)
        if padre.valor==0:
            if self.profundidad(padre)%2==0:
                padre.color= "rojo"
            else:
                padre.color= "azul"
    
    def profundidad(self,nodo):
        prof = 0
        while nodo.padre:
            prof+= 1
            nodo=nodo.padre
        return prof-1
    
    def colorear(self):
        for nodo in self.nodos[::-1]:
            if nodo.hijo1:
                if nodo.hijo1.color=="azul":
                    nodo.color="azul"
                    continue
                else:
                    nodo.color="rojo"
            if nodo.hijo2:
                if nodo.hijo2.color=="azul":
                    nodo.color="azul"
                    continue
                else:
                    nodo.color="rojo"
            if nodo.hijo3:
                if nodo.hijo3.color=="azul":
                    nodo.color="azul"
                    continue
                else:
                    nodo.color="rojo"
    
    def hijosColores(self):
        for nodo in self.nodos:
            if nodo.hijo1:
                if nodo.hijo1.color=="azul":
                    nodo.hijosAzules.append(nodo.hijo1)
                else:
                    nodo.hijosRojos.append(nodo.hijo1)
            if nodo.hijo2:
                if nodo.hijo2.color=="azul":
                    nodo.hijosAzules.append(nodo.hijo2)
                else:
                    nodo.hijosRojos.append(nodo.hijo2)
            if nodo.hijo3:
                if nodo.hijo3.color=="azul":
                    nodo.hijosAzules.append(nodo.hijo3)
                else:
                    nodo.hijosRojos.append(nodo.hijo3)