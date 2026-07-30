import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE  TABLE IF NOT EXISTS escolas (
                   id INTEGER PRIMAY KEY AUTOINCREMENT,
                   nome_serie, TEXT
                   id_escola INTEGER, INTEGER
                   FOREIGN KEY (id_escola) REFERENCES escola(id)
                   )
                   ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS series (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT 
                   )
                   ''')
    conexao.commit()
    conexao.close()
 # O código da erro porque está tentando criar uma relação com a tabela escola antes mesmo de ela existir no banco de dados.


    
    