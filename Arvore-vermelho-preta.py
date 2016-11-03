class NoHash:
    def __init__(self,valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None
        self.pai = None
        self.cor = None

    def getValor(self):
        return self.valor
    def getAnterior(self):
        return self.anterior
    def getProximo(self):
        return self.proximo
    def setAnterior(self,no):
        self.anterior = no
    def setProximo(self,no):
        self.proximo = no
    def getPai(self):
        return self.pai
    def setPai(self,no):
        self.pai = no