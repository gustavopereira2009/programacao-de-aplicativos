senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input("digite a senha: ")
    if senha != senha_correta:
        print("senha incorreta. Tente novamente")

    print("Bem-vindo")