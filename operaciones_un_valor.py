
from ClasePadre import Padre
from math import *
class Operaciones_un_valor(Padre):
    def __init__(self, valor1,tipo,fila,columna):
        self.valor1 = valor1
        self.tipo = tipo
        super().__init__(fila,columna)

    def funcionToken(self):
        if self.valor1:
            num = self.valor1.funcionToken()
            operacion= self.tipo.funcionToken()
            if operacion == 'seno':
                return sin(num)
            elif operacion == 'coseno':
                return cos(num)
            elif operacion == 'tangente':
                return tan(num)
            elif operacion == 'inverso':
                return 1 / num
        return None

        
    def getFila(self):
        return super().getFila
    
    def getColumna(self):
        return super().getColumna
    