from ast import Store
from pathlib import Path
from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QTableWidgetItem, QMessageBox, QFileDialog, QInputDialog, QAbstractItemView)
from PySide6.QtGui import QIcon
from fpdf import FPDF
from ui_main import Ui_TelaPrincipal
from PySide6 import QtCore
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bd.operacoes_funcionario
import bd.operacoes_documento
import pandas as pd


class MainWindow(QMainWindow, Ui_TelaPrincipal):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("C.A.I.E")
        self.stackedWidgetPaginas.setCurrentWidget(self.pgArquivos)
        self.toolboxMenu.setCurrentWidget(self.page)
        appIcon = QIcon(u"ui\icons\Logo C.A.I.E Editada-sem fundo.png")
        self.setWindowIcon(appIcon)

        
    
        #####################################################
        #Botão menu
        self.btnMenu.clicked.connect(self.LeftMenu)

        #####################################################
        #Páginas do sistema
        self.btnArquivos.clicked.connect(lambda: self.stackedWidgetPaginas.setCurrentWidget(self.pgArquivos))
        self.btnCadastrarUsuario.clicked.connect(lambda: self.stackedWidgetPaginas.setCurrentWidget(self.pgCadastrarUsuario))
        self.btnUsuriosAtivos.clicked.connect(lambda: self.stackedWidgetPaginas.setCurrentWidget(self.pgUsuariosAtivos))
        self.btnRelUsuarios.clicked.connect(lambda: self.stackedWidgetPaginas.setCurrentWidget(self.pgRelUsuarios))
        self.btnRelAcessos.clicked.connect(lambda: self.stackedWidgetPaginas.setCurrentWidget(self.pgRelAcessos))

        ####################################################
        #Botões/Tabelas do sistema
        self.btnAtualizarCadastro.clicked.connect(self.atualizar_funcionarios)
        self.btnExcluirCadastro.clicked.connect(self.excluir_funcionarios)
        self.btnAddArquivo.clicked.connect(self.inserir_documento)
        self.btnAbrirArquivo.clicked.connect(self.abrir_documento)
        self.btnGerarPDF.clicked.connect(self.gerar_pdf_documentos)
        self.btnFotos.clicked.connect(self.inserir_funcionario)
        self.btnRelAcessosExcel.clicked.connect(self.gerar_excel_auditoria)
        self.btnRelUsuariosExcel.clicked.connect(self.gerar_excel_usuarios)
        self.btnRelUsuariosPDF.clicked.connect(self.gerar_pdf_usuarios)
        self.btnRelAcessosPDF.clicked.connect(self.gerar_pdf_acessos)
        self.tblArquivos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbUsuariosAtivos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbRelUsuarios.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbRelAcessos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        ###################################################
        #Funções para serem chamadas na inicialização da interface
        self.buscar_funcionarios()
        self.buscar_documentos()
        self.buscar_funcionarios_relatorio()
        self.buscar_auditoria()
        self.tbUsuariosAtivos.itemChanged.connect(self.item_modificado)
        
        
    # Define as permissões de botões e telas do funcionário autenticado de acordo com o nível 1, 2 ou 3
    def definir_permissoes(self):

        nivel_acesso = int(self.lblAcesso.text().replace("Nível de Acesso: ", ""))

        if nivel_acesso == 1:
            self.btnGerarPDF.setEnabled(True)
            self.btnArquivos.setEnabled(True)
            self.btnCadastrarUsuario.setEnabled(False)
            self.btnRelAcessos.setEnabled(False)
            self.btnRelUsuarios.setEnabled(False)
            self.btnAddArquivo.setEnabled(False)
            self.btnUsuriosAtivos.setEnabled(False)

        elif nivel_acesso == 2:
            self.btnGerarPDF.setEnabled(True)
            self.btnCadastrarUsuario.setEnabled(True)
            self.btnRelAcessos.setEnabled(True)
            self.btnRelUsuarios.setEnabled(True)
            self.btnRelAcessosExcel.setEnabled(False)
            self.btnRelUsuariosExcel.setEnabled(False)
            

        elif nivel_acesso == 3:
            self.btnGerarPDF.setEnabled(True)
            self.btnCadastrarUsuario.setEnabled(True)
            self.btnRelAcessos.setEnabled(True)
            self.btnRelUsuarios.setEnabled(True)

    # Preenche a tabela de usuários ativos com os registros da tabela funcionários do banco de dados
    def buscar_funcionarios(self):
        resultado = bd.operacoes_funcionario.mostrar_funcionarios()
        self.tbUsuariosAtivos.clearContents()
        self.tbUsuariosAtivos.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tbUsuariosAtivos.setItem(row, column, QTableWidgetItem(str(data)))
    
    linhas_modificadas = []

    # Função para lidar com a alteração de itens na tabela de usuários ativos
    def item_modificado(self, item):
        row = item.row()  # A linha modificada
        if row not in self.linhas_modificadas:
            self.linhas_modificadas.append(row)

    # Preenche a tabela de relatório de usuários com os registros da tabela funcionários do banco de dados
    def buscar_funcionarios_relatorio(self):
        resultado = bd.operacoes_funcionario.mostrar_funcionarios()
        self.tbRelUsuarios.clearContents()
        self.tbRelUsuarios.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tbRelUsuarios.setItem(row, column, QTableWidgetItem(str(data)))
    
    # Atualiza os registros da tabela de usuários ativos
    def atualizar_funcionarios(self):

        nivel_acesso = int(self.lblAcesso.text().replace("Nível de Acesso: ", ""))
        acesso_negado = False

        # Itera apenas sobre as linhas modificadas
        for row in self.linhas_modificadas:
            dados_funcionario = []
        
            # Coleta os dados da linha
            for column in range(self.tbUsuariosAtivos.columnCount()):
                item = self.tbUsuariosAtivos.item(row, column)
                if item is not None:
                    
                    dados_funcionario.append(item.text())

            id_funcionario = dados_funcionario[0]  # ID na primeira coluna
            nome = dados_funcionario[1]  # Nome na segunda coluna
            nivel = int(dados_funcionario[2])  # Nível na terceira coluna


            if nivel_acesso == 2:
            # Se o nível de acesso é 2, não permite a alteração do nível para 3
                if nivel == 3:
                    acesso_negado = True
                    break  # Sai do loop, pois não pode promover para nível 3


            # Verifica se o usuário tem permissão para atualizar a linha
            if nivel_acesso == 2 and nivel in [1, 2]:  # Usuário nível 2 pode atualizar nível 1 e 2
                bd.operacoes_funcionario.atualizar_cadastro(id_funcionario, nome, nivel)
            elif nivel_acesso == 3:  # Usuário nível 3 pode atualizar qualquer nível
                bd.operacoes_funcionario.atualizar_cadastro(id_funcionario, nome, nivel)
            else:
                # Se o nível de acesso não permitir, define acesso_negado como True
                acesso_negado = True
                break  # Encerra o loop assim que encontrar uma linha sem permissão

        if acesso_negado:
            QMessageBox.warning(self, "Acesso Negado", "Você não tem permissão para atualizar um cadastro de Nível 3.")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Atualização de Dados")
            msg.setText("Cadastros atualizados com sucesso!")
            msg.exec()

        self.tbUsuariosAtivos.reset()
        self.buscar_funcionarios()

        # Limpa a lista de linhas modificadas após a atualização
        self.linhas_modificadas.clear()

    # Exclui um funcionário da tabela de usuários ativos
    def excluir_funcionarios(self):
        id_funcionario = self.tbUsuariosAtivos.selectionModel().currentIndex().siblingAtColumn(0).data()
        nivel_acesso = int(self.lblAcesso.text().replace("Nível de Acesso: ", ""))
        
        
        funcionario = bd.operacoes_funcionario.obter_funcionario_por_id(id_funcionario)
        if funcionario:
            id_funcionario, nome_funcionario, nivel_funcionario = funcionario

            if nivel_acesso == 2 and nivel_funcionario == 3:  # Nível 2 não pode excluir nível 3
                QMessageBox.warning(self, "Acesso Negado", "Você não tem permissão para excluir este cadastro.")
                return  # Interrompe a exclusão
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Exclusão de Dados")
                msg.setText("O registro será excluido")
                msg.setInformativeText("Você tem certeza que deseja excluir estre registro?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                resposta = msg.exec()

                if resposta == QMessageBox.Yes:
                    id_funcionario = self.tbUsuariosAtivos.selectionModel().currentIndex().siblingAtColumn(0).data()
                    resultado = bd.operacoes_funcionario.excluir_cadastro(id_funcionario)
                    self.buscar_funcionarios()
                    self.buscar_funcionarios_relatorio()

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("FUNCIONARIOS")
                    msg.setText(resultado)
                    msg.exec()

    # Adiciona um novo documento na tabela de arquivos
    def inserir_documento(self):
        # Abre o explorador de arquivos para escolher o arquivo
        caminho_arquivo, _ = QFileDialog.getOpenFileName(None, "Selecionar arquivo", "", "Todos os Arquivos (*)")
        
        if not caminho_arquivo:
            QMessageBox.warning(None, "Seleção de Arquivo", "Nenhum arquivo selecionado.")
            return

        # Solicita o nome do documento
        nome_documento, ok_nome = QInputDialog.getText(None, "Nome do Documento", "Digite o nome do documento:")
        if not ok_nome or not nome_documento:
            QMessageBox.warning(None, "Nome do Documento", "O nome do documento é obrigatório.")
            return

        # Solicita o nível mínimo de acesso
        nivel_acesso, ok_acesso = QInputDialog.getInt(None, "Nível de Acesso", "Digite o nível mínimo de acesso (1 a 3):", 1, 1, 3)
        if not ok_acesso:
            QMessageBox.warning(None, "Nível de Acesso", "O nível de acesso é obrigatório.")
            return

        # Chama a função para adicionar o documento ao banco
        bd.operacoes_documento.adicionar_documento(nome_documento, caminho_arquivo, nivel_acesso)
        QMessageBox.information(None, "Sucesso", "Documento adicionado com sucesso.")

        self.tblArquivos.reset()
        self.buscar_documentos()

    # Abre o documento selecionado na tabela de arquivos
    def abrir_documento(self):
        nome_documento = self.tblArquivos.selectionModel().currentIndex().siblingAtColumn(0).data()
        documento = bd.operacoes_documento.obter_documento_por_nome(nome_documento)

        if documento:
            id_documento, nome_documento, nivel_arquivo = documento
            nivel_acesso = int(self.lblAcesso.text().replace("Nível de Acesso: ", ""))

            # Verifica se o usuário tem o nível necessário para acessar o arquivo selecionado
            if nivel_acesso >= nivel_arquivo:
                bd.operacoes_documento.abrir_documento_em_janela(nome_documento)
                self.inserir_auditoria()
                self.tbRelAcessos.reset()
                self.buscar_auditoria()
            else:
                QMessageBox.warning(self, "Acesso negado", "Você não tem permissão para acessar este arquivo.")
        else:
            QMessageBox.warning(self, "Erro", "Documento não encontrado.") 

    # Preenche a tabela de arquivos com os registros da tabela documentos do banco de dados
    def buscar_documentos(self):
        resultado = bd.operacoes_documento.mostrar_documentos()
        self.tblArquivos.clearContents()
        self.tblArquivos.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tblArquivos.setItem(row, column, QTableWidgetItem(str(data)))
    
    # Gera um PDF do documento selecionado na tabela de arquivos
    def gerar_pdf_documentos(self):
        nome_documento = self.tblArquivos.selectionModel().currentIndex().siblingAtColumn(0).data()
        documento = bd.operacoes_documento.obter_documento_por_nome(nome_documento)

        if documento:
            id_documento, nome_documento, nivel_arquivo = documento
            nivel_acesso = int(self.lblAcesso.text().replace("Nível de Acesso: ", ""))

            if nivel_acesso >= nivel_arquivo:
                # Permite a transformação em PDF, pois o nível do usuário é suficiente
                bd.operacoes_documento.converter_pdf(nome_documento)
                QMessageBox.information(self, "Sucesso", "Documento transformado em PDF com sucesso.")
            else:
                # Mostra uma mensagem informando que o acesso é negado para essa operação
                QMessageBox.warning(self, "Acesso negado", "Você não tem permissão para transformar este arquivo em PDF.")
        else:
            QMessageBox.warning(self, "Erro", "Documento não encontrado.")

    # Configura a combobox da página de cadastro de acordo com o nível do usuário autenticado
    def configurar_combobox_nivel(self):
        # Obtém o nível de acesso do usuário atual
        nivel_acesso = int(self.lblAcesso.text().replace("Nível de Acesso: ", ""))
    
        # Limpa todas as opções da ComboBox e adicione apenas as permitidas
        self.comboBoxAcesso.clear()
    
        # Adiciona níveis de acesso disponíveis
        if nivel_acesso == 2:
            # Usuário nível 2 pode cadastrar apenas níveis 1 e 2
            self.comboBoxAcesso.addItems(["1", "2"])
        elif nivel_acesso == 3:
            # Usuário nível 3 pode cadastrar qualquer nível
            self.comboBoxAcesso.addItems(["1", "2", "3"])

    # Cadastra um novo funcionário e atualiza a tabela de usuários ativos para mostrar os registros já com o novo funcionário cadastrado
    def inserir_funcionario(self):
        texto_caixa = self.lineEditNome.text()  # Recupera o texto do QLineEdit
        item_selecionado = self.comboBoxAcesso.currentText()

        if item_selecionado == "1":
            nivel_acesso = 1
        elif item_selecionado == "2":
            nivel_acesso = 2
        else:
            nivel_acesso = 3

        bd.operacoes_funcionario.cadastrar_usuario(texto_caixa, nivel_acesso)
        self.tbUsuariosAtivos.reset()
        self.buscar_funcionarios()

    # Atualiza as labels do cabeçalho com as informações do usuário autenticado
    def atualizar_dados(self, id_funcionario, nome_funcionario, nivel_acesso):
        self.lblID.setText(f"ID: {id_funcionario}")
        self.lblNome.setText(f"Nome: {nome_funcionario}")
        self.lblAcesso.setText(f"Nível de Acesso: {nivel_acesso}")

    # Insere no banco de dados o registro de acesso ao documento selecionado na tabela de arquivos
    def inserir_auditoria(self):
        nome_documento = self.tblArquivos.selectionModel().currentIndex().siblingAtColumn(0).data()
        id_documento = bd.operacoes_documento.obter_id_documento(nome_documento)
        
        id_funcionario = int(self.lblID.text().replace("ID: ", ""))
        nome_funcionario = self.lblNome.text().replace("Nome: ", "")
        nivel_acesso = int(self.lblAcesso.text().replace("Nível de Acesso: ", ""))

        bd.operacoes_documento.inserir_log_auditoria(id_funcionario, nome_funcionario, nivel_acesso, id_documento)

    # Preenche a tabela de relatório de acessos com os registros da tabela auditoria do banco de dados
    def buscar_auditoria(self):
        resultado = bd.operacoes_documento.mostrar_logs_auditoria()
        self.tbRelAcessos.clearContents()
        self.tbRelAcessos.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tbRelAcessos.setItem(row, column, QTableWidgetItem(str(data)))

    # Gera um arquivo Excel dos dados da tabela de relatório de acessos
    def gerar_excel_auditoria(self):
        dados = []
        all_dados = []

        # Pega cada linha da tabela e adiciona na variável all_dados
        for row in range(self.tbRelAcessos.rowCount()):
            for column in range(self.tbRelAcessos.columnCount()):
                dados.append(self.tbRelAcessos.item(row, column).text())

            all_dados.append(dados)
            dados = [0]

        # Define as colunas do Data Frame
        columns = ['ID', 'ID_FUNCIONARIO', 'NOME_FUNCIONARIO', 'NIVEL_ACESSO', 'ID_DOCUMENTO', 'DATA_ACESSO']

        # Define o nome e caminho do documento (Downloads)
        nome_documento = "RelatorioAcessos"
        downloads_path = Path.home() / "Downloads" / f"{nome_documento}.xlsx"

        # Transforma em Data Frame e salva na pasta Downloads do computador
        relatorio_acessos = pd.DataFrame(all_dados, columns = columns)
        relatorio_acessos.to_excel(downloads_path, sheet_name="relatorio_acessos", index=False)
        print(f"Relatório de acessos salvo em: {downloads_path}")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

    # Gera um arquivo Excel dos dados da tabela de relatório de usuários ativos
    def gerar_excel_usuarios(self):
        
        all_dados = []

        # Pega cada linha da tabela e adiciona na variável all_dados
        for row in range(self.tbRelUsuarios.rowCount()):
            dados = []
            for column in range(self.tbRelUsuarios.columnCount()):
                dados.append(self.tbRelUsuarios.item(row, column).text())

            all_dados.append(dados)
            
        # Define as colunas do Data Frame
        columns = ['ID_FUNCIONARIO', 'NOME_FUNCIONARIO', 'NIVEL_ACESSO']

        # Define o nome e caminho do documento (Downloads)
        nome_documento = "RelatorioUsuarios"
        downloads_path = Path.home() / "Downloads" / f"{nome_documento}.xlsx"

        # Transforma em Data Frame e salva na pasta Downloads do computador
        relatorio_usuarios = pd.DataFrame(all_dados, columns = columns)
        relatorio_usuarios.to_excel(downloads_path, sheet_name="relatorio_usuarios", index=False)
        print(f"Relatório de usuarios salvo em: {downloads_path}")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

    # Gera um PDF dos dados da tabela de relatório de usuários ativos
    def gerar_pdf_usuarios(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Relatório de Usuários", ln=True, align="C")

        # Define os títulos das colunas
        pdf.set_font("Arial", style="B", size=10)
        pdf.cell(30, 10, "ID", border=1)
        pdf.cell(60, 10, "Nome", border=1)
        pdf.cell(30, 10, "Nível de Acesso", border=1)
        pdf.ln()  # Quebra de linha para a próxima linha de dados

        # Adiciona os dados da tabela
        pdf.set_font("Arial", size=10)
        for row in range(self.tbRelUsuarios.rowCount()):
            for column in range(self.tbRelUsuarios.columnCount()):
                item = self.tbRelUsuarios.item(row, column)
                if item is not None:
                    pdf.cell(60 if column == 1 else 30, 10, item.text(), border=1)  # Ajuste do tamanho da célula
                else:
                    pdf.cell(60 if column == 1 else 30, 10, "", border=1)
            pdf.ln()

        # Salva o arquivo PDF na pasta de Downloads
        downloads_path = Path.home() / "Downloads" / "RelatorioUsuarios.pdf"
        pdf.output(str(downloads_path))  # Converte o caminho para string para evitar problemas

        # Exibe mensagem de sucesso
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("PDF")
        msg.setText("Relatório PDF gerado com sucesso!")
        msg.exec()

    # Gera um PDF dos dados da tabela de relatório de acessos
    def gerar_pdf_acessos(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Relatório de Acessos", ln=True, align="C")

        # Define os títulos das colunas
        pdf.set_font("Arial", style="B", size=10)
        pdf.cell(35, 10, "ID_funcionario", border=1)
        pdf.cell(40, 10, "Nome_funcionario", border=1)
        pdf.cell(35, 10, "Nível de Acesso", border=1)
        pdf.cell(35, 10, "ID_documento", border=1)
        pdf.cell(35, 10, "Data de Acesso", border=1)
        pdf.ln()  # Quebra de linha para a próxima linha de dados

        # Adiciona os dados da tabela
        pdf.set_font("Arial", size=10)
        for row in range(self.tbRelAcessos.rowCount()):
            for column in range(self.tbRelAcessos.columnCount()):
                item = self.tbRelAcessos.item(row, column)
                if item is not None:
                    pdf.cell(40 if column == 1 else 35, 10, item.text(), border=1)  # Ajuste do tamanho da célula
                else:
                    pdf.cell(40 if column == 1 else 35, 10, "", border=1)
            pdf.ln()

        # Salva o arquivo PDF na pasta de Downloads
        downloads_path = Path.home() / "Downloads" / "RelatorioAcessos.pdf"
        pdf.output(str(downloads_path))  # Converte o caminho para string para evitar problemas

        # Exibe mensagem de sucesso
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("PDF")
        msg.setText("Relatório PDF gerado com sucesso!")
        msg.exec()


    def LeftMenu(self):
        width = self.ctEsquerda.width()

        if width == 2:
            newWidth = 200
        else:
            newWidth = 2

        self.animation = QtCore.QPropertyAnimation(self.ctEsquerda, b"maximumWidth") # type: ignore
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()