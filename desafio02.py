cargo = str(input("qual o seu cargo?"))
codigo_de_acesso = int(input("digite o codigo de acesso"))
botao_de_emergencia = input("voce pressionou botao de emergencia(s/n)")
epi = input("voce possui equipamentio de protecao completo(s/n)")

if (cargo == "engenheiro" or cargo == "tecnico") and (codigo_de_acesso == 1234 or botao_de_emergencia == "s") and epi == "s":
    print("acesso liberado")
else:
    print("acesso negado")