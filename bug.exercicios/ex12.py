import sqlite3
def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO escolas(nome) VALUES (?)", (nome,))
    conexao.commit()
    conexao.close()

#  a conexao deveria ser feita dentro da funcao