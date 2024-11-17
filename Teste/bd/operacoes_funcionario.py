import os
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))
from mysql_connection import criar_conexao


# Insere um novo usuario na tabela funcionários do banco de dados
def cadastrar_usuario(nome_funcionario, nivel_acesso):
    # Validação dos dados
    if not nome_funcionario or nivel_acesso not in [1, 2, 3]:
        print("Nome e nível de acesso são obrigatórios e devem ser válidos.")
        return

    # Conecta ao banco de dados
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        # Insere o usuário no banco de dados, mas sem confirmar se as fotos foram tiradas com sucesso
        sql = "INSERT INTO funcionarios (nome_funcionario, nivel_acesso) VALUES (%s, %s)"
        cursor.execute(sql, (nome_funcionario, nivel_acesso))
        
        # Captura o ID recém-gerado
        user_id = cursor.lastrowid

        # Executa o script para captura de fotos, passando o user_id como parâmetro
        resultado_fotos = subprocess.run(["python", "Camera.py", str(user_id)])

        # Verifica se o processo de captura foi bem-sucedido
        if resultado_fotos.returncode == 0:
            conexao.commit()  # Confirma a inserção no banco de dados
            print(f"Usuário '{nome_funcionario}' cadastrado com sucesso com ID: {user_id}")
            resultado_treinamento = subprocess.run(["python", "Treinamento.py"]) #Treina o reconhecedor com as novas fotos do usuário cadastrado
            if resultado_treinamento.returncode == 0:
                print("Treinamento completo!")
            else:
                print("Erro no treinameno")
        else:
            conexao.rollback()  # Reverte a inserção se houve erro na captura das fotos
            print("Erro na captura de fotos. Cadastro não realizado.")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao cadastrar o usuário: {e}")
    finally:
        cursor.close()
        conexao.close()

# Atualiza os cadastros no banco de dados
def atualizar_cadastro(id_funcionario, nome_funcionario, nivel_acesso):
    sql = "UPDATE funcionarios SET nome_funcionario = %s, nivel_acesso = %s WHERE id_funcionario = %s"
    valores = (nome_funcionario, nivel_acesso, id_funcionario)

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

# Exclui um cadastro do banco de dados
def excluir_cadastro(id_funcionario):
    sql = f"DELETE FROM funcionarios WHERE id_funcionario = {id_funcionario}"
    
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    conexao.close()

    # Treina o reconhecedor novamente
    subprocess.run(["python", "C:\\Users\\Julea\\Documents\\APS_6\\Teste\\Teste\\Teste\\Treinamento.py"])

    return "O registro foi excluído com sucesso!"

# Retorna todos os funcionários cadastrados na tabela funcionarios do banco de dados
def mostrar_funcionarios():
    sql = "SELECT * FROM funcionarios"

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

# Retorna o nome do funcionário a partir do id
def mostrar_nome_funcionario(id_funcionario):
    sql = "SELECT nome_funcionario FROM funcionarios WHERE id_funcionario = %s"
    valores = (id_funcionario,)

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql, (valores))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

# Retorna o nível de acesso do funcionário a partir do id
def obter_nivel_acesso(id_funcionario):
    sql = "SELECT nivel_acesso FROM funcionarios WHERE id_funcionario = %s"
    valores = (id_funcionario,)

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql, (valores))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

# Retorna um funcionário a partir do id
def obter_funcionario_por_id(id_funcionario):
    sql = "SELECT * FROM funcionarios WHERE id_funcionario = %s"
    valores = (id_funcionario,)

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(sql, (valores))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado