def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)
assert calcular_desconto(100,0) == 100, "Erro: O preço deveria permanecer 100"