import sqlite3

def conectar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS professores(
        id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_professor TEXT NOT NULL,
        telefone_professor TEXT,
        materia_professor TEXT,
        idade_professor INTEGER,
        cpf_professor TEXT UNIQUE NOT NULL,
        salario_professor TEXT NOT NULL,
        nome_da_escola TEXT
    )
    ''')

    conexao.commit()
    return conexao, cursor


def cadastrar_professor(cursor, conexao):
    print(" CADASTRAR PROFESSOR ")

    nome_professor = input("Digite o nome do professor: ")
    telefone_professor = input("Digite o telefone do professor: ")
    materia_professor = input("Digite a matéria do professor: ")
    idade_professor = int(input("Digite a idade do professor: "))
    cpf_professor = input("CPF: ")
    salario_professor = input("Digite o salário do professor: R$ ")
    nome_da_escola = input("Digite a escola que o professor trabalha: ")

    cursor.execute(f'''
    INSERT INTO professores
    (nome_professor, telefone_professor, materia_professor, idade_professor, cpf_professor, salario_professor, nome_da_escola)
    VALUES
    ('{nome_professor}', '{telefone_professor}', '{materia_professor}', {idade_professor}, '{cpf_professor}', '{salario_professor}', '{nome_da_escola}')
    ''')

    conexao.commit()
    print("Professor cadastrado com sucesso!")


def listar_professores(cursor, conexao):
    print(" LISTA DE PROFESSORES")

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()

    if not professores:
        print("Nenhum professor cadastrado...")
        return

    for prof in professores:
        print(f"ID: {prof[0]} | Nome: {prof[1]} | Tel: {prof[2]} | Matéria: {prof[3]} | Idade: {prof[4]} | CPF: {prof[5]} | Salário: R${prof[6]} | Escola: {prof[7]}")


def alterar_professor(cursor, conexao):
    print(" ALTERAR PROFESSOR ")

    listar_professores(cursor, conexao)

    id_professor = input(" Digite o ID do professor que deseja alterar: ")

    nome_professor = input("Novo nome: ")
    telefone_professor = input("Novo telefone: ")
    materia_professor = input("Nova matéria: ")
    idade_professor = int(input("Nova idade: "))
    cpf_professor = input("Novo CPF: ")
    salario_professor = input("Novo salário: R$ ")
    nome_da_escola = input("Nova escola: ")

    cursor.execute(f'''
    UPDATE professores SET
        nome_professor = '{nome_professor}',
        telefone_professor = '{telefone_professor}',
        materia_professor = '{materia_professor}',
        idade_professor = {idade_professor},
        cpf_professor = '{cpf_professor}',
        salario_professor = '{salario_professor}',
        nome_da_escola = '{nome_da_escola}'
    WHERE id_professor = {id_professor}
    ''')

    conexao.commit()
    print("Dados alterados com sucesso!")


def excluir_professor(cursor, conexao):
    print(" EXCLUIR PROFESSOR ")

    listar_professores(cursor, conexao)

    id_professor = input("Digite o ID do professor que deseja excluir: ")

    cursor.execute(f"DELETE FROM professores WHERE id_professor = {id_professor}")

    conexao.commit()
    print("Professor excluído com sucesso!")


def listar_alunos_professores(cursor, conexao):
    print(" ALUNOS E PROFESSORES ")

    cursor.execute("""
    SELECT alunos.nome_aluno,
           professores.nome_professor,
           professores.materia_professor
    FROM alunos
    INNER JOIN professores
    ON alunos.id_professor = professores.id_professor
    """)

    dados = cursor.fetchall()

    if not dados:
        print("Nenhum relacionamento encontrado...")
        return

    for dado in dados:
        print(f"Aluno: {dado[0]} | Professor: {dado[1]} | Matéria: {dado[2]}")


def Menu():
    conexao, cursor = conectar()

    while True:
        print("\n======== MENU ESCOLA ========")
        print("1. Cadastrar Professor")
        print("2. Listar Professores")
        print("3. Alterar Professor")
        print("4. Excluir Professor")
        print("5. Listar Alunos e Professores")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_professor(cursor, conexao)

        elif opcao == '2':
            listar_professores(cursor, conexao)

        elif opcao == '3':
            alterar_professor(cursor, conexao)

        elif opcao == '4':
            excluir_professor(cursor, conexao)

        elif opcao == '5':
            listar_alunos_professores(cursor, conexao)

        elif opcao == '6':
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")

    conexao.close()


Menu()