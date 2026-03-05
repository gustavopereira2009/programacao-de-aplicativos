comprimento = input ("o comprimento da peca de roupa esta emtre 10 e 12 cm (s/n)")
if comprimento ==  "n":
    print("REPROVAO: problema no comprimento")
else:
    largura = input("a largura esta entre 5 e 6 cm (s/n)")
    if largura == "s":
        print("PECA APROVADA")
    else:
        ("REPROVADO: problema na largura")