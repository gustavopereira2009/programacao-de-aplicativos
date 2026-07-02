import sqlite3

def cadastrar_turma(nome,id_serie,id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreing_keys = ON;")
    try:
        cursor.execute("INSERT INTO turmas (nome_turma,id_serie,id_professor) VALUES (?,?,?)"), (nome , id_serie , id_prof)
        conexao.commit()
    except sqlite3.IntegrityError:
        ("Professor ou série não existe.")
    finally:
        conexao.close()

# pode dar erro por que não existe o id prof entao coloca os try, except junto com o erro que ai aparece 
# se acontecr algo errado nem o commit nem o close sera executado
