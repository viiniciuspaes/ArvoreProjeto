class NoHash:
    def __init__(self,valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None
        self.pai = None
        self.cor = "preto"

    # -------------------Gets and Sets--------------------------

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
    def getCor(self):
        return self.cor
    def setCor(self,cor):
        self.cor=cor


class ArvoreRB:
    def __init__(self):
        self.raiz = None
        #self.null = NoHash(None) #nao sei se sera necessario criar um ponteiro para um No preto null

    def add(self,no):
        if self.raiz == None:
            self.raiz= no
        else:
            self.inserir(no)

    def inserir(self, no):
        auxiliar = None
        noLocal = self.raiz
        while noLocal != None:
            auxiliar = noLocal
            if no.getValor() < noLocal.getValor():
                noLocal = noLocal.getAnterior()
            else:
                noLocal = noLocal.getProximo()
        no.setPai(auxiliar)
        if auxiliar == None:
            self.raiz=no
        elif no.getValor() < auxiliar.getValor():
            auxiliar.setAnterior(no)
        else:
            auxiliar.setProximo(no)
        no.setCor("vermelho")
        self.inserirFix(no)

    def inserirFix(self, no):
        while no.getPai().getCor() == "vermelho":
            if no.getPai() ==  no.getPai().getPai().getAnterior():
                auxiliar = no.getPai().getPai().getProximo()
                if auxiliar.getCor() ==  "vermelho":
                    no.getPai().setCor("preto")
                    auxiliar.setCor("preto")
                    no.getPai().getPai().setCor("vermelho")
                    no = no.getPai().getPai()
                else:
                    if no == no.getPai().getProximo():
                        no = no.getPai()
                        self.rotEsq(no)
                    no.getPai().setCor("preto")
                    no.getPai().getPai().setCor("vermelho")
                    self.rotDir(no.getPai().getPai())
            else:
                auxiliar = no.getPai().getPai().getAnterior()
                if auxiliar.getCor() == "vermelho":
                    no.getPai().setCor("preto")
                    auxiliar.setCor("preto")
                    no.getPai().getPai().setCor("vermelho")
                    no = no.getPai().getPai()
                else:
                    if auxiliar == auxiliar.getPai().getAnterior():
                        no = no.getPai()
                        self.rotDir(no)
                    no.getPai().setCor("preto")
                    no.getPai().getPai().setCor("vermelho")
                    self.rotEsq(no.getPai().getPai())
        self.raiz.setCor("preto")

    def rotEsq(self, no):
        noRotacionado = no.getProximo()
        no.setProximo(noRotacionado.getAnterior())
        noRotacionado.getAnterior().setPai(no)
        noRotacionado.setPai(no.getPai())
        if no.getPai() == None:
            self.raiz = noRotacionado
        elif no == no.getPai().getAnterior():
            no.getPai().setAnterior(noRotacionado)
        else:
            no.getPai().setProximo(noRotacionado)
        noRotacionado.setAnterior(no)
        no.setPai(noRotacionado)

    def rotDir(self,no):
        noRotacionado = no.getPai()
        noRotacionado.setAnterior(no.getProximo())
        no.setProximo(noRotacionado)
        noRotacionado.getAnterior().setPai(noRotacionado)
        no.setPai(noRotacionado.getPai())
        noRotacionado.setPai(no)
        if no.getPai() == None:
            self.raiz = no
        #falta ?
