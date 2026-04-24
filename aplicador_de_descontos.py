lista_com = [150.0,80.0,200.0,50.0]
nova_lista = []
for preco in lista_com:
        if preco > 100.0:
            preco_desconto = preco * 0.85
            nova_lista.append(round(preco_desconto, 2))
        else:
            nova_lista.append(preco)