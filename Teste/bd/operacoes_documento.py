from mysql_connection import criar_conexao
import tkinter as tk
from tkinter import scrolledtext
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import chardet

# Adiciona documento no banco de dados
def adicionar_documento(nome_documento, caminho_arquivo, nivel_arquivo):
    # Abrir o arquivo em modo binário
    with open(caminho_arquivo, "rb") as arquivo:
        conteudo = arquivo.read()

    # SQL para inserir o arquivo no banco de dados
    sql = "INSERT INTO documentos (nome_documento, nivel_minimo_acesso, conteudo) VALUES (%s, %s, %s)"
    valores = (nome_documento, nivel_arquivo , conteudo)

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

# Abre o documento na janela do tkinter
def abrir_documento_em_janela(nome_documento):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    sql = "SELECT nome_documento, conteudo FROM documentos WHERE nome_documento = %s"
    cursor.execute(sql, (nome_documento,))
    resultado = cursor.fetchone()

    if resultado:
        nome_documento, conteudo = resultado

        # Cria uma nova janela usando tkinter
        janela = tk.Tk()
        janela.title(nome_documento)
        
        # Cria uma área de texto com barra de rolagem
        area_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=60, height=20)
        area_texto.pack(expand=True, fill='both')
        
        # Tenta decodificar o conteúdo para exibir como texto
        try:
            texto = conteudo.decode("utf-8")
            area_texto.insert(tk.INSERT, texto)
        except UnicodeDecodeError:
            area_texto.insert(tk.INSERT, "[Arquivo contém dados binários não exibíveis como texto]")

        # Torna a área de texto somente leitura
        area_texto.config(state=tk.DISABLED)
        
        # Inicia a interface gráfica
        janela.mainloop()
    else:
        print("Documento não encontrado.")


    cursor.close()
    conexao.close()

# Insere registros de log de acessos aos documentos na tabela auditoria do banco de dados
def inserir_log_auditoria(id_funcionario, nome_funcionario, nivel_acesso, id_documento):
    sql = "INSERT INTO auditoria (id_funcionario, nome_funcionario, nivel_acesso, id_documento) VALUES (%s, %s, %s, %s)"
    valores = (id_funcionario, nome_funcionario, nivel_acesso, id_documento)

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

# Retorna o id do documento a partir do nome
def obter_id_documento(nome_documento):
    sql = "SELECT id_documento FROM documentos WHERE nome_documento = %s"
     
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql, (nome_documento,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado[0] if resultado else None

# Retorna todos os registros da tabela auditoria
def mostrar_logs_auditoria():
    sql = "SELECT id_funcionario, nome_funcionario, nivel_acesso, id_documento, data_acesso FROM auditoria"

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado     
     
# Retorna o documento a partir do nome
def obter_documento_por_nome(nome_documento):
    sql = "SELECT id_documento, nome_documento, nivel_minimo_acesso FROM documentos WHERE nome_documento = %s"
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql, (nome_documento,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

# Retorna todos os documentos da tabela documentos
def mostrar_documentos():
    sql = "SELECT nome_documento, nivel_minimo_acesso FROM documentos"

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

# Converte o documento em PDF a partir do nome
def converter_pdf(nome_documento):
    sql = "SELECT conteudo FROM documentos WHERE nome_documento = %s"

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql, (nome_documento,))
    resultado = cursor.fetchone()
    
    if resultado is None:
        print(f"Documento '{nome_documento}' não encontrado.")
        return
    
    conteudo_binario = resultado[0]
        
    # Verifica se o conteúdo está em bytes, então decodifica
    detected_encoding = chardet.detect(conteudo_binario)['encoding']
    print(f"Codificação detectada: {detected_encoding}")
        
    # Decodifica usando a codificação detectada
    if detected_encoding:
            conteudo_texto = conteudo_binario.decode(detected_encoding)
    else:
            print("Erro: não foi possível detectar a codificação.")
            return
        
    # Define o caminho de salvamento na pasta Downloads
    downloads_path = Path.home() / "Downloads" / f"{nome_documento}.pdf"
        
    # Configura o PDF para o tamanho A4
    c = canvas.Canvas(str(downloads_path), pagesize=A4)
    width, height = A4
    text_y_position = height - 40
    
    # Escreve o conteúdo no PDF linha a linha
    for line in conteudo_texto.splitlines():
        c.drawString(40, text_y_position, line)
        text_y_position -= 15  # Move a posição para a próxima linha
            
    # Finaliza e salva o PDF
    c.showPage()
    c.save()
        
    print(f"PDF '{nome_documento}.pdf' foi gerado e salvo em {downloads_path}")

    cursor.close()
    conexao.close()

# Retorna o conteudo do documento a partir do nome
def obter_conteudo_decumento(nome_documento):
    sql = "SELECT nome_documento, conteudo FROM documentos WHERE nome_documento = %s"
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql, (nome_documento,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado
