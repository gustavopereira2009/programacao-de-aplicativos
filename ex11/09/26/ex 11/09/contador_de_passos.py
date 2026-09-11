numeros = list(range(1,101))

def busca_sequencial(lista,valor):
    comparacoes = 0

    for i in range(len(lista)):
        comparacoes += 1

        if lista[i] == valor:
            print("Busca sequencial:")
            print("Valor encotrado na posicao:", i)
            print("Comparacoes realizadas:", comparacoes)

        print("Valor nao encontrado")
        return -1



def busca_binaria(lista,valor):
    inicio = 0
    fim = len(lista) -1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes +=1

        if lista[meio] == valor:
            print("Busca Binaria")
            print("Valor encotrado na posicao:", meio)
            print("Comparacoes realizadas:", comparacoes)
            return meio 

        elif lista[meio] < valor:
            inicio = meio + 1

        else:
            fim = meio - 1

    print("Valor nao encontrado")
    return -1

busca_sequencial(numeros, 95)
busca_binaria(numeros, 95 )