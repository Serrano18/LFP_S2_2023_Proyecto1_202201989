from metodoamstract import Expression

class Palabra(Expression):
    
    def __init__(self,palabra,fila,columna):
        self.palabra = palabra
        super().__init__(fila,columna)

    def operar(self, arbol):
        return self.palabra
    
    def getFila(self):
        return super().getFila
    
    def getColumna(self):
        return super().getColumna
    
    def getPalabra(self):
        return self.palabra