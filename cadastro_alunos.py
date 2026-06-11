import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               telefone TEXT,
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
                        insert  into alunos (nome, telefone, turma, idade,cpf)
                        values('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{cpf_aluno}' )
                        ''')
                        
cursor.execute(comando_inserir)
conexao.commit()
conexao.close 