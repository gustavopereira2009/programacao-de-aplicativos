import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()



cursor.execute("""
CREATE TABLE IF NOT EXISTS professor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    materia TEXT,
    idade INTEGER,
    cpf TEXT,
    salario REAL,
    escola TEXT,
    endereco TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS aluno(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    telefone TEXT,
    endereco TEXT,
    cidade TEXT,
    estado TEXT,
    id_professor INTEGER,
    FOREIGN KEY(id_professor) REFERENCES professor(id)
)
""")

conexao.commit()



def cadastrar_professor():

    try:

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        materia = input("Materia: ")
        idade = int(input("Idade: "))
        cpf = input("CPF: ")
        salario = float(input("Salario: "))
        escola = input("Escola: ")
        endereco = input("Endereco: ")

        cursor.execute("""
        INSERT INTO professor
        (nome,telefone,materia,idade,cpf,salario,escola,endereco)
        VALUES (?,?,?,?,?,?,?,?)
        """,(nome,telefone,materia,idade,cpf,salario,escola,endereco))

        conexao.commit()

        print("Professor cadastrado!")

    except:

        print("Erro ao cadastrar professor.")



def listar_professores():

    try:
        cursor.execute("SELECT * FROM professor")
        dados = cursor.fetchall()
        for professor in dados:

            print("----------------------------")
            print("ID:", professor[0])
            print("Nome:", professor[1])
            print("Telefone:", professor[2])
            print("Materia:", professor[3])
            print("Idade:", professor[4])
            print("CPF:", professor[5])
            print("Salario:", professor[6])
            print("Escola:", professor[7])
            print("Endereco:", professor[8])

    except:

        print("Erro ao listar.")



def alterar_professor():

    try:

        listar_professores()

        id = int(input("ID do professor: "))

        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        materia = input("Nova materia: ")
        idade = int(input("Nova idade: "))
        cpf = input("Novo CPF: ")
        salario = float(input("Novo salario: "))
        escola = input("Nova escola: ")
        endereco = input("Novo endereco: ")

        cursor.execute("""
        UPDATE professor
        SET
        nome=?,
        telefone=?,
        materia=?,
        idade=?,
        cpf=?,
        salario=?,
        escola=?,
        endereco=?
        WHERE id=?
        """,(nome,telefone,materia,idade,cpf,salario,escola,endereco,id))

        conexao.commit()

        print("Professor alterado!")

    except:

        print("Erro ao alterar.")



def excluir_professor():

    try:
        listar_professores()
        id = int(input("ID para excluir: "))
        cursor.execute("DELETE FROM professor WHERE id=?",(id,))
        conexao.commit()
        print("Professor excluido!")

    except:
       print("Erro ao excluir.")



def menu():

    while True:

        print("1 - Cadastrar Professor")
        print("2 - Listar Professores")
        print("3 - Alterar Professor")
        print("4 - Excluir Professor")
        print("5 - Aluno")
        print("6 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_professor()

        elif opcao == "2":
            listar_professores()

        elif opcao == "3":
            alterar_professor()

        elif opcao == "4":
            excluir_professor()

        elif opcao == "5":
            break

        elif opcao == "6":
            conexao.close()
            break

        else:
            print("Opcao invalida.")


menu()