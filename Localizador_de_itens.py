nomes = ["Gustavo,Bruno,Arthur,Pedro,Joao,Tiago,Yuri"]
buscar_nome= input("Digite o nome de quem voce esta procurando")

def esta_na_lista(nome,buscar_nome):
    for n in nomes:
        if n == buscar_nome:
            return "Encontrado"
        return  "não disponivel"

msg = esta_na_lista(nomes,buscar_nome)
print(msg)