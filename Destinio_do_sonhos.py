open('viagem.txt','w').close

def criar():
    destino = input("Digite o proximo destino")
    with open('viagem.txt','a') as f:
        f.write(destino + '\n' )
        print("proxima viagem adicionada")


def ler():
    with open('viagem.txt','r') as f:
        destino = f.readline()

        i = 0
        for destino in destino:
            print(f"{i} - {destino.strip()}")
            i+=1

def atualizar():
    ler()
    idx = input("Digite o destino que voce deseja alterar")
    novo_destino = input("Novo destino: ")

    with open('viagem.txt','r') as f:
        linhas = f.readlines()

        linhas[idx] = novo_destino + '\n'

        with open('viagem.txt','w') as f:
            f.writelines(linhas)
            print("Destino removido")

while True:
    print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
    opcao = input("Escolha: ")
    
    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '5': break 