# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Telas_APS.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        if not TelaPrincipal.objectName():
            TelaPrincipal.setObjectName(u"TelaPrincipal")
        TelaPrincipal.resize(708, 462)
        TelaPrincipal.setStyleSheet(u"background-color: rgb(59, 59, 59);")
        self.centralwidget = QWidget(TelaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:rgb(255,255,255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ctEsquerda = QFrame(self.centralwidget)
        self.ctEsquerda.setObjectName(u"ctEsquerda")
        self.ctEsquerda.setMinimumSize(QSize(0, 0))
        self.ctEsquerda.setMaximumSize(QSize(2, 16777215))
        self.ctEsquerda.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QToolBox{\n"
"	text-align: left;\n"
"	backgroud-color: rgb(0, 45, 0);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	borde-radius: 5pix;\n"
"\n"
"	background-color:rgb(0, 255, 127);\n"
"	text-align:left;\n"
"	\n"
"}\n"
"")
        self.ctEsquerda.setFrameShape(QFrame.StyledPanel)
        self.ctEsquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ctEsquerda)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ctNomeSistema = QFrame(self.ctEsquerda)
        self.ctNomeSistema.setObjectName(u"ctNomeSistema")
        self.ctNomeSistema.setFrameShape(QFrame.StyledPanel)
        self.ctNomeSistema.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ctNomeSistema)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblTitulo_2 = QLabel(self.ctNomeSistema)
        self.lblTitulo_2.setObjectName(u"lblTitulo_2")

        self.horizontalLayout_2.addWidget(self.lblTitulo_2)


        self.verticalLayout_2.addWidget(self.ctNomeSistema)

        self.toolboxMenu = QToolBox(self.ctEsquerda)
        self.toolboxMenu.setObjectName(u"toolboxMenu")
        self.toolboxMenu.setEnabled(True)
        self.toolboxMenu.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(148, 148, 111);\n"
