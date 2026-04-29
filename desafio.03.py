saldo = 1000.00

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":  
        valor = float(input("Digite o valor para depósito: R$ "))

        if valor > 0:
            saldo += valor
            print(f"Depósito realizado com sucesso!")
        else:
            print("Valor inválido! O depósito deve ser maior que zero.")

    elif opcao == "2":  
        valor = float(input("Digite o valor para saque: R$ "))

        if valor > 0 and (valor <= saldo or valor == 100):
            saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saque não autorizado!")

    elif opcao == "3":  
        print("\n=== EXTRATO ===")
        print(f"Saldo atual: R$ {saldo}")

    elif opcao == "4":
        print("Encerrando sistema...")

    else:
        print("Opção inválida! Tente novamente.")