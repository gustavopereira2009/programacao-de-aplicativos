temperatura = float("qual a temperatura atua")

if temperatura <= 30:
    print("clima estavel")
else:
    print("alerta de calor")

    umidade = float(input("digite a umidade atual (%): "))

    if umidade < 40:
        print("acao: ligar irrigacao!")
    else:
        print("acao: ligar apenas ventiladores")