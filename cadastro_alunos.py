import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    turma TEXT,
    idade INTEGER,
    cpf TEXT UNIQUE NOT NULL,
    id_professor INTEGER
)
""")

nome = input("Digite o nome do aluno: ")
telefone = input("Digite o telefone: ")
turma = input("Digite a turma: ")
idade = int(input("Digite a idade: "))
cpf = input("Digite o CPF: ")

print(" Professores cadastrados: ")

cursor.execute("SELECT * FROM professores")
professores = cursor.fetchall()

for professor in professores:
    print(f"ID: {professor[0]} - Nome: {professor[1]}")

id_professor = int(input("Digite o ID do professor do aluno: "))

cursor.execute(f'''
INSERT INTO alunos(nome, telefone, turma, idade, cpf, id_professor)
VALUES('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}', {id_professor})
''')

conexao.commit()

print("\nLista de alunos com seus professores:\n")

cursor.execute("""
SELECT alunos.nome,
       professores.nome_professor
FROM alunos
INNER JOIN professores
ON alunos.id_professor = professores.id_professor
""")

dados = cursor.fetchall()

for dado in dados:
    print("Aluno:", dado[0])
    print("Professor:", dado[1])
    print("------------------")

conexao.close()