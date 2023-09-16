from metodoamstract import Expression
from math import *
class Operaciones_un_valor(Expression):
    def __init__(self, valor1,tipo,fila,columna):
        self.valor1 = valor1
        self.tipo = tipo
        super().__init__(fila,columna)

    def operar(self,arbol):
        if self.valor1:
            num = self.valor1.operar(arbol)
            operacion= self.tipo.operar(arbol)
            if operacion == 'seno':
                return sin(num)
            elif operacion == 'coseno':
                return cos(num)
            elif operacion == 'tangente':
                return tan(num)
        return None

        
    def getFila(self):
        return super().getFila
    
    def getColumna(self):
        return super().getColumna