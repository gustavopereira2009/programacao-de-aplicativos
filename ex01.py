ID = int(input("qual o seu ID ?"))
valor = int(input("qual o valor da sua compra ?"))

# verificando a regra 
if ID % 2 == 0 and valor > 5000:
    print(f"parabens, usario {ID}! Voce ganhou um cumpom para sua compra de R$ {valor}")
else:
    print(f"Obrigado pela compra, usario {ID}. Continue acompanhado nossas promocoes!")