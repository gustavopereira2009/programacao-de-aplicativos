def analisar_vendas(nome, lista_vendas, meta_mensal):
    total_vendas = 0
    quantidade_vendas = 0
    
    for venda in lista_vendas:
        total_vendas += venda
        quantidade_vendas += 1
