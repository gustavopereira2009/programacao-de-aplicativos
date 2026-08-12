def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_situacao(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"


# Testes da função calcular_media
assert calcular_media(8, 6) == 7
assert calcular_media(10, 10) == 10
assert calcular_media(0, 0) == 0

# Testes da função verificar_situacao
assert verificar_situacao(7) == "Aprovado"
assert verificar_situacao(6) == "Aprovado"
assert verificar_situacao(5.9) == "Reprovado"

print("Todos os testes passaram!")








# 1) Se todos os testes passarem o codigo vai rodar normalmente sem nehum erro

# 2) O teste que verifica o valor minimo para aprovacao è assert verificar_situacao (6) == "Aprovado"

# 3) Porque se ela der falha todos aluno serim aprovados ate os que tem media menor de 6

# 4) A pessoa que tira media 6 reprova também 