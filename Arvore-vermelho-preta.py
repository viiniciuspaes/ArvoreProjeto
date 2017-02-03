class No:
    def __init__(self,valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None
        self.pai = None
        self.cor = "preto"

    # -------------------Gets and Sets--------------------------

    def getValor(self):
        return self.valor
    def setValor(self,valor):
        self.valor=valor
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
        self.null = No(None)
        self.null.setPai(self.null)
        self.null.setAnterior(self.null)
        self.null.setProximo(self.null)
        self.raiz = self.null

    def getRaiz(self):
        return self.raiz

    def setRaiz(self, no):
        self.raiz = no

    def minimoArvore(self, no):
        while no.getAnterior() != self.null:
            no = no.getAnterior()
        return no

    def maximoArvore(self, no):
        while no.getProximo() != self.null:
            no = no.getProximo()
        return no

    def sucessorArvore(self, no):
        if no.getProximo() != self.null:
            return self.minimoArvore(no.getProximo())
        auxiliar = no.getPai()
        while auxiliar != self.null and no == auxiliar.getProximo():
            no = auxiliar
            auxiliar = auxiliar.getPai()
        return auxiliar

    def predecessorArvore(self, no):
        if no.getAnterior != self.null:
            return self.maximoArvore(no.getAnterior())
        auxiliar = no.getPai()
        while auxiliar != self.null and no == auxiliar.getAnterior():
            no = auxiliar
            auxiliar = auxiliar.getPai()
        return auxiliar

    def inserir(self, no):
        auxiliar = self.null
        noLocal = self.getRaiz()
        while noLocal != self.null:
            auxiliar = noLocal
            if no.getChave() < noLocal.getChave():
                noLocal = noLocal.getAnterior()
            else:
                noLocal = noLocal.getProximo()
        no.setPai(auxiliar)
        if auxiliar == self.null:
            self.setRaiz(no)
        elif no.getChave() < auxiliar.getChave():
            auxiliar.setAnterior(no)
        else:
            auxiliar.setProximo(no)
        no.setAnterior(self.null)
        no.setProximo(self.null)
        no.setCor("vermelho")
        self.inserirFix(no)

    def inserirFix(self, no):
        while no.getPai().getCor() == "vermelho":
            if no.getPai() == no.getPai().getPai().getAnterior():
                auxiliar = no.getPai().getPai().getProximo()
                if auxiliar.getCor() == "vermelho":
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
                    if no == no.getPai().getAnterior():
                        no = no.getPai()
                        self.rotDir(no)
                    no.getPai().setCor("preto")
                    no.getPai().getPai().setCor("vermelho")
                    self.rotEsq(no.getPai().getPai())
        self.getRaiz().setCor("preto")

    def rotEsq(self, no):
        noRotacionado = no.getProximo()
        no.setProximo(noRotacionado.getAnterior())
        if noRotacionado.getAnterior() != self.null:
            noRotacionado.getAnterior().setPai(no)
        noRotacionado.setPai(no.getPai())
        if no.getPai() == self.null:
            self.raiz = noRotacionado
        elif no == no.getPai().getAnterior():
            no.getPai().setAnterior(noRotacionado)
        else:
            no.getPai().setProximo(noRotacionado)
        noRotacionado.setAnterior(no)
        no.setPai(noRotacionado)

    def rotDir(self, no):
        noRotacionado = no.getAnterior()
        no.setAnterior(noRotacionado.getProximo())
        if noRotacionado.getProximo() != self.null:
            noRotacionado.getProximo().setPai(no)
        noRotacionado.setPai(no.getPai())
        if no.getPai() == self.null:
            self.raiz = noRotacionado
        elif no == no.getPai().getProximo():
            no.getPai().setProximo(noRotacionado)
        else:
            no.getPai().setAnterior(noRotacionado)
        noRotacionado.setRight(no)
        no.setPai(noRotacionado)

    def delete(self, no):
        if no.getAnterior() == self.null and no.getProximo() == self.null:
            auxiliar = no
        else:
            auxiliar = self.sucessorArvore(no)
        if auxiliar.getAnterior() != self.null:
            x = auxiliar.getAnterior()
        else:
            x = auxiliar.getProximo()
        x.setPai(auxiliar.setPai())
        if auxiliar.getPai() != self.null:
            self.setRaiz(x)
        else:
            if auxiliar == auxiliar.getPai().getAnterior():
                auxiliar.getPai().setAnterior(x)
            else:
                auxiliar.getPai().setProximo(x)
        if auxiliar != no:
            no.setChave(x.getChave())
        if auxiliar.getCor() == "preto":
            self.deleteFix(x)
        return auxiliar

    def deleteFix(self, no):
        while no != self.getRaiz() and no.getCor() == "preto":
            if no == no.getPai().getAnterior():
                auxiliar = no.getPai().getProximo()
                if auxiliar.getCor() == "vermelho":
                    auxiliar.setCor("preto")
                    no.getPai().setCor("vermelho")
                    self.rotEsq(no.getPai())
                    auxiliar = no.getPai().getProximo()
                if auxiliar.getAnterior().getCor() == "preto" and auxiliar.getProximo().getCor() == "preto":
                    auxiliar.setCor("vermelho")
                    no = no.getPai()
                else:
                    if auxiliar.getProximo().getCor() == "preto":
                        auxiliar.getAnterior().setCor("preto")
                        auxiliar.setCor("vermelho")
                        self.rotDir(auxiliar)
                        auxiliar = no.getPai().getProximo()
                    auxiliar.setCor(no.getPai().getCor())
                    no.getPai().setCor("preto")
                    auxiliar.getProximo().setCor("preto")
                    self.rotEsq(no.getPai())
                    no = self.getRaiz()
            else:
                auxiliar = no.getPai().getAnterior()
                if auxiliar.getCor() == "vermelho":
                    auxiliar.setCor("preto")
                    no.getPai().setCor("vermelho")
                    self.rotDir(no.getPai())
                    auxiliar = no.getPai().getAnterior()
                if auxiliar.getProximo().getCor() == "preto" and auxiliar.getAnterior().getCor() == "preto":
                    auxiliar.setCor("vermelho")
                    no = no.getPai()
                else:
                    if auxiliar.getAnterior().getCor() == "preto":
                        auxiliar.getProximo().setCor("preto")
                        auxiliar.setCor("vermelho")
                        self.rotEsq(auxiliar)
                        auxiliar = no.getPai().getAnterior()
                    auxiliar.setCor(no.getPai().getCor())
                    no.getPai().setCor("preto")
                    auxiliar.getAnterior.setCor("preto")
                    self.rotDir(no.getPai())
                    no = self.getRaiz()
        no.setCor("preto")

    def buscar(self, chave):
        x = self.raiz
        while x != self.null and chave != x.getChave():
            if chave > x.getChave():
                x = x.getProximo()
            else:
                x = x.getAnterior()
        return x

    def percorrerEmOrdem(self, no, arquivo):
        if no != self.null:
            self.percorrerEmOrdem(no.getAnterior(), arquivo)
            string = " - "
            for x in no.getAluguel():
                string = string + str(x.getNome()) + " / "
            arquivo.writelines(str(no.getChave() + string))
            self.percorrerEmOrdem(no.getProximo(), arquivo)
