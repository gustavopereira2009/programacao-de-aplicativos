def criar_arquivo():
    open('viagem.txt','w').close()

def criar():
    destino = input("Digite o proximo destino: ")
    with open('viagem.txt','a') as f:
        f.write(destino + '\n' )
        print("proxima viagem adicionada")


def ler():
    with open('viagem.txt','r') as f:
        destino = f.readlines()                                                            

        i = 0
        for destino in destino:
            print(f"{i} - {destino.strip()}")
            i+=1

def atualizar():
    ler()
    idx = int(input("Digite o destino que voce deseja alterar"))
    novo_destino = input("Novo destino: ")

    with open('viagem.txt','r') as f:
        linhas = f.readlines()

        linhas[idx] = novo_destino + '\n'

        with open('viagem.txt','w') as f:
            f.writelines(linhas)
            print("Destino atualizado")


def deletar():
    ler()
    idx = int(input("Digite o destino que voce deseja excluir"))

    with open('viagem.txt','r') as f:
         linhas = f.readlines()
    
    del linhas[idx]

    with open('viagem.txt','w') as f:
        f.writelines(linhas)
        print("Destino Removido")


while True:
    print("\n 1-Adicionar destino  \n 2-Listar Sujestões  \n 3-Editar Sujestão  \n 4-Remover Sujestões  \n 5-Sair")
    opcao = input("Escolha: ")
    
    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break 