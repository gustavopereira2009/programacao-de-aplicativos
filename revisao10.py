almoxarifado = []

while True:
    print("\n=== Sistema do Almoxarife ===")
    print("1 - Adicionar item")
    print("2 - Listar itens")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        item = input("Digite o nome do item: ")
        almoxarifado.append(item)
        print(f"Item '{item}' adicionado com sucesso!")
        
    elif opcao == "2":
        if not almoxarifado:
            print("O almoxarifado está vazio.")
        else:
            print("Itens no almoxarifado:")
            for i, item in enumerate(almoxarifado, start=1):
                print(f"{i}. {item}")
                
    elif opcao == "3":
        print("Saindo do sistema...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")