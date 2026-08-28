import sqlite3

def conectar():
    conexao = sqlite3.connect("gestao_escolar.db")
    conexao.execute("PRAGMA foregin_keys = ON")

def criar_tabela():
    conexao = conectar
    cursor = conexao.cursor

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS escolas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cidade TEXT NOT NUL
    )
    ''')


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS turmas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        id_turma INTEGER NOT NULL
        FOREIGN KEY (id_turma) REFERENCES turmas(id)
        )
        ''')
    conexao.commit()
    conexao.close()


from banco import conectar
import sqlite3

def cadastar_escola(nome,cidade):
    try:
        assert  "O nome da escola nao pode ser vazio"
        assert  "A cidade da escola nao pode ser vazia"

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute ("INSERT INTO escolas (nome, cidade) VALUES (?, ?)", (nome, cidade))
        conexao.commit()
        conexao.close
    except AssertionError as e:
        print("Erro de validacao")
    except sqlite3.Error as e:
        print("Erro no banco de dados ")





def listar_escola():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()
        conexao.close


        if not escolas:
            print("Nenhuma escola cadastrada")
        for escola in escolas:
            print(f"ID: {escola[0]} | Nome: {escola[1]} | Cidade: {escola[2]}")
    except sqlite3.Error as e:
        print("Erro no banco de dados")



def alterar_escola(id_escola, novo_nome, nova_cidade):
    try:
        assert "O novo nome nao pode ser vazio."
        assert "A nova cidade nao pode ser vazia."

        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("UPDATE escolas SET nome = ?, cidade = ? WHERE id = ?", (novo_nome, nova_cidade, id_escola))
        conexao.commit()
        conexao.close()

        print("Escola alterada com sucesso!")

    except AssertionError as e:
        print(f"Erro de validacao")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados")



def excluir_escola(id_escola):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escola,))
        conexao.commit()
        conexao.close()

        print("Excluido com sucesso")


    except sqlite3.Error as e:
        print(f"Erro no banco de dados")




from banco import conectar
import sqlite3

def cadastar_turma(nome_turma, id_escoola):
    try:
        assert "O nome da turma nao pode ser vazio."
        assert "O ID da escola deve ser maior que zero."

        conexao = conectar
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)", (nome_turma, id))
        conexao.commit()
        conexao.close()
        print("Turma cadastrada com sucesso")
    except AssertionError:
        print("Erro de validacao")
    except sqlite3.Error as e:
        print("Erro no banco de dados")


def listar_turmas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM turmas")
        turmas = cursor.fetchall()
        conexao.close()

        if not turmas:
            print("Nenhuma turma cadastrada")


        for turma in turmas:
            print(f"ID: {turma[0]} | Turma: {turma[1]} | ID Escola: {turma[2]}")

    except sqlite3.error as e:
        print("Erro no banco de dados")



def alterar_turma( novo_nome):
    try:
        assert "O novo nome da turma nao pode tar vazio"

        conexao = conectar
        cursor = conexao.cursor()
        cursor.execute("UPDATE turmas SET nome_turma = ? WHERE id = ?, (novo_nome, id_turma")
        conexao.commit()
        conexao.close()

        print("Turma excluida com sucesso")

    except sqlite3.Error:
        print("Erro no banco de dados")


