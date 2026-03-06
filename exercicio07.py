temperatura = float(input("qual a temperatura atual"))

if temperatura <= 30:
    print("clima estavel")
elif temperatura > 30.0:
    print("alerta de calor")

    umidade = float(input("digite a umidade atual "))
if umidade < 40.0:
    print("acao: ligar irrigacao!")
elif umidade > 40.0:
    print("acao: ligar apenas ventiladores")