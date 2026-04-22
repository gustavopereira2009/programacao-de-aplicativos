def analisar_desempenho (nota):

    if nota >=9:
        return "execelente"

    if nota >=7:
        return "Bom"

    if nota >= 5:
        return "regular"
    else:
        return "Insuficiente"

nota_usuario = int(input("qual e a sua nota ?"))
mensagem = analisar_desempenho(nota_usuario)
print(mensagem)