import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS escolas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL
                   )
                   ''')
   
    # Faltou o conexao.commit() para salvar as alteracoes
    conexao.commit()
    conexao.close()