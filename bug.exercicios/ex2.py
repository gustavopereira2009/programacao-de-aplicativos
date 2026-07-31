import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect("sistema_escola.db")
    conexao.execute("PRAGMA foreign_keys = ON")  
    cursor = conexao.cursor()
    
    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome_serie, id_escola)) 
        conexao.commit()
        print("Série cadastrada com sucesso!")
        
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente ou nome de série duplicado!")
    finally:
        conexao.close()

# Tinha que ter o pragma para dar certo

# INSERIR O PRAGMA - CORRIGIR  * ja fiz