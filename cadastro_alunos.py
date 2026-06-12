import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               telefone TEXT,
               turma TEXT,
               idade INTEGER,
               cpf TEXT UNIQUE NOT NULL
               )
               ''')

nome_aluno = input("digite o nome do aluno: ")
telefone_aluno = input("digite o telefone do aluno: ")
turma_aluno = input("digite a turma do aluno: ")
idade_aluno = int(input("digite a idade do aluno: "))
cpf_aluno = input("digite o cpf do aluno: ")

comando_inserir = (f'''
                        INSERT INTO alunos (nome, telefone, turma, idade,cpf)
                        VALUES ('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{cpf_aluno}' )
                        ''')
                        
cursor.execute(comando_inserir)
conexao.commit()

cursor.execute(''' select * from alunos ''')
todos_alunos = cursor.fetchall()

if not todos_alunos:
    print("Nenhum aluno cadastrado")
else:
    for aluno in todos_alunos:
        print(f" ID: {aluno[0]}, Nome: {aluno[1]}, Telefone: {aluno[2]}, Turma: {aluno[3]}, Idade: {aluno[4]}, CPF: {aluno[5]} ")

conexao.close()