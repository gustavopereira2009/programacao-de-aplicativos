senha_correta = "12345"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso permitido!")
        break  
    else:
        tentativas += 1
        print(f"Senha incorreta! Tentativa {tentativas} de {max_tentativas}.")
else:
    print("Acesso bloqueado")