"	borde-top-left-radius: 15pix;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(0, 85, 0);\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 105, 318))
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnArquivos = QPushButton(self.page)
        self.btnArquivos.setObjectName(u"btnArquivos")
        self.btnArquivos.setMinimumSize(QSize(0, 30))
        self.btnArquivos.setMaximumSize(QSize(16777215, 16777215))
        self.btnArquivos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnArquivos)

        self.btnCadastrarUsuario = QPushButton(self.page)
        self.btnCadastrarUsuario.setObjectName(u"btnCadastrarUsuario")
        self.btnCadastrarUsuario.setEnabled(True)
        self.btnCadastrarUsuario.setMinimumSize(QSize(0, 30))
        self.btnCadastrarUsuario.setMaximumSize(QSize(16777215, 16777215))
        self.btnCadastrarUsuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnCadastrarUsuario)

        self.btnUsuriosAtivos = QPushButton(self.page)
        self.btnUsuriosAtivos.setObjectName(u"btnUsuriosAtivos")
        self.btnUsuriosAtivos.setMinimumSize(QSize(0, 30))
        self.btnUsuriosAtivos.setMaximumSize(QSize(16777215, 16777215))
        self.btnUsuriosAtivos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btnUsuriosAtivos)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.toolboxMenu.addItem(self.page, u"Arquivos e Usu\u00e1rios")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 120, 318))
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnRelUsuarios = QPushButton(self.page_2)
        self.btnRelUsuarios.setObjectName(u"btnRelUsuarios")
        self.btnRelUsuarios.setMinimumSize(QSize(0, 30))
        self.btnRelUsuarios.setMaximumSize(QSize(16777215, 16777215))
        self.btnRelUsuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnRelUsuarios)

        self.btnRelAcessos = QPushButton(self.page_2)
        self.btnRelAcessos.setObjectName(u"btnRelAcessos")
        self.btnRelAcessos.setMinimumSize(QSize(0, 30))
        self.btnRelAcessos.setMaximumSize(QSize(16777215, 16777215))
        self.btnRelAcessos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnRelAcessos)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.toolboxMenu.addItem(self.page_2, u"Relat\u00f3rios")

        self.verticalLayout_2.addWidget(self.toolboxMenu)


        self.horizontalLayout.addWidget(self.ctEsquerda)

        self.ctPrincipal = QFrame(self.centralwidget)
        self.ctPrincipal.setObjectName(u"ctPrincipal")
        self.ctPrincipal.setFrameShape(QFrame.StyledPanel)
        self.ctPrincipal.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.ctPrincipal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ctCabecalho = QFrame(self.ctPrincipal)
        self.ctCabecalho.setObjectName(u"ctCabecalho")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctCabecalho.sizePolicy().hasHeightForWidth())
        self.ctCabecalho.setSizePolicy(sizePolicy)
        self.ctCabecalho.setFrameShape(QFrame.StyledPanel)
        self.ctCabecalho.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.ctCabecalho)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ctDadosCabecalho = QFrame(self.ctCabecalho)
        self.ctDadosCabecalho.setObjectName(u"ctDadosCabecalho")
        self.ctDadosCabecalho.setFrameShape(QFrame.StyledPanel)
        self.ctDadosCabecalho.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.ctDadosCabecalho)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblTitulo = QLabel(self.ctDadosCabecalho)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.gridLayout.addWidget(self.lblTitulo, 0, 2, 1, 1)

        self.lblAcesso = QLabel(self.ctDadosCabecalho)
        self.lblAcesso.setObjectName(u"lblAcesso")

        self.gridLayout.addWidget(self.lblAcesso, 3, 0, 1, 1)

        self.btnMenu = QPushButton(self.ctDadosCabecalho)
        self.btnMenu.setObjectName(u"btnMenu")
        sizePolicy.setHeightForWidth(self.btnMenu.sizePolicy().hasHeightForWidth())
        self.btnMenu.setSizePolicy(sizePolicy)
        self.btnMenu.setMaximumSize(QSize(40, 40))
        self.btnMenu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"ui\icons\Botão Menu Verde.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMenu.setIcon(icon)

        self.gridLayout.addWidget(self.btnMenu, 0, 0, 1, 1)

        self.lblNome = QLabel(self.ctDadosCabecalho)
        self.lblNome.setObjectName(u"lblNome")

        self.gridLayout.addWidget(self.lblNome, 1, 0, 1, 1)

        self.lblID = QLabel(self.ctDadosCabecalho)
        self.lblID.setObjectName(u"lblID")

        self.gridLayout.addWidget(self.lblID, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.ctDadosCabecalho, 0, 0, 1, 1)

        self.ctLogo = QFrame(self.ctCabecalho)
        self.ctLogo.setObjectName(u"ctLogo")
        self.ctLogo.setFrameShape(QFrame.StyledPanel)
        self.ctLogo.setFrameShadow(QFrame.Raised)
        self.lblLogo = QLabel(self.ctLogo)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setGeometry(QRect(70, -40, 141, 171))
        self.lblLogo.setPixmap(QPixmap(u"ui\icons\Logo C.A.I.E Editada-sem fundo.png"))
        self.lblLogo.setScaledContents(True)

        self.gridLayout_4.addWidget(self.ctLogo, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.ctCabecalho)

        self.ctConteudo = QFrame(self.ctPrincipal)
        self.ctConteudo.setObjectName(u"ctConteudo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ctConteudo.sizePolicy().hasHeightForWidth())
        self.ctConteudo.setSizePolicy(sizePolicy1)
        self.ctConteudo.setStyleSheet(u"background-color: rgb(117, 117, 117)")
        self.ctConteudo.setFrameShape(QFrame.StyledPanel)
        self.ctConteudo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.ctConteudo)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidgetPaginas = QStackedWidget(self.ctConteudo)
        self.stackedWidgetPaginas.setObjectName(u"stackedWidgetPaginas")
        self.stackedWidgetPaginas.setEnabled(True)
        self.pgArquivos = QWidget()
        self.pgArquivos.setObjectName(u"pgArquivos")
        self.ctArquivo = QFrame(self.pgArquivos)
        self.ctArquivo.setObjectName(u"ctArquivo")
        self.ctArquivo.setGeometry(QRect(0, 50, 631, 210))
        self.ctArquivo.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(138, 138, 138)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(148, 148, 111);\n"
