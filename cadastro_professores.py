import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos(
              id INTEGER  PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               telefone TEXT,
               materia TEXT,
               idade INTERGER,
               cpf TEXT UNIQUE NOT NULL,
               salario REAL NOT NULL,
               escola TEXT NOT NULL
               )
               ''')
conexao.commit

nome_professor = input("Digite o nome do professor: ")
telefone_professor = input("Digite o telefone do professor: ")
materia_professor = input("Digite a materia do professor: ")
idade_professor = int(input("digite a idade do professor: "))
cpf_aluno = input("Digite o cpf do professor: ")
salario_professor  = float(input("Digite o salario do propfessor: "))
escola = input("Digite a escola que o professor trabalha: ")

comando_inserir = (f'''
                       INSERT INTO 





