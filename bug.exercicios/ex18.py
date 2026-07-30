import sqlite3

def cadastrar_lista_alunos():
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)]

    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    cursor.executemany(
        "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
        lista
    )

    conexao.commit()
    conexao.close()

# tinha que ter o for para pecorre a lista

# remover o for e ve se esta certo *