"	borde-top-left-radius: 15pix;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.ctArquivo.setFrameShape(QFrame.StyledPanel)
        self.ctArquivo.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.ctArquivo)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tblArquivos = QTableWidget(self.ctArquivo)
        if (self.tblArquivos.columnCount() < 2):
            self.tblArquivos.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblArquivos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblArquivos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblArquivos.setObjectName(u"tblArquivos")
        self.tblArquivos.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(0, 0, 0);\n"
"	font: 10pt \"MS Shel Dig 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"       color: rgb(0, 0, 0);"
"}"
"""
    QTableWidget::item:selected {
        background-color: lightblue;\n
        color: black;
    }
"""
)

        self.gridLayout_8.addWidget(self.tblArquivos, 0, 0, 1, 1)

        self.ctBotoesArquivos = QFrame(self.ctArquivo)
        self.ctBotoesArquivos.setObjectName(u"ctBotoesArquivos")
        self.ctBotoesArquivos.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(148, 148, 111);\n"
"	borde-top-left-radius: 15pix;\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 85, 0);\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.ctBotoesArquivos.setFrameShape(QFrame.StyledPanel)
        self.ctBotoesArquivos.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.ctBotoesArquivos)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btnGerarPDF = QPushButton(self.ctBotoesArquivos)
        self.btnGerarPDF.setObjectName(u"btnGerarPDF")
        self.btnGerarPDF.setMinimumSize(QSize(0, 30))
        self.btnGerarPDF.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.btnGerarPDF, 2, 0, 1, 1)

        self.btnAddArquivo = QPushButton(self.ctBotoesArquivos)
        self.btnAddArquivo.setObjectName(u"btnAddArquivo")
        self.btnAddArquivo.setMinimumSize(QSize(100, 30))
        self.btnAddArquivo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddArquivo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.btnAddArquivo, 0, 0, 1, 1)

        self.btnAbrirArquivo = QPushButton(self.ctBotoesArquivos)
        self.btnAbrirArquivo.setObjectName(u"btnAbrirArquivo")
        self.btnAbrirArquivo.setMinimumSize(QSize(0, 30))
        self.btnAbrirArquivo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.btnAbrirArquivo, 1, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 3, 0, 1, 1)


        self.gridLayout_8.addWidget(self.ctBotoesArquivos, 0, 1, 1, 1)

        self.lblArquivo = QLabel(self.pgArquivos)
        self.lblArquivo.setObjectName(u"lblArquivo")
        self.lblArquivo.setGeometry(QRect(10, 0, 621, 21))
        self.stackedWidgetPaginas.addWidget(self.pgArquivos)
        self.pgCadastrarUsuario = QWidget()
        self.pgCadastrarUsuario.setObjectName(u"pgCadastrarUsuario")
        self.ctCadastro = QFrame(self.pgCadastrarUsuario)
        self.ctCadastro.setObjectName(u"ctCadastro")
        self.ctCadastro.setGeometry(QRect(90, 20, 471, 171))
        self.ctCadastro.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(138, 138, 138)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(148, 148, 111);\n"
