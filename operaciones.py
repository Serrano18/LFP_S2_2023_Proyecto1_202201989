
from ClasePadre import Padre

class Operaciones(Padre):
    def __init__(self, valor1,valor2,tipo,fila,columna):
        self.valor1 = valor1
        self.valor2 = valor2
        self.tipo = tipo
        super().__init__(fila,columna)

    def funcionToken(self):
        num1=''
        num2=''
        operacion=self.tipo.funcionToken()
        if self.valor1!=None:
            num1=self.valor1.funcionToken()
        if self.valor2!=None:
            num2=self.valor2.funcionToken()
        #Realizar las operaciones
        if operacion == 'suma':
            return num1 + num2
        elif operacion == 'resta':
            return num1 - num2
        elif operacion == 'multiplicacion':
            return num1 * num2
        elif operacion == 'division':
            return num1 / num2
        elif operacion == 'potencia':
            return  num1 ** num2
        elif operacion == 'raiz':
            return num1 ** (1/num2)
        elif operacion == 'mod':
            return num1 % num2
        else:
            return 0
    
    def getFila(self):
        return super().getFila
    
    def getColumna(self):
        return super().getColumna
        
    def getValor1(self):
        return self.valor1

    def getValor2(self):
        return self.valor2
    
    def getTipo(self):
        return self.tipo