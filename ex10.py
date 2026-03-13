cores = ["Vermelho", "Verde", "Azul", "Amarelo", "Preto"]
numero = int(input("Digite um número de 1 a 5: "))

if 1 <= numero <= 5:
    print("A cor escolhida é:", cores[numero - 1])
else:
    print("Número inválido!")