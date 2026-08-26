#ex1
def dobrar(numero):
    return numero * 2


assert dobrar (3) == 6  
assert dobrar (0) == 1
assert dobrar (-2) == -4

# O assert dobrar(0) == 1
# Qual foi o resultado? 0
# Por que a funcao mutiplica o numero por 2 (0 * 2 = 0) enquanto o resultado esperado era 1





#ex2
def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"
assert situacao_aluno(6.01) == "Aprovado"



# Por que è a onde muda de reprovado para aprovado, e define quem passa de ano e quem reprova de ano



#ex3
def calcular_desconto(preco,percentual):
    return preco - (preco * (percentual/100))

assert calcular_desconto(100,10) == 90.0
assert calcular_desconto(200,20) == 160.0
assert calcular_desconto(50,50) == 25.0