import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE id = ?", (id_registro,))

    print(cursor.fetchone())
    conexao.close()


# O erro e que o "?" so funcionam para valores e algo do tipo nao funcionam para nomes de tabelas