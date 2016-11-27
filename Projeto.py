from PyQt5 import QtCore, QtWidgets
import  sys

class Usuario:
    def __init__(self, cpf, nome):
        self.chave = cpf
        self.anterior = None
        self.proximo = None
        self.pai = None
        self.cor = "preto"
        self.nome = nome
        self.livros_alugados = []

    def getChave(self):
        return self.chave
    def setChave(self,valor):
        self.chave=valor
    def getNome(self):
        return self.nome
    def getAlugados(self):
        return self.livros_alugados
    def adicionarAlugado(self,livro):
        self.livros_alugados.append(livro)
    def removerAlugado(self,livro):
        self.livros_alugados.remove(livro)
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
        self.chave = nome
        self.anterior = None
        self.proximo = None
        self.pai = None
        self.cor = "preto"
        self.quantidade = quantidade
        self.reservado = False
        self.alugado = False
        self.usuarios_alugou = []
        self.usuarios_reservou = []

    def getChave(self):
        return self.chave
    def setChave(self,valor):
        self.chave=valor
    def getQuantidade(self):
        return self.quantidade
    def mudarQuantidade(self,numero):
        self.quantidade= self.quantidade + numero
    def isReservado(self):
        return self.reservado
    def getAluguel(self):
        return self.usuarios_alugou
    def adicionarAluguel(self,aluno):
        self.usuarios_alugou.append(aluno)
    def removeAluguel(self,aluno):
        self.usuarios_alugou.remove(aluno)
    def adicionarReserva(self, aluno):
        self.usuarios_reservou.append(aluno)
    def removeReserva(self):
        return self.usuarios_reservou.pop(0)
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


class ArvoreRB:
    def __init__(self):
        self.raiz = None

    def minimoArvore(self,no):
        while no.getAnterior() != None:
            no = no.getAnterior()
        return no
    def maximoArvore(self,no):
        while no.getProximo() != None:
            no=no.getProximo()
        return no

    def sucessorArvore(self,no):
        if no.getProximo() != None:
            return self.minimoArvore(no.getProximo())
        auxiliar = no.getPai()
        while auxiliar != None and no == auxiliar.getProximo():
            no = auxiliar
            auxiliar = auxiliar.getPai()
        return auxiliar
    def predecessorArvore(self,no):
        if no.getAnterior != None:
            return self.maximoArvore(no.getAnterior())
        auxiliar = no.getPai()
        while auxiliar != None and no == auxiliar.getAnterior():
            no = auxiliar
            auxiliar = auxiliar.getPai()
        return auxiliar

    def inserir(self,no):
        if self.raiz == None:
            self.raiz=no
        else:
            self.inseri(no)

    def inseri(self, no):
        auxiliar = None
        noLocal = self.raiz
        while noLocal != None:
            auxiliar = noLocal
            if no.getChave() < noLocal.getChave():
                noLocal = noLocal.getAnterior()
            else:
                noLocal = noLocal.getProximo()
        no.setPai(auxiliar)
        if auxiliar == None:
            self.raiz=no
        elif no.getChave() < auxiliar.getChave():
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
        #falta coisa

    def delete(self,no):
        if no.getAnterior() == None and no.getProximo()== None:
            auxiliar = no
        else:
           auxiliar = self.sucessorArvore(no)
        if auxiliar.getAnterior() != None:
            x = auxiliar.getAnterior()
        else:
            x = auxiliar.getProximo()
        x.setPai(auxiliar.setPai())
        if auxiliar.getPai() != None:
            self.raiz = x
        elif auxiliar == auxiliar.getPai().getAnterior():
            auxiliar.getPai().setAnterior(x)
        else:
            auxiliar.getPai().setProximo(x)
        if auxiliar != no:
            no.setValor(x.getChave())
        if auxiliar.getCor() == "preto":
            self.deleteFix(x)
        return auxiliar

    def deleteFix(self,no):
        while no != self.raiz:
            if no == no.getPai().getAnterior():
                auxiliar = no.getPai().getProximo()
                if auxiliar.getCor() == "preto":
                    no.getPai().setCor("vermelho")
                    self.rotEsq(no.getPai())
                    auxiliar=no.getPai().getProximo()
                if auxiliar.getAnterior().getCor() == "preto" and auxiliar.getProximo().getCor()=="vermelho":
                    auxiliar.setCor("vermelho")
                    no=no.getPai()
                elif auxiliar.getProximo().getCor() == "preto":
                    auxiliar.getAnterior().setCor("vermelho")
                    self.rotDir(auxiliar)
                    auxiliar = no.getPai().getProximo()
                    auxiliar.setCor(no.getPai().getCor())
                    no.getPai().setCor("preto")
                    auxiliar.getProximo().setCor("preto")
                    self.rotEsq(no.getPai())
                    no=self.raiz
                else:
                    auxiliar.getProximo().setCor("vermelho")
                    self.rotDir(auxiliar)
                    auxiliar = no.getPai().getAnterior()
                    auxiliar.setCor(no.getPai().getCor())
                    no.getPai().setCor("preto")
                    auxiliar.getAnterior().setCor("preto")
                    self.rotEsq(no.getPai())
                    no = self.raiz
        no.setCor("preto")

    def buscar(self, chave):
        x = self.raiz
        while x != None and chave != x.getChave():
            if chave > x.getChave():
                x = x.getProximo()
            else:
                x = x.getAnterior()
        return x

    def percorrerEmOrdem(self, no):
        if no != None:
            self.percorrerEmOrdem(no.getAnterior())
            print(no.getChave())
            self.percorrerEmOrdem(no.getProximo())

