ataque = int(input("digite o dano do ataque"))
defesa = int(input("digite a defesa do vilao"))

dano = ataque - defesa

if ataque <= defesa:
    print ("O vilao bloqueou o ataque",dano)
elif ataque >= defesa:
    print("ataque critico! voce casou dano ao vilao,o danocausado foi ", dano)