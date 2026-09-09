import sqlite3

def conectar():
    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    return conexao, cursor


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


def excluir_truma(id_turma):
    try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM escolas WHERE id = ?", (id_turma,))
            conexao.commit()
            conexao.close()
    
            print("Excluido com sucesso")

    except sqlite3.Error as e:
        print("Erro no banco de dados")




def cadastrar_aluno():
    try:
        nome = input("Nome do aluno: ").strip()
        idade = int(input("Idade do aluno: "))
        id_turma = int(input("ID da Turma: "))
        
        assert nome != "", "O nome do aluno nao pode ser vazio."
        assert idade >= 3, "A idade do aluno deve ser igual ou superior a 3 anos."

        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, idade, id_turma) VALUES (?, ?, ?)", (nome, idade, id_turma))
        conexao.commit()
        conexao.close()
        print("Aluno cadastrado com sucesso!")
        
    except ValueError:
        print("Erro: Idade e ID da turma precisam ser numeros.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error:
        print("Erro: Essa turma nao existe no banco de dados.")

def listar_turma():
    try:

        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()
        conexao.close()
        
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("\n--- LISTA DE ALUNOS ---")
            for aluno in alunos:
                print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | ID Turma: {aluno[3]}")
    except sqlite3.Error as e:
        print(f"Erro ao listar: {e}")

def alterar_turma():
    try:
        id_busca = int(input("ID do aluno para alterar: "))
        nome = input("Novo nome do aluno: ").strip()
        idade = int(input("Nova idade do aluno: "))
        id_turma = int(input("Novo ID da turma: "))
        
        assert nome != "", "O nome nao pode ser vazio."
        assert idade >= 3, "A idade deve ser igual ou maior que 3 anos."


        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("UPDATE alunos SET nome = ?, idade = ?, id_turma = ? WHERE id = ?", (nome, idade, id_turma, id_busca))
        conexao.commit()
        conexao.close()

        
        print("Aluno alterado!")
    except ValueError:
        print("Erro: Digite dados numericos validos.")
    except AssertionError as e:
        print(f"Erro de validacao: {e}")
    except sqlite3.Error:
        print("Erro: Nao foi possivel alterar. Verifique se a turma existe.")

def excluir_turma():
    try:
        id_busca = int(input("ID do aluno para excluir: "))

        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM alunos WHERE id = ?", (id_busca,))
        conexao.commit()
        conexao.close()


        print("Aluno excluido!")
    except ValueError:
        print("Erro: O ID precisa ser um numero.")




import escola
import turma
import aluno

def menu_escolas():
    opcao = 0
    while opcao != 5:
        print("1. Cadastrar Escola")
        print("2. Listar Escolas")
        print("3. Alterar Escola")
        print("4. Excluir Escola")
        print("5. Voltar")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1: escola.cadastrar()
        elif opcao == 2: escola.listar()
        elif opcao == 3: escola.alterar()
        elif opcao == 4: escola.excluir()

def menu_turmas():
    opcao = 0
    while opcao != 5:
        print("1. Cadastrar Turma")
        print("2. Listar Turmas")
        print("3. Alterar Turma")
        print("4. Excluir Turma")
        print("5. Voltar")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1: turma.cadastrar()
        elif opcao == 2: turma.listar()
        elif opcao == 3: turma.alterar()
        elif opcao == 4: turma.excluir()

def menu_alunos():
    opcao = 0
    while opcao != 5:
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Alterar Aluno")
        print("4. Excluir Aluno")
        print("5. Voltar")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1: aluno.cadastrar()
        elif opcao == 2: aluno.listar()
        elif opcao == 3: aluno.alterar()
        elif opcao == 4: aluno.excluir()

def menu_principal():
    opcao = 0
    while opcao != 4:
        print("1. Gerenciar Escolas")
        print("2. Gerenciar Turmas")
        print("3. Gerenciar Alunos")
        print("4. Sair")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1:
            menu_escolas()
        elif opcao == 2:
            menu_turmas()
        elif opcao == 3:
            menu_alunos()
        elif opcao == 4:
            print("Saindo do sistema")

    menu_principal()









