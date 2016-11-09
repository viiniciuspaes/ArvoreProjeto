class Aluno:
    def __init__(self, cpf, nome):
        self.valor = cpf
        self.anterior = None
        self.proximo = None
        self.pai = None
        self.cor = "preto"
        self.nome = nome
        self.alugou = []

    def getValor(self):
        return self.valor
    def setValor(self,valor):
        self.valor=valor
    def getNome(self):
        return self.nome
    def getAlugados(self):
        return self.alugou
    def addAlugados(self,livro):
        self.alugou.append(livro)
    def removerAlugado(self,livro):
        self.alugou.remove(livro)
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
    def getCor(self):
        return self.cor
    def setCor(self,cor):
        self.cor=cor

class Livro:
    def __init__(self,nome,quantidade):
        self.valor = nome
        self.anterior = None
        self.proximo = None
        self.pai = None
        self.cor = "preto"
        self.quantidade = quantidade
        self.reservado = False
        #self.alugado = False
        self.alugou = []

    def getValor(self):
        return self.valor
    def setValor(self,valor):
        self.valor=valor
    def getQuantidade(self):
        return self.quantidade
    def mudarQuantidade(self,numero):
        self.quantidade= self.quantidade + numero
    def isReservado(self):
        return self.reservado
    def getAlugados(self):
        return self.alugou
    def addAlugado(self,aluno):
        self.alugou.append(aluno)
    def removeAlugado(self,aluno):
        self.alugou.remove(aluno)
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
    def getCor(self):
        return self.cor
    def setCor(self,cor):
        self.cor=cor