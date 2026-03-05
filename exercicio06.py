curso = input("voce concluiu o curso de seguranca (s/n)")
if curso == "n":
    print("Acesso Negado: Faca o treinamento primeiro")
else:
    instrutor = input("O instrutor ta na sala (s/n)")
    if instrutor == "s":
       print("Acesso liberado: Opercao iniciada")
    else:
        print("Aguarde o instrutor para ligar a maquina")