"	borde-top-left-radius: 15pix;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(0, 85, 0);\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.ctCadastro.setFrameShape(QFrame.StyledPanel)
        self.ctCadastro.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.ctCadastro)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.lblNomeCadastro = QLabel(self.ctCadastro)
        self.lblNomeCadastro.setObjectName(u"lblNomeCadastro")

        self.gridLayout_2.addWidget(self.lblNomeCadastro, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 4, 1, 1, 1)

        self.btnFotos = QPushButton(self.ctCadastro)
        self.btnFotos.setObjectName(u"btnFotos")
        self.btnFotos.setMinimumSize(QSize(0, 25))
        self.btnFotos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btnFotos, 5, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 4, 0, 1, 1)

        self.comboBoxAcesso = QComboBox(self.ctCadastro)
        self.comboBoxAcesso.addItem("")
        self.comboBoxAcesso.addItem("")
        self.comboBoxAcesso.addItem("")
        self.comboBoxAcesso.setObjectName(u"comboBoxAcesso")
        self.comboBoxAcesso.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.comboBoxAcesso, 3, 1, 1, 1)

        self.lineEditNome = QLineEdit(self.ctCadastro)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.lineEditNome, 2, 1, 1, 2)

        self.lblNivelAcesso = QLabel(self.ctCadastro)
        self.lblNivelAcesso.setObjectName(u"lblNivelAcesso")

        self.gridLayout_2.addWidget(self.lblNivelAcesso, 3, 0, 1, 1)

        self.lblCadastrar = QLabel(self.ctCadastro)
        self.lblCadastrar.setObjectName(u"lblCadastrar")

        self.gridLayout_2.addWidget(self.lblCadastrar, 0, 0, 1, 3)

        self.stackedWidgetPaginas.addWidget(self.pgCadastrarUsuario)
        self.pgUsuariosAtivos = QWidget()
        self.pgUsuariosAtivos.setObjectName(u"pgUsuariosAtivos")
        self.ctTabelaUsuarios = QFrame(self.pgUsuariosAtivos)
        self.ctTabelaUsuarios.setObjectName(u"ctTabelaUsuarios")
        self.ctTabelaUsuarios.setGeometry(QRect(0, 50, 631, 210))
        self.ctTabelaUsuarios.setFrameShape(QFrame.StyledPanel)
        self.ctTabelaUsuarios.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.ctTabelaUsuarios)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tbUsuariosAtivos = QTableWidget(self.ctTabelaUsuarios)
        if (self.tbUsuariosAtivos.columnCount() < 3):
            self.tbUsuariosAtivos.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbUsuariosAtivos.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbUsuariosAtivos.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbUsuariosAtivos.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.tbUsuariosAtivos.setObjectName(u"tbUsuariosAtivos")
        self.tbUsuariosAtivos.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(0, 0, 0);\n"
"	font: 10pt \"MS Shel Dig 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"       color: rgb(0, 0, 0);"
"}"
"""
    QTableWidget::item:selected {
        background-color: lightblue;\n
        color: black;
    }
"""
)

        self.gridLayout_9.addWidget(self.tbUsuariosAtivos, 0, 0, 1, 1)

        self.ctUsuarios = QFrame(self.ctTabelaUsuarios)
        self.ctUsuarios.setObjectName(u"ctUsuarios")
        self.ctUsuarios.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(148, 148, 111);\n"
"	borde-top-left-radius: 15pix;\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 85, 0);\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.ctUsuarios.setFrameShape(QFrame.StyledPanel)
        self.ctUsuarios.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.ctUsuarios)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btnAtualizarCadastro = QPushButton(self.ctUsuarios)
        self.btnAtualizarCadastro.setObjectName(u"btnAtualizarCadastro")
        self.btnAtualizarCadastro.setMinimumSize(QSize(100, 30))
        self.btnAtualizarCadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btnAtualizarCadastro)

        self.btnExcluirCadastro = QPushButton(self.ctUsuarios)
        self.btnExcluirCadastro.setObjectName(u"btnExcluirCadastro")
        self.btnExcluirCadastro.setMinimumSize(QSize(0, 30))
        self.btnExcluirCadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btnExcluirCadastro)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.gridLayout_9.addWidget(self.ctUsuarios, 0, 1, 1, 1)

        self.lblUsuariosAtivos = QLabel(self.pgUsuariosAtivos)
        self.lblUsuariosAtivos.setObjectName(u"lblUsuariosAtivos")
        self.lblUsuariosAtivos.setGeometry(QRect(20, 5, 591, 21))
        self.stackedWidgetPaginas.addWidget(self.pgUsuariosAtivos)
        self.pgRelUsuarios = QWidget()
        self.pgRelUsuarios.setObjectName(u"pgRelUsuarios")
        self.lblRelUsuarios = QLabel(self.pgRelUsuarios)
        self.lblRelUsuarios.setObjectName(u"lblRelUsuarios")
        self.lblRelUsuarios.setGeometry(QRect(10, 10, 621, 21))
        self.frameRelUsuarios = QFrame(self.pgRelUsuarios)
        self.frameRelUsuarios.setObjectName(u"frameRelUsuarios")
        self.frameRelUsuarios.setGeometry(QRect(0, 50, 631, 210))
        self.frameRelUsuarios.setFrameShape(QFrame.StyledPanel)
        self.frameRelUsuarios.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frameRelUsuarios)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tbRelUsuarios = QTableWidget(self.frameRelUsuarios)
        if (self.tbRelUsuarios.columnCount() < 3):
            self.tbRelUsuarios.setColumnCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbRelUsuarios.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbRelUsuarios.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbRelUsuarios.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        self.tbRelUsuarios.setObjectName(u"tbRelUsuarios")
        self.tbRelUsuarios.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(0, 0, 0);\n"
