def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)
assert calcular_desconto(100,0) == 100, "Erro: O preço deveria permanecer 100"
assert calcular_desconto(100.0,10) == 90.0, "Erro: O preço deveria ser 90"
assert calcular_desconto(200.0,50) == 100.0, "Erro: O preço deveria ser 100"
assert calcular_desconto(50.0,100) == 0.0, "Erro: O preço dveria ser 0"
assert calcular_desconto(49.90,10) == 44.91, "Erro: O preço deveria ser 44.91"