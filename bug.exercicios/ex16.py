def menu():
    while True:
        print("1. Cadastrar Aluno")
        print("2. Sair")
        opcao = input ("Escolha: ")

        if opcao == "1":
            print("Cadastrando...")
       
       
        elif opcao == "2":
            print("Saindo do progama.")
            break
        
        else:
            print("Opcao invalida")

menu()


# O erro era que o pass nao encerrava. tem que usar algo como break ou algo do tipo