class Ui_MainWindow(object):
    def __init__(self, arvore,arvore2,box):
        self.arvore_livro = arvore
        self.arvore_usuario = arvore2
        self.usuario= None
        self.livro = None
        self.mensagem = box

    def iniciarUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 315)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 316))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(1,1,1,1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.menu.setObjectName("menu")
        self.Cadastros = QtWidgets.QWidget()
        self.Cadastros.setObjectName("Cadastros")
        self.frame = QtWidgets.QFrame(self.Cadastros)
        self.frame.setGeometry(QtCore.QRect(0, 0, 420, 315))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button_Cadastrar_livro = QtWidgets.QPushButton(self.frame)
        self.button_Cadastrar_livro.setGeometry(QtCore.QRect(300, 60, 85, 27))
        self.button_Cadastrar_livro.setObjectName("button_Cadastrar_livro")
        self.button_Cancelar = QtWidgets.QPushButton(self.frame)
        self.button_Cancelar.setGeometry(QtCore.QRect(20, 240, 85, 27))
        self.button_Cancelar.setObjectName("button_Cancelar")
        self.label_nome_livros = QtWidgets.QLabel(self.frame)
        self.label_nome_livros.setGeometry(QtCore.QRect(20, 40, 54, 17))
        self.label_nome_livros.setObjectName("label_nome_livros")
        self.label_quatidade_livros = QtWidgets.QLabel(self.frame)
        self.label_quatidade_livros.setGeometry(QtCore.QRect(160, 40, 71, 17))
        self.label_quatidade_livros.setObjectName("label_quatidade_livros")
        self.editText_nome_livros = QtWidgets.QLineEdit(self.frame)
        self.editText_nome_livros.setGeometry(QtCore.QRect(20, 60, 113, 29))
        self.editText_nome_livros.setObjectName("editText_nome_livros")
        self.editText_quantidade_livros = QtWidgets.QLineEdit(self.frame)
        self.editText_quantidade_livros.setGeometry(QtCore.QRect(150, 60, 113, 29))
        self.editText_quantidade_livros.setObjectName("editText_quantidade_livros")
        self.Label_Livros = QtWidgets.QLabel(self.frame)
        self.Label_Livros.setGeometry(QtCore.QRect(10, 10, 111, 17))
        self.Label_Livros.setObjectName("Label_Livros")
        self.label_Usuarios = QtWidgets.QLabel(self.frame)
        self.label_Usuarios.setGeometry(QtCore.QRect(10, 100, 131, 17))
        self.label_Usuarios.setObjectName("label_Usuarios")
        self.editText_nome_usuario = QtWidgets.QLineEdit(self.frame)
        self.editText_nome_usuario.setGeometry(QtCore.QRect(20, 150, 113, 29))
        self.editText_nome_usuario.setObjectName("editText_nome_usuario")
        self.label_nome_usuarios = QtWidgets.QLabel(self.frame)
        self.label_nome_usuarios.setGeometry(QtCore.QRect(20, 130, 54, 17))
        self.label_nome_usuarios.setObjectName("label_nome_usuarios")
        self.label_cpf = QtWidgets.QLabel(self.frame)
        self.label_cpf.setGeometry(QtCore.QRect(160, 130, 54, 17))
        self.label_cpf.setObjectName("label_cpf")
        self.editText_cpf_usuario = QtWidgets.QLineEdit(self.frame)
        self.editText_cpf_usuario.setGeometry(QtCore.QRect(150, 150, 113, 29))
        self.editText_cpf_usuario.setObjectName("editText_cpf_usuario")
        self.button_Cadastrar_usuario = QtWidgets.QPushButton(self.frame)
        self.button_Cadastrar_usuario.setGeometry(QtCore.QRect(300, 150, 85, 27))
        self.button_Cadastrar_usuario.setObjectName("button_Cadastrar_usuario")
        self.button_Descadastrar_usuario = QtWidgets.QPushButton(self.frame)
        self.button_Descadastrar_usuario.setGeometry(QtCore.QRect(120, 240, 131, 27))
        self.button_Descadastrar_usuario.setObjectName("button_Descadastrar_usuario")
        self.button_Descadastrar_livro = QtWidgets.QPushButton(self.frame)
        self.button_Descadastrar_livro.setGeometry(QtCore.QRect(274, 240, 131, 27))
        self.button_Descadastrar_livro.setObjectName("button_Descadastrar_livro")
        self.menu.addTab(self.Cadastros, "")
        self.Biblioteca = QtWidgets.QWidget()
        self.Biblioteca.setObjectName("Biblioteca")
        self.frame_2 = QtWidgets.QFrame(self.Biblioteca)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 420, 315))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.button_Cancelar_2 = QtWidgets.QPushButton(self.frame_2)
        self.button_Cancelar_2.setGeometry(QtCore.QRect(10, 240, 85, 27))
        self.button_Cancelar_2.setObjectName("button_Cancelar_2")
        self.editText_buscar_usuario = QtWidgets.QLineEdit(self.frame_2)
        self.editText_buscar_usuario.setGeometry(QtCore.QRect(290, 0, 113, 29))
        self.editText_buscar_usuario.setObjectName("editText_buscar_usuario")
        self.textView_Nome_usuario = QtWidgets.QLabel(self.frame_2)
        self.textView_Nome_usuario.setGeometry(QtCore.QRect(10, 10, 54, 17))
        self.textView_Nome_usuario.setObjectName("textView_Nome_usuario")
        self.textView_nome_Livro = QtWidgets.QLabel(self.frame_2)
        self.textView_nome_Livro.setGeometry(QtCore.QRect(10, 110, 54, 17))
        self.textView_nome_Livro.setObjectName("textView_nome_Livro")
        self.editText_buscar_livro = QtWidgets.QLineEdit(self.frame_2)
        self.editText_buscar_livro.setGeometry(QtCore.QRect(290, 100, 113, 29))
        self.editText_buscar_livro.setObjectName("editText_buscar_livro")
        self.button_buscar_usuario = QtWidgets.QPushButton(self.frame_2)
        self.button_buscar_usuario.setGeometry(QtCore.QRect(320, 30, 85, 27))
        self.button_buscar_usuario.setObjectName("button_buscar_usuario")
        self.button_buscar_livro = QtWidgets.QPushButton(self.frame_2)
        self.button_buscar_livro.setGeometry(QtCore.QRect(320, 130, 85, 27))
        self.button_buscar_livro.setObjectName("button_buscar_livro")
        self.textView_isDisponivel = QtWidgets.QLabel(self.frame_2)
        self.textView_isDisponivel.setGeometry(QtCore.QRect(150, 110, 111, 17))
        self.textView_isDisponivel.setObjectName("textView_isDisponivel")
        self.label_quantidade = QtWidgets.QLabel(self.frame_2)
        self.label_quantidade.setGeometry(QtCore.QRect(10, 140, 81, 17))
        self.label_quantidade.setTextFormat(QtCore.Qt.RichText)
        self.label_quantidade.setObjectName("label_quantidade")
        self.textView_Quantidade = QtWidgets.QLabel(self.frame_2)
        self.textView_Quantidade.setGeometry(QtCore.QRect(110, 140, 54, 17))
        self.textView_Quantidade.setObjectName("textView_Quantidade")
        self.button_devolver = QtWidgets.QPushButton(self.frame_2)
        self.button_devolver.setGeometry(QtCore.QRect(120, 240, 85, 27))
        self.button_devolver.setObjectName("button_devolver")
        self.button_alugar = QtWidgets.QPushButton(self.frame_2)
        self.button_alugar.setGeometry(QtCore.QRect(220, 240, 85, 27))
        self.button_alugar.setObjectName("button_alugar")
        self.list_Alugados = QtWidgets.QListWidget(self.frame_2)
        self.list_Alugados.setGeometry(QtCore.QRect(10, 30, 281, 51))
        self.list_Alugados.setFlow(QtWidgets.QListView.LeftToRight)
        self.list_Alugados.setObjectName("list_Alugados")
        self.list_Alugou = QtWidgets.QListWidget(self.frame_2)
        self.list_Alugou.setGeometry(QtCore.QRect(10, 170, 381, 51))
        self.list_Alugou.setFlow(QtWidgets.QListView.LeftToRight)
        self.list_Alugou.setObjectName("list_Alugou")
        self.menu.addTab(self.Biblioteca, "")
        self.verticalLayout.addWidget(self.menu)
        MainWindow.setCentralWidget(self.centralWidget)

        self.nomearUi(MainWindow)
        self.menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.func()


    def nomearUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        self.button_Cadastrar_livro.setText("Cadastrar")
        self.button_Cancelar.setText("Cancelar")
        self.label_nome_livros.setText("Nome")
        self.label_quatidade_livros.setText("Quantidade")
        self.Label_Livros.setText("Cadastro De Livros")
        self.label_Usuarios.setText("Cadastro De Usuarios")
        self.label_nome_usuarios.setText("Nome")
        self.label_cpf.setText("CPF")
        self.button_Cadastrar_usuario.setText("Cadastrar")
        self.button_Descadastrar_usuario.setText("Descadastrar Usuario")
        self.button_Descadastrar_livro.setText("Descadastrar Livro")
        self.menu.setTabText(self.menu.indexOf(self.Cadastros), "Cadastros")
        self.button_Cancelar_2.setText("Cancelar")
        self.textView_Nome_usuario.setText("Usuario")
        self.textView_nome_Livro.setText("Livro")
        self.button_buscar_usuario.setText("Buscar")
        self.button_buscar_livro.setText("Buscar")
        self.textView_isDisponivel.setText("Disponivel")
        self.label_quantidade.setText("Quantidade:")
        self.textView_Quantidade.setText("numeros")
        self.button_devolver.setText("Devolver")
        #self.button_reservar.setText("Reservar")
        self.button_alugar.setText("Alugar")
        self.menu.setTabText(self.menu.indexOf(self.Biblioteca), "Biblioteca")

    def func(self):
        self.button_Cadastrar_livro.clicked.connect(self.cadastroLivro)
        self.button_buscar_livro.clicked.connect(self.buscarLivro)
        self.button_buscar_usuario.clicked.connect(self.buscarUsuario)
        self.button_Cadastrar_usuario.clicked.connect(self.cadastroUsuario)
        self.button_alugar.clicked.connect(self.alugarLivro)
        self.button_Descadastrar_livro.clicked.connect(self.descadastroLivro)
        self.button_Descadastrar_usuario.clicked.connect(self.descadastroUsuario)
        self.button_devolver.clicked.connect(self.devolverLivro)
        self.button_Cancelar.clicked.connect(sys.exit)
        self.button_Cancelar_2.clicked.connect(sys.exit)


    def cadastroLivro(self):
        titulo =  self.editText_nome_livros.text()
        quantidade =  int(self.editText_quantidade_livros.text())
        livro = Livro(titulo, quantidade)
        self.arvore_livro.inserir(livro)

    def cadastroUsuario(self):
        cpf =  self.editText_cpf_usuario.text()
        nome = self.editText_nome_usuario.text()
        usuario = Usuario(cpf, nome)
        self.arvore_usuario.inserir(usuario)

    def descadastroLivro(self):
        self.arvore_livro.delete(self.livro)

    def descadastroUsuario(self):
        self.arvore_usuario.delete(self.usuario)

    def alugarLivro(self):
        livro = self.livro
        if livro != None:
            disponibilidade = livro.getQuantidade()
            reservado = livro.isReservado()
            usuario = self.usuario
            if usuario != None:
                if disponibilidade == 0 and reservado == False:
                    mensagem= QtWidgets.QMessageBox.question(self.mensagem,"Aviso!",
                                                            "Livro nao disponivel, deseja alugar?",
                                                            QtWidgets.QMessageBox.Yes |
                                                             QtWidgets.QMessageBox.No)
                    if mensagem == QtWidgets.QMessageBox.Yes:
                        livro.adicionarReserva(usuario)
                elif disponibilidade != 0 and reservado == True:
                    mensagem = QtWidgets.QMessageBox.question(self.mensagem, "Aviso!",
                                                              "O Livro ja esta reservado!, deseja entra na fila?",
                                                              QtWidgets.QMessageBox.Yes |
                                                              QtWidgets.QMessageBox.No)

                    if mensagem == QtWidgets.QMessageBox.Yes:
                        livro.adicionarReserva(usuario)
                elif disponibilidade != 0 and reservado == False:
                    mensagem = QtWidgets.QMessageBox.question(self.mensagem, "Aviso!","Livro disponivel!")
                    usuario.adicionarAlugado(livro)
                    livro.adicionarAluguel(usuario)
                    livro.mudarQuantidade(-1)


    def devolverLivro(self,):
        livro = self.livro
        if livro != None:
            disponibilidade = livro.getQuantidade()
            reservado = livro.isReservado()
            usuario = self.usuario
            if usuario != None:
                if disponibilidade == 0 and reservado == True:
                    livro.removeAluguel(usuario)
                    reservou = livro.removeReservado()
                    livro.adicionarAluguel(reservou)
                    usuario.removerAlugado(livro)
                    mensagem = QtWidgets.QMessageBox.question(self.mensagem, "Aviso!", "Livro restornado com sucesso!")
                    if len(livro.reservou) == 0:
                        livro.reservado = False
                elif disponibilidade != 0:
                    livro.removeAluguel(usuario.getChave())
                    usuario.removerAlugado(livro)
                    livro.mudarQuantidade(1)
                    mensagem = QtWidgets.QMessageBox.question(self.mensagem, "Aviso!", "Livro restornado com sucesso!")

    def buscarUsuario(self):
        usuario=self.arvore_usuario.buscar(self.editText_buscar_usuario.text())
        self.textView_Nome_usuario.setText(usuario.getNome())
        if len(usuario.getAlugados()) !=0:
            for i in usuario.getAlugados():
                item = QtWidgets.QListWidgetItem(i.getChave())
                self.list_Alugados.addItem(item)
        self.usuario = usuario

    def buscarLivro(self):
        livro = self.arvore_livro.buscar(self.editText_buscar_livro.text())
        self.textView_nome_Livro.setText(livro.getChave())
        self.textView_Quantidade.setText(str(livro.getQuantidade()))
        if livro.getQuantidade() > 0 :
            self.textView_isDisponivel.setText("Disponivel")
        else:
            self.textView_isDisponivel.setText("Nao Disponivel")
        if len(livro.getAluguel()) != 0:
            for i in livro.getAluguel():
                item = QtWidgets.QListWidgetItem(i.getNome())
                self.list_Alugou.addItem(item)
        self.livro = livro


def run():
    livros = ArvoreRB()
    usuarios = ArvoreRB()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    popup = QtWidgets.QMessageBox()
    ui = Ui_MainWindow(livros,usuarios,popup)
    ui.iniciarUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


run()