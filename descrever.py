import json # sabe que vc vai usar o json
import os # importar a biblioteca para mexer em arquivos e pastas do computador

BANCO_DADOS = 'alunos.json' # cria o arquivo

def cadastrar(): # cria uma funcao para cadastrar
    print("\n--- Novo Cadastro ---") # para aparecer bonito no terminal

    if os.path.exists(BANCO_DADOS): # Verifica se o arquivo do banco de dados já existe no computador
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo
            alunos = json.load(f) # cria uma variavel 
    else: # se algo der errado ela que vai atuar
        alunos = [] # ele cria uma variavel para cadrastar o aluno

    novo_aluno = { # ele cria uma variavel
        "nome": input("Nome: "), # ele pergunta seu nome
        "telefone": input("Telefone: "), # ele pergunta seu telefone
        "turma": input("Turma: "), # ele pergunta a sua turma
        "idade": int(input("Idade: ")), # ele pergunta a sua idade
        "cpf": input("CPF: ") # ele pergunta seu cpf
    }
    
    alunos.append(novo_aluno) # ele adiciona alunos na lista novos_alunos

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # ele abre o arquivo
        json.dump(alunos, f, indent=4, ensure_ascii=False) # ele organiza para fiar boniuto no terminal e facil de enteder
        
    print("Aluno cadastrado com sucesso!") # ele aperece quando o aluno for cadrastado

def listar(): # ele cria uma funcao para listar os alunos
    print("\n--- Lista de Alunos ---") # para ficar bonito no terminal e identificar que e para listar
    
    if os.path.exists(BANCO_DADOS): # Verifica se o arquivo do banco de dados já existe no computador
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # ele abre o arquivo
            alunos = json.load(f) # ele cria uma variavel para ler quem ta na lista
    else: # se alg de errado ele que vai aparecer
        alunos = [] # ele cria uma lista nova com a variavel aluno

    if not alunos: # ekle verifica se existe o aluno
        print("Nenhum aluno cadastrado.") # aparece caso nao haja nenhum aluno cadarstado
        return # ele retorna a mensagem

    for aluno in alunos: # ele caca um aluno na lista alunos
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") # ele aparece sua informacos no terminal

def atualizar(): # ele cria a funcao para atualizar
    print("\n--- Atualizar Aluno ---") # ele fica organizado no terminal e identifica que e para atualizar 
    if not os.path.exists(BANCO_DADOS): # Verifica se o arquivo do banco de dados já existe no computador
        print("Nenhum aluno cadastrado no sistema.") # aparece caso nao tenha aluno cadarstado
        return # ele retorna a mensagem

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # ele abre o arquivo
        alunos = json.load(f) # ele o que ta na lista
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) # vereficar se o cpf esta certo
    
    for aluno in alunos: # busca aluno na lista alunos
        if aluno['cpf'] == cpf_busca: # ele verifi o cpf
            print(f"Editando dados de: {aluno['nome']}") # ele edita os seus dados
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # ele edita seu nome
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] # ele edita seu telefone
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] # ele edita sua turma
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) # ele edita sua idade
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] # ele edita o seu cpf
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # ele abre o arquivo
                json.dump(alunos, f, indent=4, ensure_ascii=False) # ele deixa bonito no terminbal e deixa organizado para ler o codigo
            print("Dados atualizados com sucesso!") # aparece essa mensagem quando voce atualiza os dados 
            return # ele retorna a mensagem
            
    print("Aluno não encontrado.") # aperece caso nao exista o aluno

def excluir(): # ele cria uma funcao para excluir
    print("\n--- Excluir Aluno ---") # para ficar organizado nno terminal e identificar que e para excluir
    if not os.path.exists(BANCO_DADOS): # Verifica se o arquivo do banco de dados já existe no computador
        print("Nenhum aluno cadastrado no sistema.") # caso nao tenha aluno cadrastado aparece essa mensagen
        return # ele retorna a mensagem

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # ele abre o arquivo
        alunos = json.load(f) # ela le o que ta no arquivo
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: ")) # para voce digitar o id do aluno que voce deseja remover
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] # ele cria uma variavel nova e uma lista para excluir
    
    if len(nova_lista) < len(alunos): # Verifica se a nova lista tem menos alunos que a lista original.
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # ele abre o arquivo
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # ele fica organizqado no terminal e facil para leitura de codgo
        print("Aluno removido com sucesso!") # aparece caso o aluno seja removido
    else: # caso algo der errado ele que aparece 
        print("Aluno não encontrado.") # # aparece caso nenhum aluno seja encontrado

def menu(): # cria uma funcao para o menu
    if not os.path.exists(BANCO_DADOS): # Abre o arquivo do banco de dados para salvar novas informações nele
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # ele abre o arquivo
            json.dump([], f) # Salva uma lista vazia dentro do arquivo aberto

    while True: # Cria uma repetição que roda o código para sempre até ser forçada a parar
        print("\n=== SISTEMA ESCOLAR ===") # aparece a mensagem no terminal
        print("1. Cadastrar Aluno") # para cadarstar o aluno
        print("2. Listar Alunos") # para listar os alunos
        print("3. Atualizar Aluno") # para atualizar o aluno
        print("4. Excluir Aluno") # para excluir o aluno
        print("5. Sair") # para sair
        
        opcao = input("Escolha uma opção: ") # para escolher uma opcao
        
        if opcao == '1': cadastrar() # opcao para cadrastar
        elif opcao == '2': listar() # opcao para listar
        elif opcao == '3': atualizar() # opcao para atualizar
        elif opcao == '4': excluir() # opcao para excluir
        elif opcao == '5': break # Para a repetição e fecha o programa se o usuário digitar a opção
        else: print("Opção inválida!") # caso nao tenhga nenhuma opcao

menu() # ele chama funcao