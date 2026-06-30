import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    id_turma = input("Digite o ID numerico da turma: ")

    
    if id_turma.isdigit():
        id_numero = int(id_turma) 
        
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?,?)", (nome, id_numero))
        conexao.commit()
        conexao.close() 
        
        print("Salvo com sucesso!")
    else:
        print("Erro: Você não digitou um número válido!")

 # O código quebra porque o except captura apenas erros de banco de dados (sqlite3.Error), ignorando o erro de conversão de texto para número (ValueError) e deixando de executar a função de fechamento por falta de parênteses em conexao.close