"	font: 10pt \"MS Shel Dig 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"       color: rgb(0, 0, 0);"
"}"
"""
    QTableWidget::item:selected {
        background-color: lightblue;\n
        color: black;
    }
"""
)

        self.gridLayout_7.addWidget(self.tbRelUsuarios, 0, 0, 1, 1)

        self.frameBtnRelUsuarios = QFrame(self.frameRelUsuarios)
        self.frameBtnRelUsuarios.setObjectName(u"frameBtnRelUsuarios")
        self.frameBtnRelUsuarios.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(148, 148, 111);\n"
"	borde-top-left-radius: 15pix;\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 85, 0);\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.frameBtnRelUsuarios.setFrameShape(QFrame.StyledPanel)
        self.frameBtnRelUsuarios.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frameBtnRelUsuarios)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btnRelUsuariosPDF = QPushButton(self.frameBtnRelUsuarios)
        self.btnRelUsuariosPDF.setObjectName(u"btnRelUsuariosPDF")
        self.btnRelUsuariosPDF.setMinimumSize(QSize(80, 30))
        self.btnRelUsuariosPDF.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btnRelUsuariosPDF)

        self.btnRelUsuariosExcel = QPushButton(self.frameBtnRelUsuarios)
        self.btnRelUsuariosExcel.setObjectName(u"btnRelUsuariosExcel")
        self.btnRelUsuariosExcel.setMinimumSize(QSize(60, 30))
        self.btnRelUsuariosExcel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btnRelUsuariosExcel)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)


        self.gridLayout_7.addWidget(self.frameBtnRelUsuarios, 0, 1, 1, 1)

        self.stackedWidgetPaginas.addWidget(self.pgRelUsuarios)
        self.pgRelAcessos = QWidget()
        self.pgRelAcessos.setObjectName(u"pgRelAcessos")
        self.frameRelAcessos = QFrame(self.pgRelAcessos)
        self.frameRelAcessos.setObjectName(u"frameRelAcessos")
        self.frameRelAcessos.setGeometry(QRect(10, 50, 631, 210))
        self.frameRelAcessos.setFrameShape(QFrame.StyledPanel)
        self.frameRelAcessos.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frameRelAcessos)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tbRelAcessos = QTableWidget(self.frameRelAcessos)
        if (self.tbRelAcessos.columnCount() < 5):
            self.tbRelAcessos.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbRelAcessos.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbRelAcessos.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbRelAcessos.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbRelAcessos.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbRelAcessos.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.tbRelAcessos.setObjectName(u"tbRelAcessos")
        self.tbRelAcessos.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(0, 0, 0);\n"
"	font: 10pt \"MS Shel Dig 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"       color: rgb(0, 0, 0);"
"}"
"""
    QTableWidget::item:selected {
        background-color: lightblue;\n
        color: black;
    }
"""
)

        self.gridLayout_6.addWidget(self.tbRelAcessos, 0, 0, 1, 1)

        self.frameBtnRelAcessos = QFrame(self.frameRelAcessos)
        self.frameBtnRelAcessos.setObjectName(u"frameBtnRelAcessos")
        self.frameBtnRelAcessos.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(148, 148, 111);\n"
