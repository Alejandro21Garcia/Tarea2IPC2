import re
from nodo import Nodo

class ListaCircularDE:
    def __init__(self):
        
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return True
        else: 
            False
    
    def agregarInicio(self, num):
        if self.vacia():
            self.primero = self.ultimo = Nodo(num)
        else:
            aux = Nodo(num)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.unirNodos()

    def  agregarFinal(self, num):
        if self.vacia():
            self.primero = self.ultimo = Nodo(num)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(num)
            self.ultimo.anterior = aux

    def unirNodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def recorerIF(self):
        aux = self.primero
        while aux:
            print(aux.num)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorerFI(self):
        aux = self.ultimo
        while aux:
            print(aux.num)
            aux = aux.anterior
            if aux == self.ultimo:
                break

    def buscar(self, num):
        aux = self.primero
        while aux:
            if aux.num == num:
                print('Anterior: ', aux.anterior.num )
                print('Siguinte: ', aux.siguiente.num)
                return print('Actual:', num)
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False
                