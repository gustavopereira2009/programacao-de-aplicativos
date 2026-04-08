valor = float(input("Qual e o valor da compra ? R$:"))

if valor > 100.00:
    desconto = valor * 0.10
    final = valor - desconto
print(f"Valor da sua compra: R$ {valor}")