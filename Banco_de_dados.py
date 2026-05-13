estoque = []
def adicionar_produto(nome):
    """Adiciona um novo item à lista."""
    estoque.append(nome)
    print(f"Produto '{nome}' adicionado com sucesso!")

def listar_produtos():
    """Percorre a lista e exibe os itens com seus índices."""
    print("\n--- Lista de Produtos ---")
    if len(estoque) == 0:
        print("O estoque está vazio.")
    else:
        
        for i, produto in enumerate(estoque):
            print(f"{i} - {produto}")
    print("-------------------------")

def atualizar_produto(indice, novo_nome):
    """Substitui o nome de um produto existente pelo índice."""
    
    if 0 <= indice < len(estoque):
        produto_antigo = estoque[indice]
        estoque[indice] = novo_nome
        print(f"Produto '{produto_antigo}' atualizado para '{novo_nome}'.")
    else:
        print("Erro: Índice inválido!")

def remover_produto(indice):
    """Remove o item da lista utilizando o índice."""
    if 0 <= indice < len(estoque):
        
        produto_removido = estoque.pop(indice)
        print(f"Produto '{produto_removido}' removido com sucesso!")
    else:
        print("Erro: Índice inválido!")


def exibir_menu():
    """Menu principal que interage com o usuário."""
    while True:
        print("\n--- MENU ESTOQUE ---")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            adicionar_produto(nome)
            
        elif opcao == "2":
            listar_produtos()
            
        elif opcao == "3":
            listar_produtos()
            if len(estoque) > 0:
                indice = int(input("Digite o índice do produto para atualizar: "))
                novo_nome = input("Digite o novo nome: ")
                atualizar_produto(indice, novo_nome)
            
        elif opcao == "4":
            listar_produtos()
            if len(estoque) > 0:
                indice = int(input("Digite o índice do produto para remover: "))
                remover_produto(indice)
            
        elif opcao == "5":
            print("Saindo do programa. Até logo!")
            break 
            
        else:
            print("Opção inválida, tente novamente.")
exibir_menu()
