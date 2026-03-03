usuario = input("qual o nome e usuario")
senha = int(input("qual a senha"))

if (usuario == "admin" or usuario == "root") and senha == 1234:
    print("acesso liberado")
else:
   print("acesso negado")