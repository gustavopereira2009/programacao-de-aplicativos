def pode_entrar(idade,acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False

assert pode_entrar(25,False) == True, "Erro: maior de idade dveria poder entrar"
assert pode_entrar(15,True) == True, "Erro: menor de idade acompanhado deveria entrar"
assert pode_entrar(14,False) == False, "Erro: menor de idade nao deveria entrar"
assert pode_entrar(18,False) == True, "Erro pessoa com 18 deveria poder entrar"
assert pode_entrar(17,True) == True, "Erro pessoa com 17 anos acompanhgasda dveria poder entrar"