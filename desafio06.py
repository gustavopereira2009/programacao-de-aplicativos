livros_disponiveis  = ["Python pro", "Banco de dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
escolha = input("Digite o nome do livro que voce deseja: ")

if escolha in livros_disponiveis:
    livros_disponiveis .remove(escolha)
    livros_disponiveis.append(escolha)
else:
    print("Desculpe, este livro nao esta no acervo.")

escolha = input("Digite o nome do livro que voce esta devolvendo")
if escolha in livros_emprestados:
    livros_emprestados.remove(escolha)
    livros_disponiveis.append(escolha)
else:
    print("esse livro nao conta como emprestado.")

    del livros_emprestados[0:2]

    print(f"estado final das duas listas {livros_disponiveis} e {livros_emprestados}")