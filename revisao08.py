peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:}")

if imc > 25:
    print("Você está acima do peso (sobrepeso).")
else:
    print("Seu peso está dentro do normal.")