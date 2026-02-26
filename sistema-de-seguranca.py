nome_usuario = input("digite o nome de usuario")
codigo_secreto = int(input("digite o codigo de seguranca"))

if nome_usuario == "admin" and codigo_secreto == 900:
    print ("acesso ao servidor liberado. sistema online")
else:
    print("falhana autrenticacao. alerta de seguranca ligado")