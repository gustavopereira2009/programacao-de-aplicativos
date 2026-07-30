import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect("sistema_escola.db") 
    cursor = conexao.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO series (nome_serie, id_escola) 
            VALUES (?, ?)
        ''', (nome_serie, id_escola))
        
        conexao.commit()
        print("Série cadastrada com sucesso!")
        
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente ou nome de série duplicado!")
    finally:
        conexao.close()

# O nome do banco de dados na linha de conexão está sem aspas, o que causa um erro de sintaxe
# INSERIR O PRAGMA - CORRIGIR