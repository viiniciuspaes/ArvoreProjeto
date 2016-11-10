class Usuario:
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
    def setAnterior(self, usuario):
        self.anterior = usuario
    def setProximo(self, usuario):
        self.proximo = usuario
    def getPai(self):
        return self.pai
    def setPai(self, usuario):
        self.pai = usuario
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
        self.reservou = []

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
    def setAnterior(self, livro):
        self.anterior = livro
    def setProximo(self, livro):
        self.proximo = livro
    def getPai(self):
        return self.pai
    def setPai(self, livro):
        self.pai = livro
    def getCor(self):
        return self.cor
    def setCor(self,cor):
        self.cor=cor

a = ArvoreRB_Livro()
b = ArvoreRB_Usuario()

def cadastroLivro():
    titulo = #Pyqt dado1
    quantidade = # Pyqt dado2
    livro = Livro(titulo,quantidade)
    a.inserir(livro)

def cadastroUsuario():
    cpf = #Pyqt dado1
    nome = # Pyqt dado2
    usuario = Usuario(cpf,nome)
    b.inserir(usuario)

def descadastroLivro():
    titulo = #Pyqt dado1
    no = a.buscar(titulo)
    a.delete(no)

def descadastroUsuario():
    cpf = #Pyqt dado1
    no = b.buscar(cpf)
    b.delete(no)

def alugarLivro():
    tituloDesejado = #Pyqt dado1
    no = a.buscar(tituloDesejado)
    disp = no.getQuantidade()
    resev = no.isReservado()
    if disp == 0 and resev == False:
        print("Desculpe, mas o livro não está disponivel")
        print("Deseja reservar?(Y/N)")
        resposta = input()
        if resposta == "Y":

