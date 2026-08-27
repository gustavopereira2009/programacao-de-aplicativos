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


#ex4
def eh_par(numero):
    return numero % 2 == 0
assert eh_par(3) is False

# O problema estava no teste :3 nao é par logo is True tava errado



#ex5
def frete_gratis(valor):
    return valor >= 200

def pode_votar(idade):
    return idade >= 16

def senha_valida(senha):
    return len(senha) >= 8


assert frete_gratis(199.99) is False
assert frete_gratis(200) is True
assert frete_gratis(200.01) is True

assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True


assert senha_valida("1234567") is False
assert senha_valida("12345678") is True
assert senha_valida("123456789") is True


#ex6
def situacao_faltas(faltas):
    if faltas <= 4:
        return "Regular"
    elif faltas <=10:
        return "Atençao"
    else:
        return "Reprovado por falta"


assert situacao_faltas(0) == "Regular"
assert situacao_faltas(4) == "Regular"
assert situacao_faltas(5) == "Atençao"
assert situacao_faltas(10) == "Atençao"
assert situacao_faltas(11) == "Reprovado por falta"


#ex7

def calcular_media(n1, n2):
    return (n1 + n2) / 1


def calcular_media_corrigida(n1, n2):
    return (n1 + n2) / 2


assert calcular_media_corrigida(10, 10) == 10
assert calcular_media_corrigida(5, 5) == 5
assert calcular_media_corrigida(0, 10) == 5

# funcao escolhida: calcular_media
# Regra errada : tava divindo por 1 e nao por 2





#ex8
def pode_votar(idade):
    return idade >= 16

assert pode_votar(15) is False
assert pode_votar(16) is True