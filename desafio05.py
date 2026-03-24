autorizados = ["Alice", "Bob", "Carlos"]
nome = input("digite o nome do pesquisador: ")

if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"Acesso permitido! O pesquisador {nome} esta na posicao {indice}")
    remover = input("deseja remover o pesquisador dessa listra? (S/N):")
    if remover == "sim":
        autorizados.remove(nome)
    print("pesquisador removido.")
    print(f"lista atualizada:", {autorizados})
else:
    print(f"Acesso Negado! O pesquisador {nome} não foi encontrado.")

    cadastrar = input("deseja cadastrar esse novo pesquisador ? (S/N)")
    if cadastrar == "sim":
        autorizados.append(nome)
        print("pesquisador cadastrado")
        print("lista final:", autorizados)
    else:
        print("nenhuma alteracao feita")