"	borde-top-left-radius: 15pix;\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 85, 0);\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.frameBtnRelAcessos.setFrameShape(QFrame.StyledPanel)
        self.frameBtnRelAcessos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frameBtnRelAcessos)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btnRelAcessosPDF = QPushButton(self.frameBtnRelAcessos)
        self.btnRelAcessosPDF.setObjectName(u"btnRelAcessosPDF")
        self.btnRelAcessosPDF.setMinimumSize(QSize(80, 30))
        self.btnRelAcessosPDF.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.btnRelAcessosPDF)

        self.btnRelAcessosExcel = QPushButton(self.frameBtnRelAcessos)
        self.btnRelAcessosExcel.setObjectName(u"btnRelAcessosExcel")
        self.btnRelAcessosExcel.setMinimumSize(QSize(80, 30))
        self.btnRelAcessosExcel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.btnRelAcessosExcel)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_6)


        self.gridLayout_6.addWidget(self.frameBtnRelAcessos, 0, 1, 1, 1)

        self.lblRelAcessos = QLabel(self.pgRelAcessos)
        self.lblRelAcessos.setObjectName(u"lblRelAcessos")
        self.lblRelAcessos.setGeometry(QRect(10, 6, 621, 20))
        self.stackedWidgetPaginas.addWidget(self.pgRelAcessos)

        self.verticalLayout_5.addWidget(self.stackedWidgetPaginas)


        self.verticalLayout.addWidget(self.ctConteudo)


        self.horizontalLayout.addWidget(self.ctPrincipal)

        TelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaPrincipal)

        self.toolboxMenu.setCurrentIndex(1)
        self.stackedWidgetPaginas.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(TelaPrincipal)
    # setupUi

    def retranslateUi(self, TelaPrincipal):
        TelaPrincipal.setWindowTitle(QCoreApplication.translate("TelaPrincipal", u"MainWindow", None))
        self.lblTitulo_2.setText(QCoreApplication.translate("TelaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">C.A.I.E</span></p></body></html>", None))
        self.btnArquivos.setText(QCoreApplication.translate("TelaPrincipal", u"Arquivos", None))
        self.btnCadastrarUsuario.setText(QCoreApplication.translate("TelaPrincipal", u"Cadastrar Usu\u00e1rio", None))
        self.btnUsuriosAtivos.setText(QCoreApplication.translate("TelaPrincipal", u"Usu\u00e1rios Ativos", None))
        self.toolboxMenu.setItemText(self.toolboxMenu.indexOf(self.page), QCoreApplication.translate("TelaPrincipal", u"Arquivos e Usu\u00e1rios", None))
        self.btnRelUsuarios.setText(QCoreApplication.translate("TelaPrincipal", u"Relat\u00f3rio de Usu\u00e1rios", None))
        self.btnRelAcessos.setText(QCoreApplication.translate("TelaPrincipal", u"Relat\u00f3rio de Acessos", None))
        self.toolboxMenu.setItemText(self.toolboxMenu.indexOf(self.page_2), QCoreApplication.translate("TelaPrincipal", u"Relat\u00f3rios", None))
        self.lblTitulo.setText(QCoreApplication.translate("TelaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">C.A.I.E.</span></p></body></html>", None))
        self.lblAcesso.setText(QCoreApplication.translate("TelaPrincipal", u"TextLabel", None))
        self.btnMenu.setText("")
        self.lblNome.setText(QCoreApplication.translate("TelaPrincipal", u"TextLabel", None))
        self.lblID.setText(QCoreApplication.translate("TelaPrincipal", u"TextLabel", None))
        self.lblLogo.setText("")
        ___qtablewidgetitem = self.tblArquivos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaPrincipal", u"Nome", None));
        ___qtablewidgetitem1 = self.tblArquivos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaPrincipal", u"N\u00edvel de Acesso", None));
        self.btnGerarPDF.setText(QCoreApplication.translate("TelaPrincipal", u"Gerar PDF", None))
        self.btnAddArquivo.setText(QCoreApplication.translate("TelaPrincipal", u"Adicionar Arquivo", None))
        self.btnAbrirArquivo.setText(QCoreApplication.translate("TelaPrincipal", u"AbrirArquivo", None))
        self.lblArquivo.setText(QCoreApplication.translate("TelaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Arquivos</span></p></body></html>", None))
        self.lblNomeCadastro.setText(QCoreApplication.translate("TelaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Nome:</span></p></body></html>", None))
        self.btnFotos.setText(QCoreApplication.translate("TelaPrincipal", u"Tirar Fotos", None))
        self.comboBoxAcesso.setItemText(0, QCoreApplication.translate("TelaPrincipal", u"1", None))
        self.comboBoxAcesso.setItemText(1, QCoreApplication.translate("TelaPrincipal", u"2", None))
        self.comboBoxAcesso.setItemText(2, QCoreApplication.translate("TelaPrincipal", u"3", None))

        self.lineEditNome.setStyleSheet("color: black;")
        self.lineEditNome.setPlaceholderText(QCoreApplication.translate("TelaPrincipal", u"Nome", None))
        self.lblNivelAcesso.setText(QCoreApplication.translate("TelaPrincipal", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">N\u00edvel de Acesso:</span></p></body></html>", None))
        self.lblCadastrar.setText(QCoreApplication.translate("TelaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Novo Cadastro</span></p></body></html>", None))
        ___qtablewidgetitem2 = self.tbUsuariosAtivos.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaPrincipal", u"ID", None));
        ___qtablewidgetitem3 = self.tbUsuariosAtivos.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TelaPrincipal", u"Nome", None));
        ___qtablewidgetitem4 = self.tbUsuariosAtivos.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TelaPrincipal", u"N\u00edvel de Acesso", None));
        self.btnAtualizarCadastro.setText(QCoreApplication.translate("TelaPrincipal", u"Atualizar Cadastro", None))
        self.btnExcluirCadastro.setText(QCoreApplication.translate("TelaPrincipal", u"Excluir Cadastro", None))
        self.lblUsuariosAtivos.setText(QCoreApplication.translate("TelaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Usu\u00e1rios Ativos</span></p></body></html>", None))
        self.lblRelUsuarios.setText(QCoreApplication.translate("TelaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Relat\u00f3rio de Usu\u00e1rios Ativos</span></p></body></html>", None))
        ___qtablewidgetitem5 = self.tbRelUsuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TelaPrincipal", u"ID", None));
        ___qtablewidgetitem6 = self.tbRelUsuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TelaPrincipal", u"Nome", None));
        ___qtablewidgetitem7 = self.tbRelUsuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TelaPrincipal", u"N\u00edvel de Acesso", None));
        self.btnRelUsuariosPDF.setText(QCoreApplication.translate("TelaPrincipal", u"Gerar PDF", None))
        self.btnRelUsuariosExcel.setText(QCoreApplication.translate("TelaPrincipal", u"Gerar Excel", None))
        ___qtablewidgetitem8 = self.tbRelAcessos.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TelaPrincipal", u"ID", None));
        ___qtablewidgetitem9 = self.tbRelAcessos.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TelaPrincipal", u"Nome", None));
        ___qtablewidgetitem10 = self.tbRelAcessos.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("TelaPrincipal", u"N\u00edvel de Acesso", None));
        ___qtablewidgetitem11 = self.tbRelAcessos.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("TelaPrincipal", u"Arquivo", None));
        ___qtablewidgetitem12 = self.tbRelAcessos.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("TelaPrincipal", u"Data de Acesso", None));
        self.btnRelAcessosPDF.setText(QCoreApplication.translate("TelaPrincipal", u"Gerar PDF", None))
        self.btnRelAcessosExcel.setText(QCoreApplication.translate("TelaPrincipal", u"Gerar Excel", None))
        self.lblRelAcessos.setText(QCoreApplication.translate("TelaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Relat\u00f3rio de Acessos</span></p></body></html>", None))
    # retranslateUi

