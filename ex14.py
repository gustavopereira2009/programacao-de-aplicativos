vagas = ["Ocupado", "Livre", "Ocupado", "Livre"]
indice = int(input("digite o numero da vaga (0 a 3):"))

if 0 <= indice <=3:
    if indice % 2 == 0 and vagas[indice] == "livre":
        print(f"vagas{indice} autoizado para estacionar")
    else:
        print(f"vaga {indice} indisponivel ou fora da regra")
else:
    print("indice invalido")