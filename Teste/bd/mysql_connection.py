import mysql.connector

# Configurações de conexão
def criar_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",  
        database="controle_acesso" 
    )
