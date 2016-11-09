class No:
    def __init__(self, chave, data = 0):
        self.data = data
        self.chave = chave
        self.cor = 'red'
        self.pai = None
        self.left = None
        self.right = None

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getChave(self):
        return self.chave
    
    def setChave(self, x):
        self.chave = x
    
    def getCor(self):
        return self.cor
    
    def setCor(self, C):
        self.cor = C
    
    def getPai(self):
        return self.pai
    
    def setPai(self, P):
        self.pai = P
    
    def getLeft(self):
        return self.left
    
    def setLeft(self, L):
        self.left = L
    
    def getRight(self):
        return self.right
    
    def setRight(self, R):
        self.right = R

class ArvoreRB:
    def __init__(self):
        self.none = No(None, None)
        self.none.setPai(self.none)
        self.none.setLeft(self.none)
        self.none.setRight(self.none)
        self.none.setCor('black')
        self.root = self.none

    def getRoot(self):
        return self.root
    
    def setRoot(self, x):
        self.root = x

    def maximo(self, x):
        while x.getRight() != None:
            x = x.getRight()
        return x

    def minimo(self, x):
        while x.getLeft() != None:
            x = x.getLeft()
        return x

    def sucessor(self, x):
        if x.getRight() != None:
            return self.minimo(x.getRight())
        y = x.getPai()
        while y != None and x == y.getRight():
            x = y
            y = y.getPai()
        return y

    def antecessor(self, x):
        if x.getLeft() != None:
            return self.maximo(x.getLeft())
        y = x.getPai()
        while y != None and x == y.getLeft():
            x = y
            y = y.getPai()
        return y

    def rotateLeft(self, x):
        y = x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft() != self.none:
            y.getLeft().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == self.none:
            self.setRoot(y)
        elif x == x.getPai().getLeft():
            x.getPai().setLeft(y)
        else:
            x.getPai().setRight(y)
        y.setLeft(x)
        x.setPai(y)

    def rotateRight(self, x):
        y = x.getLeft()
        x.setLeft(y.getRight())
        if y.getRight() != self.none:
            y.getRight().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == self.none:
            self.setRoot(y)
        elif x == x.getPai().getRight():
            x.getPai().setRight(y)
        else:
            x.getPai().setLeft(y)
        y.setRight(x)
        x.setPai(y)

    def RBinsert(self,z ):
        y = self.none
        x = self.getRoot()
        while x != self.none:
            y = x
            if z.getChave() < x.getChave():
                x = x.getLeft()
            else:
                x = x.getRight()
        z.setPai(y)
        if y == self.none:
            self.setRoot(z)
        elif z.getChave() < y.getChave():
            y.setLeft(z)
        else:
            y.setRight(z)
        z.setLeft(self.none)
        z.setRight(self.none)
        z.setCor('red')
        self.insertFixUp(z)
        
    def insertFixUp(self, z):
        while z.getPai().getCor() == 'red':
            if z.getPai() == z.getPai().getPai().getLeft():
                y = z.getPai().getPai().getRight()
                if y.getCor() == 'red':
                    z.getPai().setCor('black')
                    y.setCor('black')
                    z.getPai().getPai().setCor('red')
                    z = z.getPai().getPai()
                else:
                    if z == z.getPai().getRight():
                        z = z.getPai()
                        self.rotateLeft(z)
                    z.getPai().setCor('black')
                    z.getPai().getPai().setCor('red')
                    self.rotateRight(z.getPai().getPai())
            else:
                y = z.getPai().getPai().getLeft()
                if y.getCor() == 'red':
                    z.getPai().setCor('black')
                    y.setCor('black')
                    z.getPai().getPai().setCor('red')
                    z = z.getPai().getPai()
                else:
                    if z == z.getPai().getLeft():
                        z = z.getPai()
                        self.rotateRight(z)
                    z.getPai().setCor('black')
                    z.getPai().getPai().setCor('red')
                    self.rotateLeft(z.getPai().getPai())
        self.getRoot().setCor('black')

    def RBdelete(self, z):
        if z.getLeft() == self.none or z.getRight() == self.none:
            y = z
        else:
            y = self.sucessor(z)
        if y.getLeft() != self.none:
            x = y.getLeft()
        else:
            x = y.getRight()
        x.setPai(y.getPai())
        if y.getPai() == self.none:
            self.setRoot(x)
        else:
            if y == y.getPai().getLeft():
                y.getPai().setLeft(x)
            else:
                y.getPai().setRight(x)
        if y != z:
            z.setChave(y.getChave())
        if y.getCor() == 'black':
            self.deleteFixUp(x)
        return y

    def deleteFixUp(self, x):
        while x != self.getRoot() and x.getCor() == 'black':
            if x == x.getPai().getLeft():
                w = x.getPai().getRight()
                if w.getCor() == 'red':
                    w.setCor('black')
                    x.getPai().setCor('red')
                    self.rotateLeft(x.getPai())
                    w = x.getPai().getRight()
                if w.getLeft().getCor() == 'black' and w.getRight().getCor() == 'black':
                    w.setCor('red')
                    x = x.getPai()
                else:
                    if w.getRight().getCor() == 'black':
                        w.getLeft().setCor('black')
                        w.setCor('red')
                        self.rotateRight(w)
                        w = x.getPai().getRight()
                    w.setCor(x.getPai().getCor())
                    x.getPai().setCor('black')
                    w.getRight().setCor('black')
                    self.rotateLeft(x.getPai())
                    x = self.getRoot()
            else:
                w = x.getPai().getLeft()
                if w.getCor() == 'red':
                    w.setCor('black')
                    x.getPai().setCor('red')
                    self.rotateRight(x.getPai())
                    w = x.getPai().getLeft()
                if w.getRight().getCor() == 'black' and w.getLeft().getCor() == 'black':
                    w.setCor('red')
                    x = x.getPai()
                else:
                    if w.getLeft().getCor() == 'black':
                        w.getRight().setCor('black')
                        w.setCor('red')
                        self.rotateLeft(w)
                        w = x.getPai().getLeft()
                    w.setCor(x.getPai().getCor())
                    x.getPai().setCor('black')
                    w.getLeft().setCor('black')
                    self.rotateRight(x.getPai())
                    x = self.getRoot()
        x.setCor('black')

    def percorrerEmOrdem(self, x):
        if x != None:
            self.percorrerEmOrdem(x.getLeft())
            print(x.chave)
            self.percorrerEmOrdem(x.getRight())

    def buscar(self, valor):
        x = self.root
        while (x != None) and (valor != x.getChave()):
            if valor > x.getChave():
                x = x.getRight()
            else:
                x = x.getLeft()
        return x

a = ArvoreRB()
no= No(20)
no2 = No(10)
a.RBinsert(no)
a.RBinsert(no2)
print(a.buscar(10))